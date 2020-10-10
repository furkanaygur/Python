import pandas as pd

Students = {
    'Name': ['Furkan', 'Furkan', 'Furkan', 'Furkan'],
    'Branch': ['Software Engineering', 'Computer Engineering', 'Computer Programing', 'Software Engineering'],
    'Age': [22, 20, 18, 23],
    'Province': ['Istanbul', 'Ankara', 'Izmır', 'Elazıg'],
    'Year': [2020, 2022, 2018, 2022]
}

df = pd.DataFrame(Students)
print(df)

age = df['Age'].sum()
print(age)
# ********************************************
result = df.groupby(['Branch', 'Name']).groups
print(result)

# ********************************************
for name, group in df.groupby("Branch"):
    print(name)
    print(group)
# ********************************************
result = df.groupby("Branch").get_group("Software Engineering")
# ********************************************
result = df.groupby("Branch").mean()
print(result)
# ********************************************
result = df.groupby("Branch")["Age"].mean()
print(result)
# ********************************************
result = df.groupby("Branch")["Name"].count()
print(result)
# ********************************************
result = df.groupby("Branch")["Age"].max()["Software Engineering"]
print(result)

# ********************************************
import numpy as np

result = df.groupby("Branch")["Age"].agg([np.sum, np.mean, np.max, np.min]).loc["Software Engineering"]
print(result)
