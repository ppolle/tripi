from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField,SelectField
from wtforms.validators import Required,NumberRange
from wtforms.fields.html5 import DateField
from wtforms_components import DateRange
from datetime import datetime, date


class createEventForm(FlaskForm):

    title = StringField('Event Name', validators=[Required()],default = "Event Name")
    location = StringField('Event location', validators=[Required()], default="Event Location")
    persons = IntegerField('Number of people', validators=[
                           Required(),NumberRange(max=100)], default="0")
    date = DateField('Event Date', validators=[Required(),DateRange(min=date.today())],format = '%Y-%m-%d')
    category = SelectField(u'Select Category', choices=[('1', 'Sports'),('2', 'Entertainment'), ('3', 'Adventure'), ('4', 'Fun')])
    event_desc = TextAreaField('Event Description')
    submit = SubmitField('Create Event')


class editEventForm(FlaskForm):

    title = StringField('Event Name', validators=[Required()])
    location = StringField('Event location', validators=[Required()])
    persons = IntegerField('Number of people', validators=[Required()])
    date = DateField('Event Date', validators=[Required(),DateRange(min=date.today())],format = '%Y-%m-%d')
    category = SelectField(u'Programming Language', choices=[('1', 'Sports'),('2', 'Entertainment'), ('3', 'Adventure'), ('4', 'Fun')])
    event_desc = TextAreaField('Event Description')
    submit = SubmitField('Submit')

