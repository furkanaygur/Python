import pandas as pd 

df = pd.read_csv('C:/Users/furka/Desktop/youtube-ing.csv')

result = df.head(10)
print(result)

result = df[5:].head(5)
print(result)

result = len(df.columns)
print(result)

df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"], axis=1 , inplace=True)
print(df)

result = df["likes"].mean()
print(result)

result = df["dislikes"].mean()
print(result)

result = df.head(50)[["title","likes","dislikes"]]
print(result)

result = df[ df["views"] == (df["views"].max())]["title"].iloc[0]
print(result)


result = df[ df["views"] == (df["views"].min())]["title"].iloc[0]
print(result)


result = df.sort_values("views", ascending= False)[["title","views"]].head(10)
print(result)

result = df.groupby("category_id").mean().sort_values("likes")["likes"]
print(result)

result = df.groupby("category_id").sum().sort_values("comment_count", ascending= False)["comment_count"]
print(result)

result = df["category_id"].value_counts()
print(result)

df["title_len"] = df["title"].apply(len)
print(df)

df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))
print(df)


def Calc_Likes_Dislikes(dataset):  
    likesList = list(df["likes"])
    dislikesList = list(df["dislikes"])
    List = list(zip(likesList,dislikesList))
    rateList = []
    for like, dislike in List:
        if (like+dislike) == 0:
            rateList.append(0)
        else:
            rateList.append(like/(like+dislike)),
    
    return rateList

df["rate"] =Calc_Likes_Dislikes(df)
print(df.sort_values("rate", ascending = False)[["title","likes","dislikes","rate"]])
