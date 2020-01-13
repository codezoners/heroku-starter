import pymongo
import os

# Local database:
#CONNECTION="mongodb://localhost:27017/"

# MongoDB Atlas:
user = os.environ["DB_USER"]
password = os.environ["DB_PASS"]

CONNECTION=\
    "mongodb+srv://%s:%s@cluster0-ay0js.mongodb.net/test?retryWrites=true&w=majority&connect=false" \
    % (user, password)

myclient = pymongo.MongoClient(CONNECTION)

<<<<<<< HEAD
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient("mongodb://tfmp_user:Freedom34@ds263248.mlab.com:63248/tfmp?retryWrites=false")
=======
>>>>>>> c815040e76d82c854bb8cc22d9f541a9a08a9896
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = { "name": "Jim", "address": "Highway 999" }

# Add some data:
x = mycol.insert_one(mydict)

# Retrieve some data:
for x in mycol.find():
    print(x)
