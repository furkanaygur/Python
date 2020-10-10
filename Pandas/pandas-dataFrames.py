import pandas as pd

s1 = pd.Series([3, 2, 0, 1])
s2 = pd.Series([0, 3, 7, 2])

data = dict(apples=s1, oranges=2)
df = pd.DataFrame(data)
print(df)
# *********************************************
data = [["Furkan", 22], ["Furkan", 18], ["Furkan", 20]]
df = pd.DataFrame(data, columns=['Name', 'Age'], index=[1, 2, 3], dtype=float)
print(df)
# *********************************************
dict = {"Name": ["Furkan", "Furkan", "Furkan"], "Age": [22, 20, 18]}
df = pd.DataFrame(dict, index=[1, 2, 3])
print(df)
# *********************************************
dict_list = [
    {"Name": "Furkan", "Age": 22},
    {"Name": "Furkan", "Age": 20},
    {"Name": "Furkan", "Age": 18}
]

df = pd.DataFrame(dict_list, index=[1, 2, 3])
# *********************************************
