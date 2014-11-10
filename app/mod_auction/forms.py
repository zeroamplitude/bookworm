from wtforms import StringField, validators, PasswordField, SubmitField, Form
from app.models import User


class Bid(Form):
    bidPrice = StringField("First name", [validators.DataRequired("Please enter your  first name.")])
    submit = SubmitField("Bid")

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
