from flask import Blueprint, session, redirect, url_for, request, render_template, flash
from app import db
from app.mod_auction.forms import BidForm
from app.mod_member.forms import UploadBookForm
from app.models import Book, Bid, User

mod_auction = Blueprint('auction', __name__, url_prefix='/auction')


# Sign up - Registration for new users
@mod_auction.route('/book/<bookID>', methods=['GET', 'POST'])
def book(bookID):
    form = BidForm()
    bookS = db.session.query(Book).filter(Book.book_id == bookID).scalar()
    if request.method == 'POST':
        if not form.validate():
            flash('Bid Unsuccessful')
            return render_template('auction/book.html', form=form, book=bookS)
        else:
            aucID = db.session.query(Book.auc_id).filter(Book.book_id == bookID).scalar()
            usrID = db.session.query(User.user_id).filter(User.email == session['email']).scalar()
            newBid = Bid(auc_id=aucID, user_id=usrID, bid_price=form.bid_price.data)
            db.session.add(newBid)
            db.session.commit()
            flash('Bid Successful')
            return render_template('auction/book.html', form=form, book=bookS)
    
    elif request.method == 'GET':
        return render_template('auction/book.html', form=form, book=bookS)


