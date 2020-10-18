import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")
# myclient = pymongo.MongoClient("mongodb+srv://furkanaygur:<yourpassword>@cluster0.98ggn.mongodb.net/<yourdatabasename>?retryWrites=true&w=majority")

mydb = myclient["node-app"]

mycollection = mydb["products"]

# # INSERT

# product = {"name":"Iphone 12", "price":1400}

# insert = mycollection.insert_one(product)

# print(insert.inserted_id)

# productList = [
#     {"name":"Iphone 12", "price":1400, "description":"last version"},
#     {"name":"Iphone 11", "price":999, "categories":['phone','electronic']}
 
# ]

# insert = mycollection.insert_many(productList)
# for i in insert.inserted_ids:
#     print(i)

# # SELECT with filter
# result= mycollection.find_one()
# print(result)


# for i in mycollection.find({"name":"Iphone"},{"_id":0}):
#     print(i)


# result = mycollection.find_one({"_id": ObjectId("5f8c98ed89999d2bd59e4df6")})
# print(result)

# # with operators
# result = mycollection.find({
#     "name": {
#         "$in": ["Iphone 10","Iphone 5s"]
#     }
# })

# for i in result:
#     print(i)

# result = mycollection.find({
#     "price": {
            # $gt, $lt, $lte
#         "$gte": 500
#     }
# })

# for i in result:
#     print(i)

# result = mycollection.find({
#     "price": {
#         "$eq": 999
#     }
# })

# for i in result:
#     print(i)

# # Sorting
# result = mycollection.find({
#     "name": {
#         "$regex": "^I"
#     }
# }).sort([("price",-1),("name",1)]) # 1 = increasing, -1 = descending

# for i in result:
#     print(i)


# # Update
# result = mycollection.update_many(
#     {"name":"Iphone 8"},
#     {"$set": {
#         "name":"Iphone 9",
#         "price": 600
#     }}
# )

# for i in mycollection.find():
#     print(i)

# print(f"{result.modified_count} updated")

# # Delete
result = mycollection.delete_many({"name":"Iphone 9"})

for i in mycollection.find():
    print(i)

print(f"{result.deleted_count} deleted")