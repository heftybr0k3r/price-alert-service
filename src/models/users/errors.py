
__author__ = "Zexx"

# Setting up the different exceptions for User class
class UserError(Exception):
    def __init__(self, message):
        self.message = message

class UserNotExistsError(UserError):
    pass

class IncorrectPasswordError(UserError):
    pass

class UserAlreadyReegisteredErorr(UserError):
    pass

class InvalidEmailError(UserError):
    pass
