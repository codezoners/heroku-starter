import pymongo
import os

# Local database:
#CONNECTION="mongodb://localhost:27017/"

# MongoDB Atlas:
user = os.environ["DB_USER"]
password = os.environ["DB_PASS"]

CONNECTION=\
    "mongodb+srv://%s:%s@cluster0-ay0js.mongodb.net/test?retryWrites=true&w=majority" \
    % (user, password)

myclient = pymongo.MongoClient(CONNECTION)

mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = { "name": "Jim", "address": "Highway 999" }

# Add some data:
x = mycol.insert_one(mydict)

# Retrieve some data:
for x in mycol.find():
    print(x)
