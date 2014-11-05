from wtforms import StringField, TextAreaField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

from flask.ext.wtf import Form
from mod_auth.models import User


class ContactForm(Form):
    name = StringField("Name", [validators.DataRequired("Please enter your name")])
    email = StringField("Email", [validators.DataRequired("Please enter you email"),
                                  validators.Email("Please enter a  valid email")])
    subject = StringField("Subject", [validators.DataRequired("Please enter a subject")])
    message = TextAreaField("Message", [validators.DataRequired("Please enter your message")])
    submit = SubmitField("Send")


class EditForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True