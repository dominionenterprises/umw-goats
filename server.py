import os
import uuid
import psycopg2
import psycopg2.extras
import config
import datetime


from datetime import datetime
from flask import Flask, session, request
from flask_socketio import SocketIO, emit
from flask_socketio import join_room, leave_room

app = Flask(__name__, static_url_path='')

app.secret_key = os.urandom(24).encode('hex')

socketio = SocketIO(app)

app.route('/')
def mainIndex():
    # print 'in hello world'
    return app.send_static_file('index.html')

def connectToDB():
    connection = 'dbname=' + psql['db'] + ' user=' + psql['user'] + ' password=' + psql['passwd']  + ' host=' + psql['host']
    host = 'localhost'
    print connnection
    try:
        return psycopg2.connect(connection)
    except:
        print("Can't connect to database")

# start the server
if __name__ == '__main__':
        socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8080)), debug=True)
