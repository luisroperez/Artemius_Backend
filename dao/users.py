from config.dbconfig import client
import json


class UsersDao:

    def __init__(self):
        self.db = client.AutoAirGroupdb.user_account

    def getAllUsers(self):
        users = self.db
        for doc in users.find():
            print(doc)
        print("test")

    def insertUser(self):
        address = [
            {
                'city:' "Guaynabo",
                'place:' "Villa Avila",
                'street' "A-29 Humacao",
                'zipcode' "00969"
            }
        ]

        newUser = [
            'user_fname:' "Jaime",
            'user_lname:' "Cortes",
            'username:' "jcd1",
            'usertype:' "admin",
            'user_email:' "jaime.cortes@gmail.com",
            'user_password:' "jcd123",
            'user_address:', json.dumps(address),
            'user_phone:' '7875555555'
        ]
        print("Okay")
