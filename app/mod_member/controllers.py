from flask import session, url_for, redirect, render_template, Blueprint
from app.mod_auth.models import User

mod_member = Blueprint('member', __name__, url_prefix='/member')


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