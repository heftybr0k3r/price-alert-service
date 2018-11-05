import uuid
from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors
from src.models.alerts.alert import Alert
import src.models.users.constants as UserConstants

__author__ = "Zexx"


class User(object):

	# Constructor
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User: {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        verifiyng email password combo as sent by the site forms,
        is valid or not, checks that the email exists
        and the pass associated with it is correct
        :param email: users' mail
        :param password: hashed password (sha512)
        :return: true if valid false otherwise
        """
        user_data = Database.find_one(UserConstants.COLLECTION, {"email": email})
        if user_data is None:
            # email doesn't exist
             raise UserErrors.userNotExistsError("Nincs ilyen felhasználó az adatbázisban!")
        if not Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectPasswordError("Hibás jelszó!")

        return True

    @staticmethod
    def register_user (email, password):
        """
        Register an user with email and password
        password already in sha512 form,
        :param email: user's email
        :param password: sha512 hash
        :return: true if succesfull, false otherwise, and or exceptions
        """
        user_data = Database.find_one(UserConstants.COLLECTION, {"email": email})

        if user_data is not None: # already exists in the db
            raise UserErrors.UserAlreadyReegisteredErorr("Az e-mail cím már létezik az adatbázisban!")
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError("Az e-mail cím formátuma nem megfelelő ")
            pass
        User(email, Utils.hash_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert(UserConstants.COLLECTION, self.json())

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }

    @classmethod
    def find_by_email(cls, email):
        return cls(**Database.find_one(UserConstants.COLLECTION, {"email": email}))

    def get_alerts(self):
        return Alert.find_by_user_email(self.email)