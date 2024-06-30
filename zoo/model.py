from . import db
import flask_login
from sqlalchemy.sql import func
import enum


class UserRole(enum.Enum):
    customer = 1
    manager = 2


class User(db.Model, flask_login.UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    # manager = db.Column(db.Boolean, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Enum(UserRole), unique=False, nullable=False)
    
    #A user has many reservations
    reservations=db.relationship('Reservation', backref='user', lazy=True)


class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    information = db.Column(db.String(7000), nullable=False)
    img_path = db.Column(db.String(128))


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    information = db.Column(db.String(7000), nullable=False)
    marked = db.Column(db.Boolean, default=False, nullable = False)
    min_age = db.Column(db.Integer, nullable=True)
    max_age = db.Column(db.Integer, nullable=True)
    duration= db.Column(db.Integer, nullable=False)

    #An activity can be scheduled many times
    activities=db.relationship('Scheduled',backref='activity',lazy=True)


class Scheduled(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'), nullable=False)
    date = db.Column(db.DateTime(), nullable=False) 
    available_places = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    #A scheduled activity can have multiple reservations
    reservations=db.relationship('Reservation', backref='scheduled', lazy=True)


class Reservation(db.Model):

    # A reservation has one user and one scheduled activity
    # which are defined below

    id=db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    scheduled_id = db.Column(db.Integer, db.ForeignKey('scheduled.id'), nullable=False)
    booked_places = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(), default=func.now()) # time when reservation is made