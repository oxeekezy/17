from db import Db

class User: 
    
    _db = Db()
    _cursor = _db.cursor

    def __init__(self):
        pass

    def create_user(self, user: ()):
        sql = """
            INSERT INTO users(login, password, isAdmin)
            VALUES(?,?,?) 
        """

        self._cursor.execute(sql, user)
        self._db.save()

    def login(self, login: str, password: str):
        user = self._get_user(login=login)

        if(user.password != password):
            return False
        
        return True

    def _get_user(self, login: str):
        sql = """
            SELECT * FROM  users
            WHERE login=?
        """
        self._cursor.execute(sql, (login,))
        return self._cursor.fetchall()[0]

