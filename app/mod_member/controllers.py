from flask import Blueprint, session, url_for, redirect, render_template, request, g
from app import db
from app.mod_member.forms import UploadBookForm
from app.models import User, Book


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
    #g.user = User.query(User.user_id).filter(User.email == session['email'])
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

        book = Book(isbn=form.isbn.data, title=form.title.data,
                    author=form.author.data, user_id=form.user_id.data)
        db.session.add(book)
        db.session.commit()

    elif request.method == 'GET':
        return render_template('member/newbook.html', form=form)



def setGuser():
    User.user_id = g.user


