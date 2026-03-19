import pandas as pd

data = {
    "Employee_ID": [101,102,103,104,105],
    "Name": ["Vandana", "Mohit" , "Sikha" , "Vani" , "Rohan"],
    "Department": ["HR", "IT" , "HR" , "IT" , "Finance"],
    "Salary" : [50000 , 30000 , 45000 , 55000 , 60000],
}
df = pd.DataFrame(data)
print(df)
print("Average Salary:",df["Salary"].mean())      #Average Salary
print("Highest Salary:",df["Salary"].max())       #max Salary
print("Lowest Salary:",df["Salary"].min())       #min Salary

#filter data---Employee with salary>50000
high_salary = df[df["Salary"]>50000]
print(high_salary)

it_employee = df[df["Department"]=="HR"]        #employee in HR department
print(it_employee)

#Add column----Bonus 10% of salary
df["Bonus"] = df["Salary"] * 0.1
print(df)





