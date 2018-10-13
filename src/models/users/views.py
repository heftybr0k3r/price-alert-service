from flask import Blueprint, request, session, redirect, url_for, render_template  # sablonok létrehozásához
import src.models.users.errors as UserErrors

# view az API endpointja blueprinteket használunk hozzá
from src.models.alerts.alert import Alert
from src.models.users.user import User
import src.models.users.decorators as user_decorator

user_blueprint = Blueprint('users', __name__) # létrehoz egy templatet
@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email  = request.form['email']
        password = request.form['password']
        print(password)
        print(email)

        try:
            if (User.is_login_valid(email, password)):
                session['email'] = email
                return redirect(url_for(".user_alerts")) # átdobja a usert a másik oldalra
        except UserErrors.UserError as e:
            return e.message

    return render_template("users/login.jinja2") # loginform # azért kívülre ez a mondat, hogyha post a visszatérés és rossz a hashelt jelszó, ne fussunk hibára

@user_blueprint.route('/register', methods = ['GET','POST'])
def register_user():
    if request.method == 'POST':
        email  = request.form['email']
        password = request.form['password']
        print(password)
        print(email)

        try:
            if (User.register_user(email, password)):
                session['email'] = email
                return redirect(url_for(".user_alerts")) # átdobja a usert a másik oldalra
        except UserErrors.UserError as e:
            return e.message

    return render_template("users/register.jinja2")


@user_blueprint.route('/alerts')
@user_decorator.require_login # decorator
def user_alerts():
    user = User.find_by_email(session['email']) # currently logged in user
    alerts = user.get_alerts()
    return render_template('users/alerts.jinja2',alerts=alerts)

@user_blueprint.route('/logout')
def logout_user():
    session['email']=None
    return redirect(url_for('home'))

@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alert(user_id):
    pass


