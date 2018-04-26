from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db
from ..models import Category,Event,User
from flask_login import login_required,current_user
from .forms import JoinForm
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
@main.route('/category/event/<int:id>',methods=["GET","POST"])
def event(id):
	title='Available Events'

	trips=Event.query.filter_by(id=id).all()
	users=User.query.all()

	def getuser(id):
		user = User.query.filter_by(id=id).first()
		return  user.id

	return render_template('main/event.html',title=title,trips=trips,getuser=getuser)

@main.route('/join/<int:id>/<user_id>',methods=["GET","POST"])
@login_required
def join(id,user_id):
	# form=JoinForm()


	event=Event.query.filter_by(id=id).first()
	user=User.query.filter_by(id=user_id).first()

	if user is None:
		abort(404)
	form=JoinForm()

	if form.validate_on_submit():
		# join=Event(joiner_id=id)
		user.event_id=id
		# db.session.add(join)
		db.session.commit()
		flash('you joined this event')
		return redirect (url_for('.people',id=event.id,))

	title= 'Join Event'
	return render_template ('main/join.html',title=title,form=form,event=event)
@main.route('/your_event/<int:id>',methods=["GET","POST"])
def people(id):
	event=Event.query.filter_by(id=id).all()

	for ev in event:
		ev.p_count=ev.p_count-1
		# ev.p_count=s
		db.session.commit()

	db.session.commit()



	user=User.query.filter_by(event_id=id).all()
	return render_template('main/people.html',event=event,user=user)
