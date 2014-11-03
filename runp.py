#!flask/bin/python
from app import app
app.debug=False
app.run(host='192.168.2.146', port=80)
