import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 15).reshape(5, 3)

df = pd.DataFrame(data, index=['a', 'c', 'e', 'f', 'h'], columns=["Column1", "Column2", "Column3"])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)
# ************************************
newColumn = [np.nan, 30, np.nan, 51, np.nan, 30, np.nan, 10]
df["Column4"] = newColumn
print(df)
# ************************************
result = df.drop("b", axis=0)
print(result)
# ************************************
result = df.isnull()
print(result)
# ************************************
result = df.notnull()
print(result)
# ************************************
result = df["Column1"].isnull().sum()
print(result)
# ************************************
result = df[["Column1", "Column4"]][df["Column1"].isnull()]
print(result)
# ************************************
result = df.dropna()  # axis = 0
print(result)
result = df.dropna(axis=1)
print(result)
# ************************************
result = df.dropna(how="all")
print(result)
# ************************************
result = df[["Column1", "Column2"]].dropna(subset=["Column1", "Column2"])
print(result)
# ************************************
result = df.dropna(thresh=3)
print(result)
# ************************************
result = df.fillna(value='No input')
print(result)


# ************************************
def avg(df):
    total = df.sum().sum()
    piece = df.size - df.isnull().sum().sum()
    return total / piece


result = df.fillna(value=avg(df))
print(result)
# ************************************
