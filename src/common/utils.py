
from passlib.hash import pbkdf2_sha512
import re

__author__ = "Zexx"

class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_adress_matcher = re.compile('^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_adress_matcher.match(email) else False

    @staticmethod
    def hash_password(password):
        #sha512-ből pbkdf2_sha512-be nyomja át a user passt
        return pbkdf2_sha512.hash(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Checks that the user sent pass matches the database version

        :param password: sha512 hashed password
        :param hashed_password: pbkdf2_sha512 encrypted password
        :return: true if pass match, false otherwise
        """

        return pbkdf2_sha512.verify(password, hashed_password)
