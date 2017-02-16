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
