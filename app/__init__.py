from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.api import FlaskAPI


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = FlaskAPI(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import modules and components from blueprints
from app.mod_auth.controllers import mod_auth as auth_module
from app.mod_public.controllers import mod_public as public_module
from app.mod_member.controllers import mod_member as member_module
from app.mod_auction.controllers import mod_auction as auction_module


# Register blueprints
app.register_blueprint(auth_module)
app.register_blueprint(public_module)
app.register_blueprint(member_module)
app.register_blueprint(auction_module)
