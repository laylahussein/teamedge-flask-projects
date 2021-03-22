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


if __name__ == '__main__':
   app.run(debug = True, host = '0.0.0.0')