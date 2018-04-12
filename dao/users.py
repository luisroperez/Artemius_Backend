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
                'city:' "Rincon",
                'place:' "Urb Esteves",
                'street' "Calle Cipreses",
                'zipcode' "00969"
            }
        ]

        newUser = [
            'user_fname:' "Juan",
            'user_lname:' "DelPueblo",
            'username:' "jdp",
            'usertype:' "admin",
            'user_email:' "jdp@gmail.com",
            'user_password:' "jdp123",
            #'user_address:', json.dumps(address),
            'user_phone:' '7875555555'
        ]
        self.db.insert_once(newUser)
        print("Okay")
