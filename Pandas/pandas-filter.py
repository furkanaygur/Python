import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 75).reshape(15, 5)
print(data)

df = pd.DataFrame(data, columns=["Column1", "Column2", "Column3", "Column4", "Column5"])
print(df)

columns = df.columns
print(columns)

# Top 5
result = df.head()
print(result)

# Top 10
result = df.head(10)
print(result)

# last 5
result = df.tail()
print(result)

# Column1's top 5
result = df["Column1"].head()
print(result)

result = df[5:15]["Column1"].head()
print(result)

result = df > 50
print(result)

result = df[df > 50]
print(result)

result2 = result[result % 2 == 0]
print(result2)

result = df[df["Column1"] > 50]["Column1"]
print(result)

# multi query
result = df[(df["Column2"] > 50) | (df["Column2"] % 2 == 0)]["Column2"]
print(result)

result = df[(df["Column2"] > 50) & (df["Column2"] % 2 == 0)]["Column2"]
print(result)
# <=====>
result = df.query("Column1 >= 50 & Column1 % 2 == 0")["Column2"]
print(result)


