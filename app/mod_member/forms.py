from flask import session, g
from flask_wtf import Form
from wtforms import IntegerField, validators, StringField, SubmitField
from app import db
from app.models import User


class UploadBookForm(Form):
    isbn = IntegerField("ISBN", [validators.DataRequired("Please enter the ISBN number.")])
    title = StringField("Title", [validators.DataRequired("Please enter the book's title.")])
    # volume = IntegerField("Vol.")
    author = StringField("Author", [validators.DataRequired("Please enter the book's author")])
    # publisher = StringField("Publisher")
    # year = IntegerField("Year")
    # subject = StringField("Subject")
    user_id = g.user
    submit = SubmitField("Upload Book")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

