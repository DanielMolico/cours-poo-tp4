class AuthException(Exception):
    
    def __init__(self, username, user = None):
        super().__init__(self, username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExist(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class InvalidUserName(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

class NoPerission(AuthException):
    pass
