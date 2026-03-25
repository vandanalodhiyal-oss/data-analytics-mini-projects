import pandas as pd

# Load CSV file------
df = pd.read_csv(r"C:\Users\Hp\Downloads\data cleaning project - Sheet1 (1).csv")
print("Original Data:\n")
print(df)

# Duplicate  remove-----
df.drop_duplicates(subset = ['Name'] , keep='first' , inplace = True)

# Missing values check
print("\nMissing Values:\n")
print(df.isnull().sum())

# Fill missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Subjects list
subjects = ['HINDI','ENGLISH','MATHS','SCIENCE','SST','DRAWING']

# Total
df['Total'] = df[subjects].sum(axis=1)

# Average
df['Average'] = df['Total'] / 6

# Grade
def grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"

df['Grade'] = df['Average'].apply(grade)

# Max & Min
df['Max Marks'] = df[subjects].max(axis=1)
df['Min Marks'] = df[subjects].min(axis=1)

print("\nProcessed Data:\n")
print(df)

# Save new CSV
df.to_csv("final_students.csv", index=False)
print("\nNew file saved as final_students.csv")