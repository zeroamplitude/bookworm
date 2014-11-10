# from flask import Blueprint, session, redirect, url_for, request, render_template
# from app import db
# from app.mod_auction.forms import Bid
#
# mod_auth = Blueprint('auth', __name__, url_prefix='/auth')
#
#
# # Sign up - Registration for new users
# @mod_auth.route('/signup/', methods=['GET', 'POST'])
# def signup():
#     form = Bid()
#
#     if 'email' in session:
#         return redirect(url_for('member.profile'))
#
#     if request.method == 'POST':
#         if not form.validate():
#             return render_template('auth/signup.html', form=form)
#         else:
#             # << SQL >>
#             # INSERT INTO users (firstname, lastname, email, pwdhash)
#             # VALUES (form.firstname.data, form.lastname.data, form.email.data, form.password.data)
#             newBid = Bid(form.bidPrice.data, , form.email.data, form.password.data)
#             db.session.add(newBid)
#             db.session.commit()
#
#             return redirect(url_for('member.profile'))
#
#     elif request.method == 'GET':
#         return render_template('auth/signup.html', form=form)

