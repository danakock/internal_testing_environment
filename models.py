from flask_login import UserMixin
from . import db

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

class Subscriptions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(10))
    tier = db.Column(db.String(7))