from flask import Blueprint

items_blueprint = Blueprint('alerts',__name__)

@items_blueprint.route('/item/<string:name>')
def item_page(name):
    pass

@items_blueprint.route('/load')
def load_item():
    """
    Load an alerts data using their store and return json representation of it.
    :return:
    """
    pass

