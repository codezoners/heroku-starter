from flask import Flask, request, render_template, jsonify, redirect
import urllib.parse
import datetime
import os

ON_HEROKU = "ON_HEROKU" in os.environ

app = Flask(__name__, static_url_path='', static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

if (not ON_HEROKU) and __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
