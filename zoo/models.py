from . import db
from flask_login import UserMixin # Custom class -> User object for flask login
from sqlalchemy.sql import func
import enum


from . import db
import flask_login
from sqlalchemy.sql import func
import enum




class UserRole(enum.Enum):
    customer = 1
    manager = 2

class User(db.Model, flask_login.UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Enum(UserRole), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    reservations=db.relationship('Reservation', backref='user', lazy=True)



class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    information = db.Column(db.String(1000), nullable=False)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    information = db.Column(db.String(1000), nullable=False) # Recommended age range
    marked = db.Column(db.Boolean, default=False, nullable = False)
    activities=db.relationship('ScheduledActivity',backref='activity',lazy=True)



class ScheduledActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    date = db.Column(db.DateTime, nullable=False) # Date and time of the activity
    available_places = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    reservations=db.relationship('Reservation', backref='scheduledactivity', lazy=True)





class Reservation(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    scheduled_id = db.Column(db.Integer, db.ForeignKey('scheduled_activity.id'), nullable=False)

    booked_places = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=func.now()) # time when reservation is made

    

'''
class UserRole(enum.Enum):
    customer = 1
    manager = 2

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Enum(UserRole), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # Create a list of reserved activities
    schedule = db.relationship('ActivityReservation')

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    information = db.Column(db.String(1000), nullable=False)

class Activity(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    information = db.Column(db.String(1000), nullable=False) # Recommended age range
    marked = db.Column(db.Boolean, default=False, nullable = False)

# One to many relationship (One activity has many times)
# Reference the parent object by each child (Foreignkey)
# Store key on child objects -> Reference to parent object

class ScheduledActivity(db.Model):
    # Same activity can be scheduled many dates
    id = db.Column(db.String(64), primary_key = True)
    activity_id = db.Column(db.String(64), db.ForeignKey('activity.id'))
    # Date and time of the activity
    date = db.Column(db.DateTime, nullable=False)
    # Number of places 
    available_places = db.Column(db.Integer, nullable=False)
    ticket_price = db.Column(db.Float, nullable=False)
    activity=db.relationship('Activity', backref='scheduledactivity', lazy=True)


class ActivityReservation(db.Model):
    # ID of activity
    id=db.Column(db.String(64), primary_key=True)
    # User that made it
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    scheduled_id = db.Column(db.Integer, db.ForeignKey('scheduledactivity.id'), nullable=False)
    # Number of booked places
    booked_places = db.Column(db.Integer, nullable=False)
    # Time of booking
    date = db.Column(db.DateTime, default=func.now())
    # List of activities
<<<<<<< HEAD
    #activity = db.relationship('Activity', backref='scheduledactivity', lazy=True)
'''
=======
    activity=db.relationship('ScheduledActivity', backref='reservation', lazy=True)
    
>>>>>>> cacdc9743f5a06502bfbd1e279af19543c7f2da3
