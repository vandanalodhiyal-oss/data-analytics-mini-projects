import numpy as np
import pandas as pd

#data loding csv file--------
df = pd.read_csv(r"C:\Users\Hp\Downloads\Student class marks analysis - Sheet1.csv")
print(df)
print(df.head())           
print(df.columns)          
print(df.info())           #data types each colum
print(df.shape)            #Total number records ------row , columns
print()

#check missing value-----
print(df.isnull())
print(df.isnull().sum())

# Average se missing value fill-----
for col in ["Hindi", "English", "Physics" , "Biology" , "Chemistry"]:
    mean_value = df[col].mean()                             # Average calculate
    df[col] = df[col].fillna(mean_value)                # Fill missing value
print(f"{col} → Average: {mean_value} | Missing values filled with: {mean_value}")
print()

#Total marks calculate-----
df["Total"] = df["Hindi"] + df["English"] + df["Physics"] + df["Biology"] + df["Chemistry"]
print(df[["Name" , "Total"]])
print()

# Top student----
top_total = df["Total"].max()
df['Top Student'] = df["Total"] == top_total
df["Top Student"] = df["Top Student"].replace({True:"Yes" , False:""})
print(df[["Name" , "Total" , "Top Student"]])

#Percentage-----
max_marks = 500
df["Percentage"] = (df["Total"] / max_marks) * 100
df["Percentage"]=df["Percentage"]
print(df[["Name" , "Total" , "Percentage"]])
print(df)