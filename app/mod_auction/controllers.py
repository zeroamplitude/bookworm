from flask import Blueprint, session, redirect, url_for, request, render_template
from app import db
from app.mod_auction.forms import Bid
from app.models import Book

mod_auction = Blueprint('auction', __name__, url_prefix='/auction')


# Sign up - Registration for new users
@mod_auction.route('/book/', methods=['GET', 'POST'])
def book(bookID=3):
    form = Bid()

    if request.method == 'POST':
        if not form.validate():
            return render_template('auction/book.html', form=form)
        else:
            newBid = Bid(form.bidPrice.data)
            db.session.add(newBid)
            db.session.commit()

            return render_template('auction/book.html', form=form)
    
    elif request.method == 'GET':
        bookS = db.session.query(Book).filter(Book.book_id==bookID)
        return render_template('auction/book.html', form=form, book=bookS)

