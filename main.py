from flask import Blueprint, render_template
from . import db
from mixpanel import Mixpanel

main = Blueprint('main', __name__)
mp = Mixpanel("YOUR_TOKEN")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home.html')
def home():
    return render_template('home.html')