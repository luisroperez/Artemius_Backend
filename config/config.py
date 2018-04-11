import pymongo
import certifi
import ssl
x=1

client = pymongo.MongoClient('mongodb+srv://devUser:AAG2018@cluster0-tomfu.mongodb.net/AutoAirGroupdb',ssl_cert_reqs=ssl.CERT_REQUIRED, ssl_ca_certs=certifi.where())

