from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, IntegerField,SelectField
from wtforms.validators import Required
from wtforms import DateField


class createEventForm(FlaskForm):

    title = StringField('Event Name', validators=[Required()],default = "Event Name")
    location = StringField('Event location', validators=[Required()], default="Event Name")
    persons = IntegerField('Number of people', validators=[
                           Required()], default="Event Name")
    date = DateField('Event Date', format='%Y-%m-%d', validators=[Required()])
    event_desc = TextAreaField('Event Description')
    submit = SubmitField('Create Event')


class editEventForm(FlaskForm):

    title = StringField('Event Name', validators=[Required()])
    location = StringField('Event location', validators=[Required()])
    persons = IntegerField('Number of people', validators=[Required()])
    date = DateField('Event Date', format='%Y-%m-%d', validators=[Required()])
    event_desc = TextAreaField('Event Description')
    submit = SubmitField('Submit')

