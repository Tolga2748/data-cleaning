import pandas as pd 

df = pd.read_csv("dirty_cafe_sales.csv")

#ilk 5 satır
print("ilk 5 satır")
print(df.head(40))
print()

# verinin bilgileri
print("verinin bilgileri")
print(df.info())
print()

#eksisk veriler
print("eksisk veriler")
print(df.isnull().sum())
print()

#sütün isimleri
print("sütün isimleri")
print(df.columns)

""" df_cleaned = df.dropna(subset=["quantity", "price_per_unit", "total_spent"])

print("Temizlendikten sonra eksik değer sayısı:")
print(df_cleaned.isna().sum())
print("Orijinal satır sayısı:", len(df))
print("Temizlenmiş satır sayısı:", len(df_cleaned))
 """