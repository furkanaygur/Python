import pandas as pd
import numpy as np

data = {
    "Column1" : [1,2,3,4,5],
    "Column2" : [10,10,30,40,50],
    "Column3" : ['abc','def','ghi','jkl','mno']
}


df = pd.DataFrame(data)
print(df)

result = df["Column2"].unique()
print(result)

result = df["Column2"].nunique()
print(result)

result = df["Column2"].value_counts()
print(result)

result = df["Column1"] * 2
print(result) 

# ********************************

def square(x):
    return x * x

result = df["Column1"].apply(square)
print(result)

result = df["Column1"].apply(lambda x: x * x)
print(result)

result =  df["Column3"].apply(len)
print(result)

result = df.sort_values("Column3", ascending=False)
print(result)

# ***************************************************

data = {
    'Months' : ['May','Jun','Feb','Apr','Mar','Feb','Feb','Jun'],
    'Categories' : ['Electronic','Electronic','Electronic','Book','Book','Electronic','Book','Book'],
    'Gain' : [20,30,15,14,32,42,12,75]
}

df = pd.DataFrame(data)
print(df)

print(df.pivot_table(index="Months", columns="Categories", values="Gain"))
