import pymongo

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient("mongodb://tfmp_user:Freedom34@ds263248.mlab.com:63248/tfmp?retryWrites=false")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = { "name": "Jim", "address": "Highway 999" }

# Add some data:
x = mycol.insert_one(mydict)

# Retrieve some data:
for x in mycol.find():
    print(x)
