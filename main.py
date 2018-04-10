from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo
import certifi
import ssl
from pymongo import MongoClient




app = Flask(__name__)

client = MongoClient('mongodb://devUser:AAG2018@cluster0-tomfu.mongodb.net:27017/AutoAirGroupdb',ssl_cert_reqs=ssl.CERT_REQUIRED, ssl_ca_certs=certifi.where())

print(client.mflix)



@app.route('/')
def test():
    return

if __name__ == '__main__':
    app.run(debug=True)
