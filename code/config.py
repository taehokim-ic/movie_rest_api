from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

TESTING = True
DEBUG = True
FLASK_ENV = 'development'
SQLALCHEMY_DATABASE_URI = 'sqlite:///movie.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = environ.get('SECRET_KEY')
