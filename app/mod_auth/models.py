from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, index=True, primary_key=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(54))
    # posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    def __init__(self, fname, lname, email, password):
        self.fname = fname.title()
        self.lname = lname.title()
        self.email = email.lower()
        self.set_password(password)

        # << password hash not implemented >>
    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)
