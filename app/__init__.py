from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import modules and components from blueprints
from app.mod_auth.controllers import mod_auth as auth_module
from app.views import home


# Register blueprints
app.register_blueprint(auth_module)

