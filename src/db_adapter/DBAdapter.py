from pymongo import MongoClient


class DBAdapter:
    def __init__(self):
        mongo_client = MongoClient("localhost", 27117, username="someUser", password="somePwd")
        self.db = mongo_client.DVDRentals
