from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from hashlib import md5




        # def is_authenticated(self):
        #     return True
        #
        # def is_active(self):
        #     return True
        #
        # def is_anonymous(self):
        #     return False
        #
        # def get_id(self):
        #     try:
        #         return unicode(self.id)
        #     except NameError:
        #         return  str(self.id)
        #
        # def __repr__(self):
        #     return '<User % r>' % self.nickname
        #
        # def avatar(self, size):
        #     return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)
        #
        # @staticmethod
        # def make_unique_nickname(nickname):
        #     if User.query.filter_by(nickname=nickname).first() is None:
        #         return nickname
        #     version = 2
        #     while True:
        #         new_nickname = nickname + str(version)
        #         if User.query.filter_by(nickname=new_nickname).first() is None:
        #             break
        #         version += 1
        #     return new_nickname


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post %r>' % (self.body)

#
# class Bids(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     auction_id = db.Column(db.String(120))
#     bdPrice = db.Column(db.Integer, index=True)
#     user_id = db.Column(db.String(120))
#
#
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120))
#     publisher = db.Column(db.String(120))
#     year = db.Column(db.Integer)
#     subject = db.Column(db.String(120))
#
#
# class Auctions(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     book_id = db.Column(db.Integer)
#     start = db.Column(db.DateTime)
#     end = db.relationship(db.DateTime)
#     user_id = db.Column(db.String(120))
#     min_price = db.Column(db.Float)
#     bid_id = db.Column(db.Integer)
#
#
# class Schools(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(150))
#     city = db.Column(db.String(150))
#     province = db.Column(db.String(150))
