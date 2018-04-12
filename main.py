from flask import jsonify
from flask import Flask
from flask_pymongo import PyMongo
import pymongo
import certifi
import ssl
from config.config import client
from pymongo import MongoClient



app = Flask(__name__)
mongo = PyMongo(app)

db = client.AutoAirGroupdb
for doc in db.orders.find():
    print(doc)



@app.route('/')
def test():
    return

if __name__ == '__main__':
    app.run(debug=True)
