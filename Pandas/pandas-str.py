import pandas as pd

data = pd.read_csv('nba.csv')
data.dropna(inplace=True)
print(data)

print(data.columns)
# ******************************************
result = data["Name"].str.upper().head()
print(result)
# ******************************************
result = data["Name"].str.lower().head()
print(result)
# ******************************************
data["index"] = data["Name"].str.find('a')
result = data[["Name", "index"]].head()
print(result)
# ******************************************
data = data[data["Name"].str.contains('Jordan')]
print(data)
# ******************************************
# data = data["Team"].str.replace(' ', '-')
# print(data)
# ******************************************
data[["FirstName", "LastName"]] = data["Name"].loc[data['Name'].str.split().str.len() == 2].str.split(expand=True)
print(data[["Name", "FirstName", "LastName"]].head())
