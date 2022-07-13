from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.movie import Movie, MovieList

from db import db
import config

app = Flask(__name__, instance_relative_config=True)
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'encoding': 'cp1252'}
app.config.from_object(config)

api = Api(app)

# 초반에 movie.db 없으면 생성
@app.before_first_request
def create_tables():
	db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Movie, '/api/v1/movies/<int:movie_id>')
api.add_resource(MovieList, '/api/v1/movies')
api.add_resource(UserRegister, '/api/v1/register')

if __name__ == "__main__":
	db.init_app(app)
	app.run(port=5000)
