from flask import Blueprint

__author__ = "Zexx"

items_blueprint = Blueprint('alerts',__name__)

# Setting up the item route
@items_blueprint.route('/item/<string:name>')
def item_page(name):
    pass

# Loading item
@items_blueprint.route('/load')
def load_item():
    """
    Load an alerts data using their store and return json representation of it.
    :return:
    """
    pass

