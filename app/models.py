from werkzeug.security import generate_password_hash, check_password_hash
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
    book_id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.Integer)
    title = db.Column(db.String(120))
    volume = db.Column(db.Integer)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))
    year = db.Column(db.Integer)
    subject = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    auc_id = db.relationship('Auction', backref='book', lazy='dynamic')

    def __init__(self, isbn, title, volume, author, publisher, year, subject, user_id):
        self.isbn = isbn
        self.title = title.title()
        self.volume = volume
        self.author = author.title()
        self.publisher = publisher
        self.year = year
        self.subject = subject
        self.user_id = user_id


class Auction(db.Model):
    auc_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    highest_bid = db.relationship('Bid', backref='auction', lazy='dynamic')

    def __init__(self, book_id, start_time, end_time):
        self.book_id = book_id
        self.start_time = start_time
        self.end_time = end_time


class Bid(db.Model):
    bid_id = db.Column(db.Integer, primary_key=True)
    auc_id = db.Column(db.Integer, db.ForeignKey('auction.auc_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    bid_price = db.Column(db.Integer)

    def __init__(self, auc_id, user_id, bid_price):
        self.auc_id = auc_id
        self.user_id = user_id
        self.bid_price = bid_price