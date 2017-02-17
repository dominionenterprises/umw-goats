<<<<<<< HEAD
import psycopg2
import psycopg2.extras

from config import psql

class DBManager:
    def __init__(self):
        conn = 'dbname=' + psql['db'] + ' user=' + psql['user'] + ' password=' +\
               psql['passwd'] + ' host=' + psql['host']
        try:
            self.__conn = psycopg2.connect(conn)
        except psycopg2.OperationalError:
            print("Can't connect to database")

    def getResults(self, query):
        return query
=======
import psycopg2
import psycopg2.extras

from config import psql

class DBManager:
    def __init__(self):
        conn = 'dbname=' + psql['db'] + ' user=' + psql['user'] + ' password=' +\
               psql['passwd'] + ' host=' + psql['host']
        try:
            self.__conn = psycopg2.connect(conn)
        except psycopg2.OperationalError:
            print("Can't connect to database")

    def getResults(self, query):
        return query
>>>>>>> dfa2096deaf5e48200f70f4e0a0530aa567c3f30
