from flask import Flask, render_template, request, json, jsonify, current_app as app
from datetime import date
import os
import requests

app = Flask(__name__)

@app.route('/uglycountry')
def uglycountry():
    response = requests.get('https://date.nager.at/api/v2/publicholidays/2020/US')
    data = response.json()
    return render_template('holidays.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')