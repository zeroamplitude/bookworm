from flask import Flask
import os
from sqlalchemy import create_engine, MetaData


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
engine = create_engine('postgresql+psycopg2://bookworm:bookworm@localhost/bookworm')
metadata = MetaData(bind=engine)

print os.environ['APP_SETTINGS']

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
