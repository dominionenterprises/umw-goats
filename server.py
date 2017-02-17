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
