from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
'''
The bottom import is a workaround to circular imports, a common problem with Flask applications.
The routes module needs to import the app variable defined in this script, so putting one of the
reciprocal imports at the bottom avoids the error that results from the mutual references between
these two files.
'''