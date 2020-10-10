import pandas as pd

df = pd.read_csv("imdb.csv")

result = df.columns
print(result)

result = df.info
print(result)

# Top5
result = df.head()
print(result)

# Top 10
result = df.head(10)
print(result)

# Last 5
result = df.tail()
print(result)

# Last 10
result = df.tail(10)
print(result)

result = df[5:][["Movie_Title", "Rating"]].head(7)
print(result)

result = df[["Movie_Title", "Rating"]].query("Rating >= 8.0").head(50)
print(result)

result = df.query("YR_Released >= 2014 & YR_Released <= 2015")[["Movie_Title", "YR_Released"]].head()
print(result)

result = df.query("Num_Reviews >= 100000 | (Rating >= 8 & Rating <= 9)")[
    ["Movie_Title", "Rating", "Num_Reviews"]].head(10)
print(result)
