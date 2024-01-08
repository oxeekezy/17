import sqlite3

class Db:

    connection: object = None
    cursor: object = None

    def __init__(self):
        self.connection = sqlite3.connect()
