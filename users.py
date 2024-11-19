import hashlib

class User:
    def __init__(self,username, password):
        self.username = username
        self.password = self._encrypt_password(password)
        self.status = False
    
    def check_password(self, password) -> bool:
        encrypted_password = self._encrypt_password(password)
        return encrypted_password == self.password
    
    def _encrypt_password(self, password) -> str:
        """Esta función permite encriptar la contraseña usando la biblioteca hashlib y y la encriptacion sha256
        """
        password_encoded = password.encode('utf-8')
        return hashlib.sha256(password_encoded).hexdigest()

user = User("Daniel", "Mandarina")
print(user.check_password("Mandarina"))
