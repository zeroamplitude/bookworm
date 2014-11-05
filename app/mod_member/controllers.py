from flask import Blueprint, session, url_for, redirect, render_template, request, g, flash
from app import db
from app.mod_member.forms import PostBookForm
from app.models import User, Book
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from config import SQLALCHEMY_DATABASE_URI

mod_member = Blueprint('member', __name__, url_prefix='/member')
engine = create_engine(SQLALCHEMY_DATABASE_URI)
conn = engine.connect()

# Profile -
@mod_member.route('/profile/')
def profile():
    if 'email' not in session:
        return redirect(url_for('auth.signin'))

        # << SQL >>
        # SELECT * FROM users WHERE email = session['email'];
    user = User.query.filter_by(email=session['email']).first()

    if user is None:
        return redirect(url_for('auth.signin'))
    else:
        #uid = db.session.query(User.user_id).filter_by(User.email == user)
        # s = select(
        #     [
        #         Book.title,
        #         Book.isbn,
        #         Book.author
        #     ]
        # ).where(
        #     and_(
        #         Book.user_id == User.user_id,
        #         User.email == user
        #     )
        # )
        # books = conn.execute(s)
        books = User.query.filter_by(email=session['email']).join(Book)
            #db.session.query(Book.isbn)
        return render_template('member/profile.html', books=books)


@mod_member.route('/postbook', methods=['GET', 'POST'])
def postbook():
    form = PostBookForm

    if 'email' not in session:
        return redirect(url_for('auth.signin'))

    if request.method == 'POST':
        book = Book(isbn=form.isbn.data, title=form.title.data, volume=form.volume,
                    author=form.author.data, publisher=form.publisher.data, year=form.year.data)
        db.session.add(book)
        db.session.commit()