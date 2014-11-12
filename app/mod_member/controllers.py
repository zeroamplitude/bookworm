from datetime import datetime
from flask import Blueprint, session, url_for, redirect, render_template, request, g
from sqlalchemy import null
from app import db
from app.mod_member.forms import UploadBookForm
from app.models import User, Book, Auction


mod_member = Blueprint('member', __name__, url_prefix='/member')

@mod_member.before_request
def before_request():
    g.user = User.user_id

# Profile -
@mod_member.route('/profile/')
def profile():
    if 'email' not in session:
        return redirect(url_for('auth.signin'))

        # << sql >>
        # SELECT * FROM users WHERE email = session['email'];
    user = User.query.filter_by(email=session['email']).first()
    print user

    if user is None:
        return redirect(url_for('auth.signin'))
    else:
        books = db.session.query(Book). \
            filter(User.email == session['email']). \
            filter(Book.user_id == User.user_id)
        g.user_id = User.user_id
        return render_template('member/profile.html', books=books)


@mod_member.route('/newbook/', methods=['GET', 'POST'])
def newbook():
    form = UploadBookForm()

    if 'email' not in session:
        return redirect(url_for('auth.signin'))

    if request.method == 'POST':
        uid = db.session.query(User.user_id).filter(User.email == session['email']).scalar()
        book = Book(isbn=form.isbn.data, title=form.title.data, volume=form.volume.data,
                    author=form.author.data, publisher=form.publisher.data, year=form.year.data,
                    subject=form.subject.data, user_id=uid)
        db.session.add(book)
        db.session.commit()

        auction = Auction(book_id=book.book_id, start_time=datetime.now(), end_time=form.endDate.data)
        db.session.add(auction)
        db.session.commit()

        return redirect(url_for('member.profile'))

    elif request.method == 'GET':
        return render_template('member/newbook.html', form=form)


@mod_member.route('/connect/')
def connect():
    return render_template('member/connect.html')



def setGuser():
    User.user_id = g.user


