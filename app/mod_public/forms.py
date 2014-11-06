from flask_wtf import Form
from wtforms import StringField, validators, TextAreaField, SubmitField


class ContactForm(Form):
    name = StringField("Name", [validators.DataRequired("Please enter your name")])
    email = StringField("Email", [validators.DataRequired("Please enter you email"),
                                  validators.Email("Please enter a  valid email")])
    subject = StringField("Subject", [validators.DataRequired("Please enter a subject")])
    message = TextAreaField("Message", [validators.DataRequired("Please enter your message")])
    submit = SubmitField("Send")


class SearchForm(Form):
    title = StringField("Title")
    submit =SubmitField("Search")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)