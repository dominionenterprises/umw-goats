import psycopg2
import psycopg2.extras

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def mainIndex():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
