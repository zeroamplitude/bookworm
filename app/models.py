from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, index=True, primary_key=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(54))
    books = db.relationship('Book', backref='user', lazy='dynamic')
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

    def get_id(self):
        try:
            return unicode(self.user_id)  # python 2
        except NameError:
            return str(self.user_id)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.Integer)
    title = db.Column(db.String(120))
    # volume = db.Column(db.Integer)
    author = db.Column(db.String(120))
    # publisher = db.Column(db.String(120))
    # year = db.Column(db.Integer)
    # subject = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __init__(self, isbn, title, author, user_id):
        self.isbn = isbn
        self.title = title.title()
        self.author = author.title()
        self.user_id = user_id
