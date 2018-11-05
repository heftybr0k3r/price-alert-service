import uuid

__author__ = "Zexx"

from bs4 import BeautifulSoup
import requests
import re
import src.models.items.constants as ItemConstants
from src.common.database import Database
from src.models.stores.store import Store


class Item(object):
	# Constructor
    def __init__(self, name, url, price=None, _id=None):
        self.name = name
        self.url = url
        store = Store.find_by_url(url)
        self.tag_name = store.tag_name
        self.query = store.query
        self.price = None if price is None else price
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<{}, URL-je: {}.>".format(self.name, self.url)
	
	# Loading prices, scraping given webiste with request && BeautifulSoup
    def load_price (self):
        request = requests.get(self.url)
        print(self.url)
        content = request.content
        print(content)
        soup = BeautifulSoup(content, "html.parser")
        print(self.tag_name)
        print(self.query)
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()
        # if (string_price.find(',') == -1):
        string_price.replace(",",".")
        pattern = re.compile("(\d+.\d+)")
        str = string_price.replace(",",".")
        match = pattern.search(str)
        self.price = (match.group())

        return self.price

	# Saving to MongoDB
    def save_to_mongo(self):
        # insert json of the object
        Database.update(ItemConstants.COLLECTION, {"_id": self._id}, self.json())

    def json(self):
        return {
        "_id": self._id,
        "name": self.name,
        "url": self.url,
        "price": self.price
         }
    # cls - class method

    @classmethod
    def get_by_id(cls, item_id):
        return cls(**Database.find_one(ItemConstants.COLLECTION, {"_id": item_id}))