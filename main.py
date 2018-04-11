from flask import jsonify
from flask import Flask
from flask_pymongo import PyMongo
import pymongo
import certifi
import ssl
from pymongo import MongoClient





app = Flask(__name__)
mongo = PyMongo(app)

client = pymongo.MongoClient('mongodb+srv://devUser:AAG2018@cluster0-tomfu.mongodb.net/AutoAirGroupdb',ssl_cert_reqs=ssl.CERT_REQUIRED, ssl_ca_certs=certifi.where())

print(client.AutoAirGroupdb)



@app.route('/')
def test():
    return

if __name__ == '__main__':
    app.run(debug=True)
