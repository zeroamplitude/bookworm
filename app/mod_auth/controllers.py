from flask import Blueprint, session, redirect, url_for, render_template, request, g
from app import db
from app.models import User
from app.mod_auth.forms import SigninForm, SignupForm

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


# Sign up - Registration for new users
@mod_auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if 'uID' in session:
        return redirect(url_for('member.profile'))

    if request.method == 'POST':
        if not form.validate():
            return render_template('auth/signup.html', form=form)
        else:
            # << sql >>
            # INSERT INTO users (firstname, lastname, email, pwdhash)
            # VALUES (form.firstname.data, form.lastname.data, form.email.data, form.password.data)
            newuser = User(form.fname.data, form.lname.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['uID'] = newuser.user_id
            session['email'] = newuser.email
            return redirect(url_for('member.profile'))

    elif request.method == 'GET':
        return render_template('auth/signup.html', form=form)


# Sign in - Existing member sign in
@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = SigninForm()

    if 'uID' in session:
        return redirect(url_for('member.profile'))

    if request.method == 'POST':
        if not form.validate():
            return render_template('auth/signin.html', form=form)
        else:
            session['uID'] = User.user_id
            session['email'] = User.email
            return redirect(url_for('member.profile'))
    elif request.method == 'GET':
        return render_template('auth/signin.html', form=form)


# Log out - Exit's the user session
@mod_auth.route('/logout')
def logout():
    if 'uID' not in session:
        return redirect(url_for('auth.signin'))

    session.pop('uID', None)
    return redirect(url_for('public.home'))