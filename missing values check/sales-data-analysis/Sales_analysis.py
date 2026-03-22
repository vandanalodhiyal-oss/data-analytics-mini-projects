import pandas as pd

df = pd.read_csv(r"C:\Users\Hp\Downloads\Sales_data.csv - Sheet1 (1).csv")
print(df)
print()
print(df.head())           #5 row----Display
print()
print(df.columns)          # all Column names
print()
print(df.info())           #data types each colum
print()
print(df.shape)            #Total number records
print()

#--Data cleaning---
df["Date"]= pd.to_datetime(df['Date'])
print(df["Date"])
print()
print(df.isnull().sum())             #check missing values
print()
df.rename(columns={'Price':'UnitPrice'},inplace=True)            #rename-----price to unitprice
print(df.head())
print()

#Data Transfomation---
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
print(df.head())
print()

#Data Analysis-----
print("Total Sales",df['TotalAmount'].sum())             #Total sales
print()
print("Average order value:",df['TotalAmount'].mean())      
print()
print(df.groupby('City')['TotalAmount'].sum())        #citywise sales
print()
print(df.groupby('Category')['TotalAmount'].sum())    #Categorywise sales
print()
print(df.groupby('Product')['TotalAmount'].sum().idxmax())  #top salling product
print()

#Filtering and sorting----
delhi_orders = df[df['City']=="Delhi"]      
print(delhi_orders)
print()

high_orders= df[df['TotalAmount'] >30000]       #TotalAmount>30000  (condition based)
print(high_orders)
print()

sorted_data = df.sort_values('TotalAmount' , ascending=False)      #high to low (Desending)
print(sorted_data)
print()

top3 = df.sort_values('TotalAmount',ascending=False).head(3)        #top 3 highest value order
print(top3)
