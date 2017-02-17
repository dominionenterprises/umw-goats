<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 4c69aa071cb00ab815aeb800f601b20288d9e194
import os

from flask import Flask, session, request, render_template
from flask_socketio import SocketIO, emit

from database import DBManager
#we got this
app = Flask(__name__)
app.secret_key = os.urandom(24).hex()

db = DBManager()
socketio = SocketIO(app)

@socketio.on("search", namespace="/socketio")
def search(query):
    for result in db.getResults(query):
        emit("addResult", result)

@app.route("/")
def mainIndex():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app, host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)
<<<<<<< HEAD
=======
=======
import os

from datetime import datetime
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from config import psql

from database import DBManager

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()

db = DBManager()
socketio = SocketIO(app)

@app.context_processor
def getVars():
    return {
        "owner": "UMW Goats",
        "now": datetime.now()
    }

@socketio.on("search", namespace="/socketio")
def search(query):
    for result in db.getResults(query):
        emit("addResult", result)

@app.route("/")
def mainIndex():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app, host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)
>>>>>>> dfa2096deaf5e48200f70f4e0a0530aa567c3f30
>>>>>>> 4c69aa071cb00ab815aeb800f601b20288d9e194
