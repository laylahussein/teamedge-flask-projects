from flask import Flask, render_template, redirect, url_for, request, current_app as app
app = Flask(__name__)

from sense_hat import SenseHat
from time import sleep


sense = SenseHat()
sense.low_light = True


@app.route('/')
def index():
   return render_template("messageboard.html")

@app.route('/success', methods = ['GET', 'POST'])
def success():
   message = request.form['message']
   name = request.form['name']
   sense.show_message(message, scroll_speed = 0.4)
   return render_template("success.html", message = message)


@app.route('/all')
def all():
   #connect to DB
   conn = sqlite3.connect('./static/data/messageboard_database.db')
   curs = conn.cursor()
   message = []
   rows = curs.execute("SELECT * from messages")
   for row in rows:
      message = {'name': row[0], 'message':row[1]}
      messages.append(message)
   conn.close()
   return render_template('all.hmtl', messages = messages)


if __name__ == '__main__':
   app.run(debug = True, host = '0.0.0.0')