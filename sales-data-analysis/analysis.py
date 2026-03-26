import pandas as pd

# csv file load------
df = pd.read_csv(r"C:\Users\Hp\Downloads\Sales data analysis - sales data (1).csv")
print(df.head())

# missing values check
print("\nMissing values:\n")
print(df.isnull().sum())

# missing values average se fill----
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())

# duplicate rows remove------
df = df.drop_duplicates()

# text clean------
df["Name"] = df["Name"].str.strip()
df["City"] = df["City"].str.strip()
df["Product"] = df["Product"].str.strip()

# sales column-----
df["Sales"] = df["Quantity"] * df["Price"]

# total sales
print("\nTotal Sales:")
print(df["Sales"].sum())

# city wise sales------
print("\nCity wise sales:")
print(df.groupby("City")["Sales"].sum())

# category wise sales------
print("\nCategory wise sales:")
print(df.groupby("Category")["Sales"].sum())

# top product------
print("\nTop product:")
print(df.groupby("Product")["Sales"].sum().idxmax())
print("\nFinal Cleaned Data:\n")
print(df.to_string())