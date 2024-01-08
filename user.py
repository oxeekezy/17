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

        if(user is None or user[2] != password):
            return False
        
        return True

    def _get_user(self, login: str):
        sql = """
            SELECT * FROM  users
            WHERE login=?
        """
        self._cursor.execute(sql, (login,))
        result = self._cursor.fetchall()

        if(len(result)>0):
            return result[0]

        return None



#u = User()
#u.create_user(('oxeek', '123', True))
#u.create_user(('123', '123', False))