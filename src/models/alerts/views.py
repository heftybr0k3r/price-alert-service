from flask import Blueprint, render_template, session, request, url_for, redirect
from src.models.alerts.alert import Alert
from src.models.items.item import Item
import requests
import src.models.users.decorators as user_decorators

__author__ = "Zexx"

alert_blueprint = Blueprint('alerts',__name__)

@alert_blueprint.route('/')
def index():
    return "This is the alert page."

@alert_blueprint.route('/new', methods=['GET','POST'])
@user_decorators.require_login # decorator
def create_alert():
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        price_limit = request.form['price_limit']
        item=Item(name, url)
        item.save_to_mongo()

        alert = Alert(session['email'],price_limit,item._id)
        alert.load_item_price()

    return render_template('alerts/new_alert.jinja2')

@alert_blueprint.route('/edit/<string:alert_id>', methods=['GET','POST'])
@user_decorators.require_login # decorator
def edit_alert(alert_id):
    alert = Alert.find_by_id(alert_id)
    if request.method == 'POST':
        price_limit = request.form['price_limit']
        alert.price_limit = price_limit
        alert.save_to_mongo()
        return redirect(url_for('users.user_alerts'))

    return render_template('alerts/edit_alert.jinja2', alert = alert)

# Setting up the route to deactivate alert
@alert_blueprint.route('/deactivate/<string:alert_id>')
@user_decorators.require_login
def deactivate_alert(alert_id):
    Alert.find_by_id(alert_id).deactivate()
    return redirect(url_for('users.user_alerts'))

# Setting up the route to delete alert
@alert_blueprint.route('/delete/<string:alert_id>')
@user_decorators.require_login
def delete_alert(alert_id):
    Alert.find_by_id(alert_id).delete()
    return redirect(url_for('users.user_alerts'))

# Setting up the route to activate alert
@alert_blueprint.route('/activate/<string:alert_id>')
@user_decorators.require_login
def activate_alert(alert_id):
    Alert.find_by_id(alert_id).activate()
    return redirect(url_for('users.user_alerts'))

# Setting up the base site route
@alert_blueprint.route('/<string:alert_id>')
def get_alert_page(alert_id):
    alert = Alert.find_by_id(alert_id)
    return render_template('alerts/alert.jinja2', alert=alert)

@alert_blueprint.route('/for_user/<string:user_id>')
@user_decorators.require_login # decorator
def get_alerts_for_user(user_id):
    pass

# Scraping the price for the given item
@alert_blueprint.route('/check_price/<string:alert_id>') # alert_idt paraméterként adjuk ki
def check_alert_price(alert_id):
    Alert.find_by_id(alert_id).load_item_price_for_alert_edit()
    return redirect(url_for('.get_alert_page', alert_id=alert_id))
