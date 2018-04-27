from . import login_manager, db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))

    email = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.name}'


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    p_count = db.Column(db.Integer)
    event_date = db.Column(db.Date)
    description = db.Column(db.String)
    creator_id = db.Column(db.Integer)
    joiner_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return f'Event {self.name}'


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    events = db.relationship('Event', backref='event', lazy='dynamic')

    def __repr__(self):
        return f'Category {self.name}'


class Join(db.Model):
    __tablename__ = 'joiners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    event_id = db.Column(db.Integer)
    creator_id = db.Column(db.Integer)
    joiner_id = db.Column(db.Integer)

    def __repr__(self):
        return f'Joiner {self.name}'
