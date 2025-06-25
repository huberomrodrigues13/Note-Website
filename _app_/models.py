#This is where you store all your database models (Which are python classes that define tables)#

from . import db 
from sqlalchemy import Column, String, Integer

from flask_login import UserMixin
from sqlalchemy.sql import func

#Database model(db.Model) is a blueprint for a object that will be stored in your database#

#Main Object:
class User(db.Model, UserMixin): #User is a table/column#

    #Everything underneath is the schema/predefined-fields of the table/column#
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

    notes = db.relationship("Note")

#Sub-Object:
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


#Tip: 'user.id' is the id field in User class. Python convention for classes are uppercased, but
    #in a database they get converted into lowercase.