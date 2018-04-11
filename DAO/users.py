from config.dbconfig import client

class UsersDao:

    def __init__(self):
        db = client.users_accounts

    def getAllUsers(self):

        print("test")