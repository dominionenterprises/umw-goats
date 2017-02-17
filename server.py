import yelp_query


import os

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, Markup, request, session
from flask_socketio import SocketIO, emit

from yelp_query import zillower

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
        loc = request.form['search_term']
        try:
            if 'location' not in session:
                session['location'] = 22401

            session['location'] = request.form['search_term']
            yelpsearch = yelp_query.yelper()
            ratingslist = yelpsearch.resturant_search(session['location'])
            
            data = [
                    {'value': str(ratingslist[0]),'content':'1 ' + Markup('<span class="fa fa-star"></span>')},
                    {'value': str(ratingslist[1]),'content':'2 ' + Markup(' <span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                    {'value': str(ratingslist[2]),'content':'3 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                    {'value': str(ratingslist[3]),'content':'4 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                    {'value': str(ratingslist[4]),'content':'5 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')}
                ]
            return render_template('charts.html', data = data)

        except Exception as e:
            print("ughhhhhhhhhh", e)




        # print("category:")
        # print(category)
        # if category == "":
        #     loc = request.form['search_term']
        #     print("loc")
        #     print(loc)

        # if category == 'restaurant':
        #     data = getRestaurant(location);
        #
        # elif category == 'shopping':
        #     data = getShopping(location);
        #
        # elif category == 'nightlife':
        #     data = getNightLife(location);
        #
        # elif category == 'travel':
        #     data = getTravel(location);
        #
        # elif category == 'housing':
        #     data = getHousing(location);
        #
        # elif category == 'safety':
        #     data = getSafety(location);
        #
        # elif category == 'activites':
        #     data = getActivites(location);
        #
        # else:



    # qualityOfLife = getQuality(location);
    #
    # locationMapFormat = 'Brooklyn+Bridge,New+York,NY';

    return render_template('charts.html')
# , livingQuality=qualityOfLife, buttons=buttonItems, data = data, location = locationMapFormat

if __name__ == "__main__":
    socketio.run(app, host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)
