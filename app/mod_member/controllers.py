from flask import session, url_for, redirect, render_template, Blueprint, request
from app import db
from app.mod_member.forms import PostBookForm
from app.models import User #, User

mod_member = Blueprint('member', __name__, url_prefix='/member')

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
        return render_template('member/profile.html')


# @mod_member.route('/books', method=['GET', 'POST'])
# def postbook():
#     form = PostBookForm
#
#     if 'email' not in session:
#         return redirect(url_for('auth.signin'))
#
#     if request.method == 'POST':
#         book = Book(isbn=form.isbn.data, title=form.title.data, volume=form.volume,
#                     author=form.author.data, publisher=form.publisher.data, year=form.year.data)
#         db.session.add(book)