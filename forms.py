from flask_wtf import Form
from wtforms import StringField, TextAreaField, validators


class ContactForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    email = StringField('email Address', [validators.DataRequired(), validators.Email('email@example.com')])
    message = TextAreaField('How can I help?', [validators.DataRequired()])