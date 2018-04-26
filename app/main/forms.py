from flask_wtf import FlaskForm
from wtforms import  BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import Event

class JoinForm(FlaskForm):
    confirm=BooleanField('Join this event')
    submit=SubmitField('Confirm')
