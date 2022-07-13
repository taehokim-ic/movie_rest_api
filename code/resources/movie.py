from collections import deque
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.movie_genre import MovieGenreModel
from models.actor_played import ActorPlayedModel
from models.movie_clips import MovieClipsModel
from models.movie import MovieModel

class Movie(Resource):
    parser = reqparse.RequestParser()
    
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help="Please enter the movie title." 
    )
    parser.add_argument('year',
                        type=int,
                        required=True,
                        help="Please enter the release year."
    )
    parser.add_argument('original_title',
                        type=str,
                        required=True,
                        help="Please enter the original title."
    )
    parser.add_argument('genres',
                        type=str,
                        required=True,
                        action='append', 
                        help="Please enter the genres." 
    )
    parser.add_argument('running_time',
                        type=int,
                        required=True, 
                        help="Please enter the running time." 
    )
    parser.add_argument('director',
                        type=str,
                        required=True, 
                        help="Please enter the name of the director." 
    )
    parser.add_argument('cast',
                        type=str,
                        required=True, 
                        action='append',
                        help="Please enter the cast members." 
    )
    parser.add_argument('movie_clips',
                        type=str,
                        required=True,
                        action='append', 
                        help="Please enter the cast members." 
    )
    parser.add_argument('summary',
                        type=str,
                        required=False, 
    )
    
    @jwt_required()
    def get(self, movie_id):
        movie = MovieModel.find_by_movie_id(movie_id)
        
        if movie:
            return movie.json()
        
        return {'message': f'movid_id {movie_id} not found'}, 404
    
    @jwt_required()
    def post(self, movie_id):
        return {'message': 'This method is not allowed for the requested URL.'}, 405
          
    @jwt_required()                                        
    def delete(self, movie_id):
        movie = MovieModel.find_by_movie_id(movie_id)
        
        if not movie:
            return {'message': f"movie_id: {movie_id} does not exist"}, 400

        movie.delete_from_db()
        
        return {'message': f'Movie With movie_id: {movie_id} Successfully Deleted.'}, 200
    
    @jwt_required()
    def put(self, movie_id):
        data = Movie.parser.parse_args()
        
        title = data['title']
        year = data['year']
        original_title = data['original_title']
        running_time = data['running_time']
        director = data['director']
        summary = data['summary']
        genres = data['genres']
        clips = data['movie_clips']
        cast = data['cast']
        
        movie = MovieModel.find_by_movie_id(movie_id)
               
        if not movie:
            movie = MovieModel(movie_id, title, year, original_title, 
                               running_time, director, summary)
            
        else:
            movie.movie_id, movie.title, movie.year, movie.original_title, \
            movie.running_time, movie.director, movie.summary = \
                movie_id, title, year, original_title, running_time, director, summary

        movie.save_to_db()

        for movie_genre in MovieGenreModel.find_by_movie_id(movie_id).all():
                if not movie_genre.genre in genres:
                    movie_genre.delete_from_db()
        
        for genre in genres:
            if not MovieGenreModel.find_by_movie_id_and_genre(movie_id, genre).first():
                MovieGenreModel(movie_id, genre).save_to_db()
        
        for movie_clips in MovieClipsModel.find_by_movie_id(movie_id).all():
                if not movie_clips.link in clips:
                    movie_clips.delete_from_db()
        
        for link in clips:
            if not MovieClipsModel.find_by_movie_id_and_link(movie_id, link).first():
                MovieClipsModel(movie_id, link).save_to_db()
        
        for actor in ActorPlayedModel.find_by_movie_id(movie_id).all():
                if not actor.name in cast:
                    actor.delete_from_db()
        
        for name in cast:
            if not ActorPlayedModel.find_by_movie_id_and_name(movie_id, name).first():
                ActorPlayedModel(movie_id, name).save_to_db()
        
        return movie.json()  
    
class MovieList(Resource):
    parser = reqparse.RequestParser()
    
    parser.add_argument('movies',
                        type=dict,
                        required=True,
                        action='append',
                        help="Please enter the movies." 
    )
    
    @jwt_required()
    def get(self):
        return {'movies': [movie.json() for movie in MovieModel.query.all()]}
    
    @jwt_required()
    def post(self):
        data = MovieList.parser.parse_args()
        
        movies = data['movies']
        
        movie_queue = deque()
        movie_genre_queue = deque()
        movie_clips_queue = deque()
        movie_actor_queue = deque()
        
        movies_created = []
        
        for movie_data in movies:
            try:    
                movie_id = movie_data['movie_id']
                title = movie_data['title']
                year = movie_data['year']
                original_title = movie_data['original_title']
                running_time = movie_data['running_time']
                director = movie_data['director']
                summary = movie_data['summary']
                genres = movie_data['genres']
                clips = movie_data['movie_clips']
                cast = movie_data['cast']
                
            except Exception as inst:
                return {'message': f'Please Enter: {inst.args}.'}, 400
                    
            movie = MovieModel.find_by_movie_id(movie_id)
            
            if movie:
                return {'message': f"Movie With movie_id: {movie_id} Already Exists."}, 409
            
            else:
                movie = MovieModel(movie_id, title, year, original_title, running_time, director, summary)
                
                movie_queue.append(movie)
                
                for actor in cast:
                    movie_actor_queue.append(ActorPlayedModel(movie_id, actor))
                
                for genre in genres:
                    movie_genre_queue.append(MovieGenreModel(movie_id, genre))
                
                for clip in clips:
                    movie_clips_queue.append(MovieClipsModel(movie_id, clip))
                
                movies_created.append(movie)
                
        try:
            while movie_queue:
                movie_queue.popleft().save_to_db()

            while movie_actor_queue:
                movie_actor_queue.popleft().save_to_db()

            while movie_genre_queue:
                movie_genre_queue.popleft().save_to_db()

            while movie_clips_queue:
                movie_clips_queue.popleft().save_to_db()

        except:
            return {'message': 'An error occurred inserting the item.'}, 500 #internal server error

        return {"movies": [movie.json() for movie in movies_created]}, 201