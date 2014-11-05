from flask_wtf import Form
from wtforms import IntegerField, validators, StringField


class PostBookForm(Form):
    isbn = IntegerField("ISBN", [validators.DataRequired("Please enter the ISBN number.")])
    title = StringField("Title", [validators.DataRequired("Please enter the book's title.")])
    volume = IntegerField("Vol.")
    author = StringField("Author", [validators.DataRequired("Please enter the book's author")])
    publisher = StringField("Publisher")
    year = IntegerField("Year")
    subject = StringField("Subject")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)



