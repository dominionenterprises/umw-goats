import yelp_query


import os

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, Markup, request, session
from flask_socketio import SocketIO, emit
#from selenium.webdriver.common.by import By

import yelp_query

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

# @app.route('/getRestaurants', methods=['GET', 'POST'])
# def restaurants():
#     data = [
#             {'value':'30','content':'1 ' + Markup('<span class="fa fa-star"></span>')},
#             {'value':'10','content':'2 ' + Markup(' <span class="fa fa-star"></span><span class="fa fa-star"></span>')},
#             {'value':'5','content':'3 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
#             {'value':'20','content':'4 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
#             {'value':'40','content':'5 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')}
#            ]
#
#     #
#     # yelpsearch = yelp_query.yelper()
#     # ratingslist = yelpsearch.resturant_search(22401)
#     # print(type(ratingslist[0]))
#     # print(ratingslist[0])
#     #
#     # # for rating in ratingslist:
#     # #     tempList
#     #
#     #
#     #
#     # data = [
#     #     {'value': '20','content':'1 ' + Markup('<span class="fa fa-star"></span>')},
#     #     {'value': '20','content':'2 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span>')},
#     #     {'value': '20','content':'3 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
#     #     {'value': '20','content':'4 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
#     #     {'value': '20','content':'5 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')}
#     # ]
#
#     # print(data[0])
#
#     # overall = 40
#     location = 'Brooklyn+Bridge,New+York,NY';
#     return render_template('charts.html')

@app.route("/", methods=['GET', 'POST'])
def mainIndex():
    data = []
    total = 0
    if request.method == 'POST':
        try:
            if 'location' not in session:
                session['location'] = 22401

            session['location'] = request.form['search_term']

            yelpsearch = yelp_query.yelper()
            ratingslist = yelpsearch.resturant_search(session['location'])
            print(session['location'])
            # for rating in ratingslist:
            #     total = total + rating
            print(sum(ratingslist))
            print("SUM")
            # print(total)
            print("after for")

            # for rating in ratingslist:
            #     percent = int((rating/total) * 100)
            #     print(int(percent))
            #

            data = [
                    {'value': str(ratingslist[0]),'content':'1 ' + Markup('<span class="fa fa-star"></span>')},
                    {'value': str(ratingslist[1]),'content':'2 ' + Markup(' <span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                    {'value': str(ratingslist[2]),'content':'3 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                    {'value': str(ratingslist[3]),'content':'4 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')},
                    {'value': str(ratingslist[4]),'content':'5 ' + Markup('<span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span><span class="fa fa-star"></span>')}
                   ]
            return render_template('charts.html', data = data)




            # print(type(ratingslist[0]))
            # print(ratingslist[0])

            # if 'location' not in session:
            #     print("before category")
            #     session['category'] = request.form['category']
            #     pring("after category")
            #     print(category)
        except:
            print("ughhhhhhhhhh")




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
