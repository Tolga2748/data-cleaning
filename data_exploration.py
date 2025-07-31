import pandas as pd 

df = pd.read_csv("dirty_cafe_sales.csv")

# first 40 rows
print("first 40 rows")
print(df.head(40))
print()

# data info
print("data info")
print(df.info())
print()

# missing values
print("missing values")
print(df.isnull().sum())
print()

# column names
print("column names")
print(df.columns)



