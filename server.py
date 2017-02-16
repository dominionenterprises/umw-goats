import psycopg2
import psycopg2.extras
import config

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def mainIndex():
    return render_template('index.html')

def connectToDB():
    connection = 'dbname=' + psql['db'] + ' user=' + psql['user'] + ' password=' + psql['passwd']  + ' host=' + psql['host']
    host = 'localhost'
    print connnection
    try:
        return psycopg2.connect(connection)
    except:
        print("Can't connect to database")

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
