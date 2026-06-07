import secrets
from cryptography.fernet import Fernet as fernet
import os

class Security:
    def __init__(self, key):
        self.fernet = fernet(key)

    def encrypt(self, data):
        return self.fernet.encrypt(data)        

    def decrypt(self, data):
        return self.fernet.decrypt(data)  
