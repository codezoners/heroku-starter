from flask import Flask, request, render_template, jsonify, redirect
from flask_cors import CORS
import urllib.parse
import datetime
import os
import pymongo

ON_HEROKU = "ON_HEROKU" in os.environ

user = os.environ["DB_USER"]
password = os.environ["DB_PASS"]

# Local database:
#CONNECTION="mongodb://localhost:27017/"

# MongoDB Atlas:
CONNECTION=\
    "mongodb+srv://%s:%s@cluster0-ay0js.mongodb.net/test?retryWrites=true&w=majority" \
    % (user, password)

print(CONNECTION)

myclient = pymongo.MongoClient(CONNECTION, connect=False)
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

app = Flask(__name__, static_url_path='', static_folder="static")
CORS(app)

@app.route('/')
def index():
    print(mycol.find_one())
    return render_template('index.html', data=mycol.find())
    #return render_template('index.html', data=[])

if (not ON_HEROKU) and __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
