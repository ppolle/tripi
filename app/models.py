# from . import login_manager
from flask_login import UserMixin
from datetime import datetime
import googlemaps
import responses
# from . import db

class Distance:
	
	def __init__(self, origin_addresses, destination_addresses, mode, distance, duration, client):
		'''
		Init method that allows us to create instace of the class
		Args:
			1. origin_addresses
			2. destination_addresses
			3. mode
			4. distance
			5. duration
		'''
		self.origin_addresses = origin_addresses
		self.destination_addresses = destination_addresses
		self.mode = mode
		self.distance = distance
		self.duration = duration
		self.client = googlemaps.Client()

# class User(UserMixin,db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255))
#     email = db.Column(db.String(255))
#     pass_secure = db.Column(db.String(255))
    
    
#     def __repr__(self):
#     	return f'User {self.name}'

# class Event(db.Model):
# 	__tablename__ = 'events'
# 	id = db.Column(db.Integer,primary_key = True)
# 	name = db.Column(db.String)
# 	location = db.Column(db.String)
# 	p_count = db.Column(db.Integer)
# 	event_date = db.Column(db.Date)
# 	description = db.Column(db.String)
# 	creator_id = db.Column(db.Integer)
# 	joiner_id = db.Column(db.Integer)
# 	category_id = db.Column(db.Integer)
	

# 	def __repr__(self):
# 		return f'Event {self.name}'

# class Category(db.Model):
# 	__tablename__ = 'categories'
# 	id = db.Column(db.Integer,primary_key = True)
# 	name = db.Column(db.String)


# 	def __repr__(self):
# 		return f'Category {self.name}'
