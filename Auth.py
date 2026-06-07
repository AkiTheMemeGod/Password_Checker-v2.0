from Database import Database
import bcrypt as hash
from cryptography.fernet import Fernet as fernet

"""
pw = b'GeekPassword'
s = bcrypt.gensalt()
h = bcrypt.hashpw(pw, s) # Hash password
entered_pw = b'GeekPassword'

if bcrypt.checkpw(entered_pw, h):
    print("Password match!")
else:
    print("Incorrect password.")
"""


class Authentication:
    def __init__(self):
        self.db = Database()
        

    def register(self, username, password):

        try:
            password = password.encode("utf-8")

            self.key = fernet.generate_key()
            salt = hash.gensalt()

            hash_password = hash.hashpw(password, salt)
            data = (username, hash_password, self.key, salt)

            self.db.cur.execute("INSERT INTO USERS VALUES (?, ?, ?, ?)", data)
            self.db.conn.commit()

            return {"Success" : True, "Message" : "Successfully Registered"}

        except Exception as IntegrityError:
            return {"Success" : False, "Message" : "Username Already Exists"}
        

    def login(self, username, password):
        try:
            password = password.encode("utf-8")

            self.db.cur.execute("SELECT username, password, key, salt FROM USERS WHERE username=?", (username, ))
            user = self.db.cur.fetchone()
            hash_pw = user[1]
            if hash.checkpw(password, hash_pw):
                return {"Success" : True, "Message" : "Successfully Logged in", "Key" : user[2]}
            else:
                return {"Success" : False, "Message" : "Wrong Credentials"}
            
        except Exception as e:
            return {"Success" : False, "Message" : e}

