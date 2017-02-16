import os
import uuid
import psycopg2
import psycopg2.extras
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


# start the server
if __name__ == '__main__':
        socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8080)), debug=True)
