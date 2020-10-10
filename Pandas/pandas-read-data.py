import pandas as pd
import sqlite3

# df = pd.read_csv('sample.csv')
# print(df)

# df = pd.read_json('sample.json')
# print(df)

# df = pd.read_excel('sample.xlsx')
# print(df)


connection = sqlite3.connect("sample.db")
df = pd.read_sql_query("SELECT * FROM students", connection)
print(df)
