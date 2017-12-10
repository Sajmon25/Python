import _mysql


class DB():

    db = ""

    # def __init__(self):
    #     self.db = _mysql.connect("localhost", "root", "zaq12wsx", "sakila")

    def get_connection(self):
        #self.db = _mysql.connect("localhost", "root", "zaq12wsx", "sakila")
        return self.db

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.db.close()

    def login(self, login, password):
        return self.db.execute("SELECT first_name, last_name FROM actor WHERE user_name = ? AND password = ?", (login, password))
