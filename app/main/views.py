from flask import render_template, request, redirect, url_for, flash, abort
from . import main
from .. import db
from flask_login import login_user, logout_user, login_required, current_user
from ..models import Category, Event, Join
from flask import jsonify

# Views


@main.route('/')
def index():
    title = 'Tripi'
    category = Category.query.all()
    events = Event.query.all()
    return render_template('index.html', title=title, category=category, event=event)


'''
a view function that displays a specific category and its various events
'''


@main.route('/category/<int:id>', methods=["GET", "POST"])
def category(id):
    categories = Category.query.filter_by(id=id).first()
    events = Event.query.filter_by(category_id=id).all()
    return render_template('main/category.html', categories=categories, events=events)


@main.route('/category/event/<int:id>', methods=["GET", "POST"])
def event(id):
    title = 'Available Events'
    trips = Event.query.filter_by(id=id).all()
    activities = Event.query.all()
    return render_template('main/event.html', title=title, trips=trips, activities=activities)


@main.route('/join/<int:creatorId>/<int:eventId>', methods=["GET", "POST"])
@login_required
def join(creatorId, eventId):
    checkJoin = Join.query.filter_by(event_id=eventId, joiner_id=current_user.id).first()
    if checkJoin:
        flash('You have already registered for this particular event')
        return redirect(url_for('dashboard.dashboardIndex', id=current_user.id))
    else:
        event = Event.query.get(eventId).p_count
        Event.query.filter_by(id=eventId).update({"p_count": event-1})
        join = Join(name=current_user.firstname, joiner_id=current_user.id,
                    creator_id=creatorId, event_id=eventId)
        event = Event.query.get(eventId)
        db.session.add(join)
        db.session.commit()
        flash(f'You have succesfully joined {event.name} Event')
        return redirect(url_for('dashboard.dashboardIndex', id=current_user.id))
