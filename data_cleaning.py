import numpy as np
import pandas as pd
from tqdm import tqdm 

df = pd.read_csv("dirty_cafe_sales.csv")

# Create a copy to preserve the original dataframe
df_cleaned = df.copy()

# Clean column names
df_cleaned.columns = df_cleaned.columns.str.strip().str.lower().str.replace(" ","_")

# Convert numeric columns to numeric type
df_cleaned["quantity"] = pd.to_numeric(df_cleaned["quantity"], errors="coerce")
df_cleaned["price_per_unit"] = pd.to_numeric(df_cleaned["price_per_unit"], errors="coerce")
df_cleaned["total_spent"] = pd.to_numeric(df_cleaned["total_spent"], errors="coerce")

# Clean the 'item' column
df_cleaned["item"] = df_cleaned["item"].str.strip().str.lower()

invalid_items = ["error", "unknown"]
df_cleaned["item"] = df_cleaned["item"].replace(invalid_items, pd.NA)

missing_item_mask = df_cleaned['item'].isna()

df_cleaned.loc[missing_item_mask & (df_cleaned['price_per_unit'] == 5), 'item'] = 'salad'
df_cleaned.loc[missing_item_mask & (df_cleaned['price_per_unit'] == 1), 'item'] = 'cookie'
df_cleaned.loc[missing_item_mask & (df_cleaned['price_per_unit'] == 2), 'item'] = 'coffee'
df_cleaned.loc[missing_item_mask & (df_cleaned['price_per_unit'] == 1.5), 'item'] = 'tea'

missing_items = df_cleaned[df_cleaned['item'].isna()]

for idx in tqdm(missing_items.index):
    row = df_cleaned.loc[idx]

    match = df_cleaned[
        (df_cleaned['quantity'] == row['quantity']) &
        (df_cleaned['price_per_unit'] == row['price_per_unit']) &
        (df_cleaned['payment_method'] == row['payment_method']) &
        (df_cleaned['item'].notna())
    ]

    if not match.empty:
        predicted_item = match['item'].mode().iloc[0]
        df_cleaned.at[idx, 'item'] = predicted_item

df_cleaned = df_cleaned[df_cleaned['item'].notna()]

price_map = {
    'coffee': 2,
    'cake': 3,
    'cookie': 1,
    'salad': 5,
    'smoothie': 4,
    'sandwich': 4,
    'juice': 3,
    'tea': 2
}

mask_item = df_cleaned['price_per_unit'].isna() & df_cleaned['item'].notna()

df_cleaned.loc[mask_item, 'price_per_unit'] = df_cleaned.loc[mask_item, 'item'].map(price_map)

# Fill missing values in total_spent column
mask = df_cleaned["total_spent"].isna() & df_cleaned["quantity"].notna() & df_cleaned["price_per_unit"].notna()
df_cleaned.loc[mask, "total_spent"] = df_cleaned.loc[mask, "quantity"] * df_cleaned.loc[mask, "price_per_unit"]

ppu_mask = df_cleaned["price_per_unit"].isna() & df_cleaned["total_spent"].notna() & df_cleaned["quantity"].notna() & (df_cleaned["quantity"] != 0)
df_cleaned.loc[ppu_mask, "price_per_unit"] = df_cleaned.loc[ppu_mask, "total_spent"] / df_cleaned.loc[ppu_mask, "quantity"]

quantity_mask = df_cleaned["quantity"].isna() & df_cleaned["total_spent"].notna() & df_cleaned["price_per_unit"].notna() & (df_cleaned["price_per_unit"] != 0)
df_cleaned.loc[quantity_mask, "quantity"] = df_cleaned.loc[quantity_mask, "total_spent"] / df_cleaned.loc[quantity_mask, "price_per_unit"]

df_cleaned['payment_method'] = df_cleaned['payment_method'].fillna('UNKNOWN')
df_cleaned['payment_method'] = df_cleaned['payment_method'].replace('ERROR', 'UNKNOWN')

df_cleaned['location'] = df_cleaned['location'].replace(['ERROR', 'UNKNOWN', np.nan], 'Unknown')

# Convert 'transaction_date' column to datetime, coercing errors to NaT
df_cleaned['transaction_date'] = pd.to_datetime(df_cleaned['transaction_date'], errors='coerce')

df_cleaned = df_cleaned.dropna(subset=['transaction_date'])  # Drop rows with missing transaction_date
df_cleaned.dropna(subset=['quantity', 'price_per_unit', 'total_spent'], inplace=True)

df_cleaned.to_csv("cleaned_cafe_sales.csv", index=False)

print(df_cleaned.isna().sum())
