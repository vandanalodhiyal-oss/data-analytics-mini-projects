import pandas as pd

#csv file read-----
df = pd.read_csv(r"C:\Users\Hp\Downloads\student-data-analysis - Sheet1.csv")
print(df.head())

# Total marks calculate-------
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)

# Percentage calculate---------
df["Percentage"] = df["Total"] / 3

# Grade assign function---------
def grade(p):
    if p >= 90:
        return "A"
    elif p >= 75:
        return "B"
    elif p >= 50:
        return "C"
    else:
        return "Fail"

df["Grade"] = df["Percentage"].apply(grade)

# Result assign--------
df["Result"] = df["Percentage"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print(df)