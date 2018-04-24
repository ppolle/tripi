from flask import render_template,request,redirect,url_for
from . import main
from .. import db
from ..models import Category,Event

# Views
@main.route('/')
def index():
	title = 'Tripi'
	category=Category.query.all()
	events=Event.query.all()
	return render_template('index.html',title = title,category=category,event=event)
'''
a view function that displays a specific category and its various events
'''
@main.route('/category/<int:id>',methods=["GET","POST"])
def category(id):
	categories=Category.query.filter_by(id=id).first()

	events=Event.query.filter_by(category_id=id).all()
	return render_template('main/category.html',categories=categories,events=events)
@main.route('/Event/<int:id>')
def event(id):
	title='Available Events'
	trips=Event.query.filter_by(id=id).first()
	return render_template('main/events.html',title=title,trips=trips)
