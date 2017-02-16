import os

import psycopg2
import psycopg2.extras

from datetime import datetime
from flask import Flask, session, request, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()

socketio = SocketIO(app)

@app.route('/')
def mainIndex():
    # print 'in hello world'
    return render_template('index.html')


# start the server
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)
