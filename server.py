import os
import psycopg2
import psycopg2.extras
import config
import datetime
from datetime import datetime
from flask import Flask, session, request, render_template
from flask_socketio import SocketIO, emit

from config import psql

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()

socketio = SocketIO(app)

@socketio.on("search", namespace="/socketio")
def search(query):
    print(query)
    emit("addResult", "result")

def connectToDB():
    connection = 'dbname=' + psql['db'] + ' user=' + psql['user'] + ' password=' + psql['passwd']  + ' host=' + psql['host']
    host = 'localhost'
    print(connection)
    try:
        return psycopg2.connect(connection)
    except:
        print("Can't connect to database")

@app.route('/')
def mainIndex():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app, host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)