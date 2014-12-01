from flask import Blueprint, session, redirect, url_for, request, render_template, flash
from sqlalchemy import func
from app import db
from app.mod_auction.forms import BidForm
from app.mod_member.forms import UploadBookForm
from app.models import Book, Bid, User, Auction

mod_auction = Blueprint('auction', __name__, url_prefix='/auction')


# Sign up - Registration for new users
@mod_auction.route('/book/<bookID>', methods=['GET', 'POST'])
def book(bookID):
    form = BidForm()
    bookS = db.session.query(Book).filter(Book.book_id == bookID).scalar()
    print(str(db.session.query(Book).filter(Book.book_id == bookID).as_scalar()))
    aucID = db.session.query(Auction.auc_id).filter(Auction.book_id == bookID).scalar()
    print(str(db.session.query(Auction.auc_id).filter(Auction.book_id == bookID).as_scalar()))
    curPrice = db.session.query(func.max(Bid.bid_price)).filter(Bid.auc_id == aucID).scalar()
    print(str(db.session.query(func.max(Bid.bid_price)).filter(Bid.auc_id == aucID).as_scalar()))
    if request.method == 'POST':
        if not form.validate():
            flash('Bid Unsuccessful')
            return render_template('auction/book.html', form=form, book=bookS, curPrice=curPrice)
        else:
            if 'email' not in session:
                return redirect(url_for('auth.signin'))
            else:
                usrID = db.session.query(User.user_id).filter(User.email == session['email']).scalar()
                highBid = db.session.query(Bid.bid_price).filter(Bid.auc_id == aucID).\
                    filter(Bid.bid_price >= form.bid_price.data).first()
                if highBid:
                    flash('Your bid needs to be higher then the current price')
                    return render_template('auction/book.html', form=form, book=bookS, curPrice=curPrice)
                else:
                    newBid = Bid(auc_id=aucID, user_id=usrID, bid_price=form.bid_price.data)
                    db.session.add(newBid)
                    db.session.commit()
                    flash('Bid Successful')
                return render_template('auction/book.html', form=form, book=bookS, curPrice=form.bid_price.data)
    
    elif request.method == 'GET':
        return render_template('auction/book.html', form=form, book=bookS, curPrice=curPrice)


