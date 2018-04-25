from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, IntegerField,SelectField
from wtforms.validators import Required


class createEventForm(FlaskForm):

    title = StringField('Event Name', validators=[Required()],default = "Event Name")
    location = StringField('Event location', validators=[Required()], default="Event Location")
    persons = IntegerField('Number of people', validators=[
                           Required()], default="Number of Persons")
    date = DateField('Event Date', validators=[Required()])
    category = SelectField(u'Select Category', choices=[('1', 'Sports'),('2', 'Entertainment'), ('3', 'Adventure'), ('4', 'Fun')])
    event_desc = TextAreaField('Event Description')
    submit = SubmitField('Create Event')


class editEventForm(FlaskForm):

    title = StringField('Event Name', validators=[Required()])
    location = StringField('Event location', validators=[Required()])
    persons = IntegerField('Number of people', validators=[Required()])
    date = DateField('Event Date', validators=[Required()])
    category = SelectField(u'Programming Language', choices=[('1', 'Sports'),('2', 'Entertainment'), ('3', 'Adventure'), ('4', 'Fun')])
    event_desc = TextAreaField('Event Description')
    submit = SubmitField('Submit')

