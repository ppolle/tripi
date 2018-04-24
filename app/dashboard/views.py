from flask import render_template, redirect, url_for, flash, request
from . import dashboard
from flask_login import login_user, logout_user, login_required, current_user
from ..models import User, Event, Category
from .forms import createEventForm, editEventForm
from .. import db


@dashboard.route('/createEvent/<int:id>', methods=['GET', 'POST'])
def dashboardIndex(id):
    event_form = createEventForm()
    if event_form.validate_on_submit():
        event = Event(name=event_form.title.data, location=event_form.location.data, p_count=event_form.persons.data, event_date=event_form.date.data, description=event_form.event_desc.data, creator_id=id)
        db.session.add(event)
        db.session.commit()
        flash(f'Event {event_form.title.data} created succesfully')
        return redirect(url_for('dashboardIndex.dashboard',id =id))
    render_template('dashbaord/index.html',id = id, event_form=event_form)


@dashboard.route('/editEvent/<int:id>', methods=['GET', 'POST'])
def editEvent(id):
    editForm = editEventForm()

    if editForm.validate_on_submit():
        Event.query.filter_by(id=id).update({"name": editForm.title.data, "location": editForm.location.data,
                                             "p_count": editForm.persons.data, "event_date": editForm.date.data, "description": editForm.event_desc.data})
        db.session.commit()
        flash(f'Event {editForm.title.data} succesfully edited.')
        return redirect(url_for('dashboardIndex.dashboard', id=id))
    render_template('dashbaord/index.html', id=id, editForm=editForm)

    
