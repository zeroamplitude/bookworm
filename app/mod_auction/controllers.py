from flask import Blueprint, session, redirect, url_for, request, render_template
from app import db
from app.mod_auction.forms import Bid
from app.models import Book

mod_auction = Blueprint('auction', __name__, url_prefix='/auction')


# Sign up - Registration for new users
@mod_auction.route('/book/<bookID>', methods=['GET', 'POST'])
def book(bookID):
    form = Bid()
    bookS = db.session.query(Book).filter(Book.book_id == bookID).scalar()
    if request.method == 'POST':
        if not form.validate():
            return render_template('auction/book.html', books=bookS)
        else:
            newBid = Bid(form.bidPrice.data)
            db.session.add(newBid)
            db.session.commit()

            return render_template('auction/book.html', books=bookS)
    
    elif request.method == 'GET':
        return render_template('auction/book.html', book=bookS)

