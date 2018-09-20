# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 23:30:31 2018

@author: dell
"""
from flask import Flask ,render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1> Hello World<h1>'

@app.route('/user/<city>')
def user(city):
    if city == 'Karachi':
        return render_template('karachi.html',city='Karachi')
    elif city == 'Lahore':
        return render_template('lahore.html',city='Lahore')

if __name__ == '__main__':
    app.run(debug=True)
