import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
# myclient = pymongo.MongoClient("mongodb+srv://furkanaygur:<yourpassword>@cluster0.98ggn.mongodb.net/<yourdatabasename>?retryWrites=true&w=majority")

mydb = myclient["node-app"]

print(myclient.list_database_names())