from . import db # Importing from this package (website) (since it is in __init__.py)
from flask_login import UserMixin
from sqlalchemy.sql import func

# Each user will have notes... they need to be stored in the database so we must design a model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #func.now() gets current date/time
    # Setting up relationship between notes and users using a foreign key
    # References an ID to another database column
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Specifying foreign key means that we must pass an id of an existing user


# Creating database model for User info
# Essentially telling the database that 'all users need to look like this'
# UserMixin as a parameter as it significantly simplifies the process by using a library instead of desiging user info on our own
class User(db.Model, UserMixin):
    # Defining columns we want stored in the table (desigining schema for database)
    id = db.Column(db.Integer, primary_key=True) # Defining our id to be the primary key for each user
    email = db.Column(db.String(150), unique=True) # 150: Max Length of the string unique=True: ensures there are no duplicate emails
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    # Setting up relationship to Note
    notes = db.relationship('Note')
    