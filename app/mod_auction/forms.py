from flask_wtf import Form
from wtforms import StringField, validators, PasswordField, SubmitField, IntegerField
from app.models import User, Auction


class BidForm(Form):
    bid_price = IntegerField("Bid", [validators.DataRequired("Please enter the ISBN number.")])
    submit = SubmitField("Bid")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    # Validates email to ensure uniqueness
    # def validate(self):
    #     if not Form.validate(self):
    #         return False
    #     highBid = Auction.query.filter(Auction.auc_id == .filter_by(highBid=self.bidPrice.data).scalar()
    #     if user:
    #         self.email.errors.append("That email address is already taken")
    #         return False
    #     else:
    #         return True
