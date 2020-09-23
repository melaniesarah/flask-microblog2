import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    '''
    The SQLALCHEMY_TRACK_MODIFICATIONS configuration option is set to False to disable the feature of Flask-SQLAlchemy 
    that signals the app every time a change is about to be made in the database.
    '''