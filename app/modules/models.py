from flask import Blueprint

blueprint = Blueprint('public', __name__)

@blueprint.route('/')
def home():
    return render_template('public/home.html')
