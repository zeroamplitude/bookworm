from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators
from app.models import User


# Sign up - Form to allow users to sign up
class SignupForm(Form):
    fname = StringField("First name", [validators.DataRequired("Please enter your  first name.")])
    lname = StringField("Last name", [validators.DataRequired("Please enter your  last name.")])
    password = PasswordField('Password', [validators.DataRequired("Please enter a password.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address"),
                                  validators.Email("Please enter a valid email address.")])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    # Validates email to ensure uniqueness
    def validate(self):
        if not Form.validate(self):
            return False
        # << sql >>
        # SELECT * FROM users
        # WHERE email = self.email.data.lower()
        # LIMIT 1
        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email address is already taken")
            return False
        else:
            return True


class SigninForm(Form):
    email = StringField('Email', [validators.DataRequired("Please enter your email"),
                                  validators.Email("Please enter a valid email")])
    password = PasswordField('Password', [validators.DataRequired("Please enter your password")])
    # remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.email.errors.append("Invalid e-mail or password")
            return False
