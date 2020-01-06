from flask import Flask, request, render_template, jsonify, redirect
import urllib.parse
import datetime
import os
import pymongo

ON_HEROKU = "ON_HEROKU" in os.environ

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

app = Flask(__name__, static_url_path='', static_folder="static")

@app.route('/')
def index():
    print(mycol.find_one())
    return render_template('index.html', data=mycol.find())

if (not ON_HEROKU) and __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
