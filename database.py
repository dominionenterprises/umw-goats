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