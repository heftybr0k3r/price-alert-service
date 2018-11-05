
__author__ = "Zexx"

import uuid
from bs4 import BeautifulSoup
import requests

from src.common.database import Database
import src.models.stores.constants as StoreConstants
import src.models.stores.errors as StoreErrors


class Store(object):
	
	# Constructor
    def __init__(self, name, url_prefix, tag_name, query, _id=None):
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Webáruház: {}>".format(self.name)

    @classmethod
    def get_by_id(cls, id):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"_id": id}))

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }

    def save_to_mongo(self):
        Database.update(StoreConstants.COLLECTION, {"_id": self._id}, self.json())

		
	# Get Store by name
    @classmethod
    def get_by_name(cls, store_name):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"name": store_name}))

	# Get Store by url_prefix
    @classmethod
    def get_by_url_prefix(cls, url_prefix):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"url_prefix": {"$regex": '^{}'.format(url_prefix)}}))

    @classmethod
    def find_by_url(cls, url):
        # return a store from the given url
        for i in range(0, len(url) + 1):
            try:
                if url.find("mall") != -1:
                    print(url.find("mall"))
                    store = cls.get_by_url_prefix("https://www.mall")
                elif url.find("xiaomi") != -1:
                    print(url.find("xiaomi"))
                    store = cls.get_by_url_prefix("http://xiaomishop")
                elif url.find("edigital") != -1:
                    request = requests.get(url)
                    content = request.content
                    soup = BeautifulSoup(content, "html.parser")
                    tag = ""
                    query = ""
                    if soup.title.string.find("Extreme") != -1:
                        if soup.find("strong", "price price--large price--discount") is not None:
                            tag = "strong"
                            query = {"class": "price price--large price--discount"}
                        elif (soup.find("strong", "price price--large ")) is not None:
                            tag = "strong"
                            query = {"class": "price price--large "}
                    store = cls.get_by_url_prefix("https://edigital")
                    store.query = query
                    store.tag_name = tag
                elif url.find("ipon") != -1:
                    print(url.find("xiaomi"))
                    store = cls.get_by_url_prefix("https://ipon")
                elif url.find("emag") != -1:
                    request = requests.get(url)
                    content = request.content
                    soup = BeautifulSoup(content, "html.parser")
                    tag = ""
                    query = ""
                    if soup.title.string.find("eMAG.hu") != -1:  # eMAG
                        if soup.find("p", "product-old-price") is not None:
                            tag = "p"
                            query = {"class": "product-new-price"}
                        else:
                            tag = "p"
                            query = {"class": "product-old-price"}
                    store = cls.get_by_url_prefix("https://www.emag")
                    store.query = query
                    store.tag_name = tag
                return store
            except:
                raise StoreErrors.StoreNotFoundException("A keresett prefix alapján a bolt nem található!")
                # pass # do nothing

    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find(StoreConstants.COLLECTION, {})]

	# Self explanatory
    def delete(self):
        Database.remove(StoreConstants.COLLECTION, {'_id': self._id})