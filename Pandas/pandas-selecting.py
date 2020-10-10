import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3, 3), index=["A", "B", "C"], columns=["Column1", "Column2", "Column3"])
print(df)

result = df["Column1"]
print(result)

result = df[["Column1", "Column2"]]
print(result)

# loc["row", "column"] => loc[:, "column"]
result = df.loc["A"]
print(result)

result = df.loc[:, "Column2"]
print(result)

result = df.loc[:, "Column1":"Column3"]
print(result)

result = df.loc["A":"C", :"Column3"]
print(result)

# index number
result = df.iloc[1]
print(result)

result = df.loc["B", "Column2"]
print(result)

# Add
df["Column4"] = pd.Series(randn(3), ["A", "B", "C"])
print(df)

df["Column5"] = df["Column1"] + df["Column2"]
print(df)

# Delete
print(df.drop("Column5", axis=1))
print(df)

df.drop("Column5", axis=1, inplace=True)
print(df)
