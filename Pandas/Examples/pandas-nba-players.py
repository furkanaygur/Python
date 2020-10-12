import pandas as pd

df = pd.read_csv('nba.csv')

result = df.head(10)
print(result)
# *************************************
result = len(df.index)
print(result)
# *************************************
result = df["Salary"].mean()
print(result)
# *************************************
result = df["Salary"].max()
print(result)
# *************************************
result = df[df["Salary"] == df["Salary"].max()]["Name"].iloc[0]
print(result)
# *************************************
result = df[(df["Age"] >= 20) & (df["Age"] <= 25)][["Name", "Team", "Age"]].sort_values("Age")
print(result)
# *************************************
result = df[df["Name"] == "John Holland"]["Team"].iloc[0]
print(result)
# *************************************
result = df.groupby("Team").mean()["Salary"]
print(result)
# *************************************
result = len(df.groupby("Team"))
print(result)
# *************************************
result = df["Team"].value_counts()
print(result)
# *************************************
df = df.dropna()
result = df[df["Name"].str.contains("and")].head()
print(result)


# <======>

def str_find(name):
    if 'and' in name.lower():
        return True
    return False


result = df[df["Name"].apply(str_find)].head()
print(result)

# *************************************
