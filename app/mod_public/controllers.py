from flask import render_template, request, Blueprint
from app import mod_public
from app.mod_public.forms import ContactForm

mod_public = Blueprint('public', __name__, url_prefix='/')

# Home - Home page
@mod_public.route('/')
@mod_public.route('home/')
def home():
    return render_template('public/home.html')

# About - Provides basic information about bookworm
@mod_public.route('about/')
def about():
    return render_template('public/about.html')

# Contact - Allows user to contact web admin
@mod_public.route('contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if not form.validate():
            return render_template('public/contact.html', form=form)
        else:
            # << Mail method not implemented >>
            return 'Form posted.'
    elif request.method == 'GET':
        return render_template('public/contact.html', form=form)