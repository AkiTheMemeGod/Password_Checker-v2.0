import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("mypass.db", check_same_thread=False)
        self.cur = self.conn.cursor()

    


class Generate(Database):    
    pass
class Manage(Database):
    pass