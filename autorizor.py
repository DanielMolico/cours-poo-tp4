from authenticator import Authenticator

class Authorizor:

    permissions_key = 1

    def __init__(self, authenticator):
        self.authentificator = authenticator
        self.permissions = {}

    def add_permission(self, permission_name):
        if permission_name not in self.permissions:
            self.permissions[self.permissions_key] = permission_name
            self.permissions_key += 1
            
    def check_permission(self, username, permission_name):
        for permission in self.permissions:
            if permission in self.permissions:
                pass

        self.username = username
        self.permission_name = permission_name

    def grant_permission(self, username, permission_name):
        self.username = username
        self.permission_name = permission_name

# auth1 = Authenticator()
# auth1.add_user("Daniel","234r25r47")
# auto = Authorizor(auth1)
# auto.add_permission("Ajouter")
# auto.add_permission("supprimer")
# print(auto.permissions)
