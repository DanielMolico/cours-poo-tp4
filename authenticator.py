from users import User
from authexception import UsernameAlreadyExist, PasswordTooShort

class Authenticator:

    def __init__(self):
        self.users = {}

    def add_user(self,username, password):
        if username in self.users:
            raise UsernameAlreadyExist(username)
        if len(password) < 4:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def logIn(self,username, password):
        for user in self.users:
            if user[username] == username & user[password] == password:
                self.user.status = True

    def logout(self,username):
        if username in self.users:
            self.users[username].status = False
