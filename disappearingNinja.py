#no time to implement all 6 images correctly; just did the core logic
from flask import Flask, render_template, request, redirect,session, flash
import random
import re
import datetime
app = Flask(__name__)
app.secret_key='poshit'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template('index.html',image='all')
@app.route('/<color>')
def ninja(color):
    if color=='blue':
        return render_template('index.html',image='leo')
    if color=='red':
        return render_template('index.html',image='don')


app.run(debug=True)
#url_for('static', filename='images/tmnt.png')