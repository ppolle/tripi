from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, IntegerField
from wtforms.validators import Required


class createEventForm(FlaskForm):

    title = StringField('Event Name', validators=[Required()])
    location = StringField('Event location', validators=[Required()])
    persons = IntegerField('Number of people', validators=[Required()])
    date = DateField('Event Date', validators=[Required()])
    event_desc = TextAreaField('Event Description')
    submit = SubmitField('Submit')


class editEventForm(FlaskForm):

    title = StringField('Event Name', validators=[Required()])
    location = StringField('Event location', validators=[Required()])
    persons = IntegerField('Number of people', validators=[Required()])
    date = DateField('Event Date', validators=[Required()])
    event_desc = TextAreaField('Event Description')
    submit = SubmitField('Submit')

