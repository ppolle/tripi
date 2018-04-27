from flask import render_template, redirect, url_for, flash, request
from . import dashboard
from flask_login import login_user, logout_user, login_required, current_user
from ..models import User, Event, Category
from .forms import createEventForm, editEventForm
from .. import db
import markdown2


@dashboard.route('/createEvent/<int:id>', methods=['GET', 'POST'])
@login_required
def dashboardIndex(id):
    event_form = createEventForm()

    events = Event.query.filter_by(creator_id=id).all()
    event = Event.query.filter_by(creator_id=id).first()
    eventsJoined = Event.query.filter_by(joiner_id=id).all()

    if event_form.validate_on_submit():
        print(event_form.category.data)
        category = Category.query.filter_by()
        event = Event(name=event_form.title.data, location=event_form.location.data, p_count=event_form.persons.data,
                      event_date=event_form.date.data, description=event_form.event_desc.data, creator_id=id, category_id=int(event_form.category.data))
        db.session.add(event)
        db.session.commit()
        flash(f'Event {event_form.title.data} created succesfully')
        return redirect(url_for('dashboard.dashboardIndex', id=id))

    title = "Tripi | Dashboard"
    return render_template('dashboard/index.html', id=id, event_form=event_form, events=events, title=title)


@dashboard.route('/editEvent/<int:id>', methods=['GET', 'POST'])
@login_required
def editEvent(id):
    editForm = editEventForm()
    event = Event.query.get(id)

    if editForm.validate_on_submit():
        Event.query.filter_by(id=id).update({"name": editForm.title.data, "location": editForm.location.data,
                                             "p_count": editForm.persons.data, "event_date": editForm.date.data, "description": editForm.event_desc.data})
        db.session.commit()
        flash(f'Event {editForm.title.data} succesfully edited.')
        return redirect(url_for('dashboard.dashboardIndex', id=event.creator_id))
    editForm.location.data = event.location
    editForm.title.data = event.name
    editForm.event_desc.data = event.description
    editForm.date.data = event.event_date
    editForm.category.data = event.event
    editForm.persons.data = event.p_count
    title = "Tripi | Edit Event"
    return render_template('dashboard/edit.html', editForm=editForm, event=event, title=title)


@dashboard.route('/deleteEvent/<int:id>')
@login_required
def delete(id):
    event = Event.query.get(id)
    db.session.delete(event)
    db.session.commit()

    flash(f'You have succesfully deleted the {event.name} Event')
    return redirect(url_for('dashboard.dashboardIndex', id=current_user.id))


@dashboard.route('/single/<int:id>')
@login_required
def single(id):
    details = Event.query.get(id)
    title = f"Tripi| {details.name}"

    formatEvent = markdown2.markdown(details.description, extras=[
                                     "code-friendly", "fenced-code-blocks"])
    return render_template('dashboard/single.html', details=details, title=title, formatEvent=formatEvent)
