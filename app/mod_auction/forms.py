from flask_wtf import Form
from wtforms import StringField, validators, PasswordField, SubmitField, IntegerField
from app.models import User, Auction, Bid


class BidForm(Form):
    bid_price = IntegerField("Bid", [validators.DataRequired("Please enter the ISBN number.")])
    submit = SubmitField("Bid")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    # Validates bid to ensure it is the highest
    # def validate(self):
    #     if not Form.validate(self):
    #         return False
    #     highBid = Bid.query.filter(Bid.auc_id == B.filter_by(highBid=self.bidPrice.data).scalar()
    #     if user:
    #         self.email.errors.append("That email address is already taken")
    #         return False
    #     else:
    #         return True
