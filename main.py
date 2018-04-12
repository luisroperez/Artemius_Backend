from flask import Flask
from config.dbconfig import client



app = Flask(__name__)
#mongo = PyMongo(app)

db = client.AutoAirGroupdb
for doc in db.orders.find():
    print(doc)



@app.route('/')
def test():
    return

if __name__ == '__main__':
    app.run(debug=True)
