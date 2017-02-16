import os

import psycopg2
import psycopg2.extras

from datetime import datetime
from flask import Flask, session, request, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()

socketio = SocketIO(app)

@socketio.on("connect", namespace="/socketio")
def connect():
    print("connect")

@socketio.on("search", namespace="/socketio")
def search(query):
    print(query)
    emit("addResult", "result")

@app.route('/')
def mainIndex():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app, host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)
