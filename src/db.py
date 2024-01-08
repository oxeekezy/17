import sqlite3
from dotenv import load_dotenv
import os

class Db:
    connection: sqlite3.Connection = None
    cursor: sqlite3.Cursor = None

    def __init__(self):
        self.connection = sqlite3.connect('main.db')
        self.cursor = self.connection.cursor()
        self._init_tables()

        
    def _init_tables(self):
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS clients 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                fullname TEXT, 
                isCurrent BOOLEAN,
                email TEXT,
                phone TEXT)
        """)
        self.connection.commit()

    def create_client(self, client: ()):
        sql ="""
                INSERT INTO clients(fullname, isCurrent, email, phone)
                VALUES(?,?,?,?)          
        """
        self.cursor.execute(sql, client)
        self.connection.commit()

    def get_client(self, id: int):
        sql = """
            SELECT * FROM clients WHERE id=?
        """
        self.cursor.execute(sql, (id,))
        
        return self.cursor.fetchall()
    
    def get_clients(self):
        sql = """
            SELECT * FROM clients
        """
        self.cursor.execute(sql)
        
        return self.cursor.fetchall()

        
    
f = Db()
#f.create_client(('sadsadasd', True, 'sfdsfdsfsdfsdf@sdssds', '029128391238'))
print(f.get_clients())