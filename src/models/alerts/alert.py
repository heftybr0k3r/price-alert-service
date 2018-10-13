import uuid
from datetime import datetime
from datetime import timedelta
import requests
import src.models.alerts.constants as AlertConstants
from src.common.database import Database
from src.models.items.item import Item


class Alert(object):
    def __init__ (self, user_email, price_limit,  item_id, active=True,  last_checked=None, _id=None):
        self.user_email = user_email
        self.price_limit = price_limit
        self.item = Item.get_by_id(item_id)
        self.last_checked = datetime.now() if last_checked is None else last_checked
        self._id = uuid.uuid4().hex if _id is None else _id
        self.active = active

    def __repr__(self):
        return "<Riasztás: {}, beállított ár: {} Ft.>".format(self.item.name,self.price_limit)

    def send(self):
        str = self.item.url
        return requests.post(
            AlertConstants.URL,
            auth=("api",AlertConstants.API_KEY),
            data={
                "from": AlertConstants.FROM,
                "to": self.user_email,
                "subject": "{} ára az általad beállítottra csökkent! ".format(self.item.name),
                "text": "Átirányítás a webshopba -> {} ".format(str, "http://pricing.herokuapp.com/alerts/{}".format(self._id))
            }
        )

    @classmethod
    def find_needing_update(cls, minutes_since_update=AlertConstants.ALERT_TIMEOUT):
        last_updated_limit = datetime.now() - timedelta(minutes=minutes_since_update)
        return [cls(**elem) for elem in Database.find(AlertConstants.COLLECTION,
                                                        {"last_checked":
                                                  {"$lte": last_updated_limit},
                                                         "active": True
                                                        })]

    def save_to_mongo(self):
            Database.update(AlertConstants.COLLECTION, {"_id": self._id}, self.json())

    def json(self):
        return {
        "_id": self._id,
        "price_limit": self.price_limit,
        "last_checked": self.last_checked,
        "user_email": self.user_email, # csak mailjét használjuk
        "item_id": self.item._id, # _ = protected member
        "active": self.active
        }

    def load_item_price(self):
        str = self.item.load_price()
        print(str)
        if str.find(" ")!=-1:
            str = str.replace(" ",".")
        elif str.find(",")!=-1:
            str = str.replace(",",".")
        elif str.find(u'\xa0')!=-1:
            str = str.replace(u'\xa0',".")
        self.item.price = float(str)
        # self.last_checked = datetime.now()
        self.item.save_to_mongo()
        self.save_to_mongo()
        return self.item.price


    def load_item_price_for_alert_edit(self):
        str = self.item.load_price()
        print(str)
        if str.find(" ")!=-1:
            str = str.replace(" ",".")
        elif str.find(",")!=-1:
            str = str.replace(",",".")
        elif str.find(u'\xa0')!=-1:
            str = str.replace(u'\xa0',".")
        self.item.price = float(str)
        self.last_checked = datetime.now()
        self.save_to_mongo()
        print(self.item.price)
        self.send_email_if_price_reached()
        return self.item.price

    def price_for_alertshow(self):
        price = self.load_item_price()
        price = price * 1000
        price = int(price)
        return "{} Ft.".format(price)

    def send_email_if_price_reached(self):
        print("self item in float: {}".format(self.item.price))
        if self.item.price < float(self.price_limit):
            print(self.user_email)
            self.send()
            print("Elküldve")

    @classmethod
    def find_by_user_email(cls, user_email):
        return [cls(**elem) for elem in Database.find(AlertConstants.COLLECTION, {"user_email": user_email})]

    @classmethod
    def find_by_id (cls, alert_id):
        return cls(**Database.find_one(AlertConstants.COLLECTION, {"_id": alert_id}))

    def deactivate(self):
        self.active = False
        self.save_to_mongo()

    def activate(self):
        self.active = True
        self.save_to_mongo()

    def delete(self):
        Database.remove(AlertConstants.COLLECTION, {"_id": self._id})