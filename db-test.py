import pymongo
import os

user = os.environ["DB_USER"]
password = os.environ["DB_PASS"]
database = os.environ["DB_NAME"]

# Local database:
#CONNECTION="mongodb://localhost:27017/"

# MongoDB Atlas:

CONNECTION_ATLAS=\
    "mongodb+srv://%s:%s@cluster0-ay0js.mongodb.net/%s?retryWrites=true&w=majority&connect=false" \
    % (user, password, database)

CONNECTION=CONNECTION_ATLAS
myclient = pymongo.MongoClient(CONNECTION)

mydb = myclient[database]
mycol = mydb["customers"]
mydict = { "name": "Jim", "address": "Highway 999" }

# Add some data:
x = mycol.insert_one(mydict)

# Retrieve some data:
for x in mycol.find():
    print(x)
