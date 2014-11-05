import os

basedir = os.path.abspath(os.path.dirname(__file__))


# Database connections
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'bookworm.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# Application threads
THREADS_PER_PAGE = 2


# Enable protection agains *Cross-site Request Forgery (CSRF)*
WTF_CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"


# Secret key for signing cookies
SECRET_KEY = 'beastMode'


# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None


# admin list
ADMINS = ['nicholas.desouza@uoit.net']