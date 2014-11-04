from flask import Flask, render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required

from app import app, db, lm, oid
from forms import LoginForm, ContactForm, EditForm, SignupForm
from models import User
from datetime import datetime



@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


# Test DB
@app.route('/testdb')
def testdb():
    if db.session.query("1").from_statement("SELECT 1").all():
        return 'It works.'
    else:
        return 'Something is broken.'

# Home - Home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# About - Provides basic information about bookworm
@app.route('/about')
def about():
    return render_template('about.html')

# Contact - Allows user to contact web admin
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            # << Mail method not implemented >>
            return 'Form posted.'
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

# Sign up - Registration for new users
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        if not form.validate():
            return render_template('signup.html', form=form)
        else:
            # << SQL >>
            # INSERT INTO users (firstname, lastname, email, pwdhash)
            # VALUES (form.firstname.data, form.lastname.data, form.email.data, form.password.data)
            newuser = User(form.fname.data, form.lname.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['email'] = newuser.email
            return redirect(url_for('profile'))

    elif request.method == 'GET':
        return render_template('signup.html', form=form)

@app.route('/profile')
def profile():

    if 'email' not in session:
        return redirect(url_for('signin'))

    # << SQL >>
    # SELECT * FROM users WHERE email = session['email'];
    user = User.query.filter_by(email = session['email']).first()

    if user is None:
        return redirect(url_for('signin'))
    else:
        return render_template('profile.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',
                           user=user,
                           posts=posts)

@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm(g.user.nickname)
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('edit'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)
