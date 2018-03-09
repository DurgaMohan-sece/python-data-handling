import pymysql
from contextlib import contextmanager

class DbConnection:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def __enter__(self):
        self.connect = pymysql.connect(host=self.host,
                                       user=self.user,
                                       password=self.password,
                                       db=self.db,
                                       charset='utf8mb4',
                                       cursorclass=pymysql.cursors.DictCursor)
        return self.connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connect:
            self.connect.close()

@contextmanager
def dbconnection(host, user, password, db):
    try:
        connect = pymysql.connect(host=host,
                                  user=user,
                                  password=password,
                                  db=db,
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)
        yield connect

    finally:
        connect.close()