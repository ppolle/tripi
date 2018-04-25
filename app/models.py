from . import login_manager,db
from flask_login import UserMixin
from datetime import datetime
from . import db

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))



    def __repr__(self):
        return f'User {self.name}'

class Event(db.Model):
	__tablename__ = 'events'
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String)
	location = db.Column(db.String)
	p_count = db.Column(db.Integer)
	event_date = db.Column(db.Date)
	description = db.Column(db.String)
	creator_id = db.Column(db.Integer)
	joiner_id = db.Column(db.Integer)
	category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))

	def __repr__(self):
		return f'Event {self.name}'

class Category(db.Model):
	__tablename__ = 'categories'
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String)
	events = db.relationship('Event',backref = 'event',lazy = 'dynamic')

	def __repr__(self):
		return f'Category {self.name}'
