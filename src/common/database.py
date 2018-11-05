import pymongo
import os


class Database(object):
    URL = os.environ.get("MONGOLAB_ROSE_URI")
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URL)
        Database.DATABASE = client[os.environ.get("DBNAME")]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find (collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True )

    @staticmethod
    def remove(collection, query):
        Database.DATABASE[collection].remove(query)
