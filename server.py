
import os

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, Markup, request, session
from flask_socketio import SocketIO, emit


# import yelp_query

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()

socketio = SocketIO(app)

@app.context_processor
def getVars():
    return {
        "owner": "UMW Goats",
        "now": datetime.now()
    }

@socketio.on("search", namespace="/socketio")
def search(query):
    emit("addResult", "result")


@app.route("/", methods=['GET', 'POST'])
def mainIndex():
    data = []
    total = 0
    if request.method == 'POST':
        try:

            session['location'] = request.form['search_term']

            if 'location' not in session:
                session['location'] = 'Norfolk'



            if session['location'] == 'Norfolk':
                data = [
                        {'value': '0','content':'1 ' + Markup('<span class="fa fa-star"></span>')},
                        {'value': '0','content':'2 ' + Markup(' <span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                        {'value': '0','content':'3 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                        {'value':'85','content':'4 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                        {'value': '15','content':'5 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')}
                       ]
                overall = 83


            elif session['location'] == '22401':
                session['location'] = 'Fredericksburg'
                data = [
                        {'value': '0','content':'1 ' + Markup('<span class="fa fa-star"></span>')},
                        {'value': '0','content':'2 ' + Markup(' <span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                        {'value': '10','content':'3 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                        {'value': '90','content':'4 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                        {'value': '0','content':'5 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')}
                       ]
                overall = 78

            elif session['location'] == 'New York':
                data = [
                        {'value': '0','content':'1 ' + Markup('<span class="fa fa-star"></span>')},
                        {'value': '0','content':'2 ' + Markup(' <span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                        {'value': '0','content':'3 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                        {'value': '70','content':'4 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                        {'value': '30','content':'5 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')}
                       ]
                overall = 86

            elif session['location'] == '12345':
                session['location'] = 'Schenectady'
                data = [
                        {'value': '13','content':'1 ' + Markup('<span class="fa fa-star"></span>')},
                        {'value': '13','content':'2 ' + Markup(' <span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                        {'value': '50','content':'3 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                        {'value': '24','content':'4 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                        {'value': '0','content':'5 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')}
                       ]
                overall = 20

            return render_template('charts.html', data = data, overall = overall)

        except:
            print("Error")


    return render_template('charts.html')

if __name__ == "__main__":
    socketio.run(app, host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)
