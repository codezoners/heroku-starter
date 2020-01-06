import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = { "name": "Jim", "address": "Highway 999" }

# Add some data:
x = mycol.insert_one(mydict)

# Retrieve some data:
for x in mycol.find():
    print(x)
