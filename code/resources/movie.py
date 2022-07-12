from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.movie_genre import MovieGenreModel
from models.actor_played import ActorPlayedModel
from models.movie_clips import MovieClipsModel
from models.movie import MovieModel

#Resource connected with endpoints
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
                        help="Please enter the genre." 
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
    
    #DONE
    @jwt_required()
    def get(self, movie_id):
        movie = MovieModel.find_by_movie_id(movie_id)
        
        if movie:
            return movie.first().json()
        
        return {'message': f'movid_id {movie_id} not found'}, 404
    
    #DONE
    @jwt_required()
    def post(self, movie_id):
        return {'message': 'HTTP METHODS ALLOWED: [\'GET\', \'DELETE\', \'PUT\']'}, 405
              
    #DONE IF NOT EXISTS           
    @jwt_required()                                        
    def delete(self, movie_id):
        movie = MovieModel.find_by_movie_id(movie_id)
        
        if not movie:
            return {'message': f"movie_id '{movie_id}' does not exist"}, 400

        movie.first().delete_from_db()

        for movie_clips in MovieClipsModel.find_by_movie_id(movie_id).all():
            movie_clips.delete_from_db()
        
        for movie_cast in ActorPlayedModel.find_by_movie_id(movie_id).all():
            movie_cast.delete_from_db()
        
        for movie_genre in MovieGenreModel.find_by_movie_id(movie_id):
            movie_genre.delete_from_db()
        
        return {'message': f'Movie With movie_id {movie_id} Successfully Deleted.'}, 200
    
    #DONE
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
                        type=list[dict],
                        required=True,
                        help="Please enter the movies." 
    )
    
    #DONE
    @jwt_required()
    def get(self):
        return {'movies': [movie.json() for movie in MovieModel.query.all()]}
    
    # @jwt_required()
    # def post(self):
    #     parser = reqparse.RequestParser()
    
    #     parser.add_argument('movies',
    #                     type=dict,
    #                     required=True,
    #                     action='append',
    #                     help="Please enter the movies." 
    #     )
        
    #     data = MovieList.parser.parse_args()
    #     duplicate = []
        
    #     for movie_data in data:
    #         _title = movie_data['title']
    #         _year = movie_data['year']
    #         _original_title = movie_data['original_title']
    #         _running_time = movie_data['running_time']
    #         _director = movie_data['director']
    #         _summary = movie_data['summary']
    #         _genres = movie_data['genres']
    #         _clips = movie_data['movie_clips']
    #         _cast = movie_data['cast']
            
    #         movie = MovieModel.query.filter_by(title=_title, year=_year, director=_director).first()
            
    #         if not movie:
                
    #         else:
    #             duplicate.append(movie.movie_id, _title)
                
                
            
    #     if MovieModel.find_by_movie_id(movid_id): # can still do self.find_by_name
    #         return {'message': f"Item with name '{name}' already exists"}, 400
        
    #     data = MovieList.parser.parse_args()
        
    #     item = ItemModel(name, data['price'], data['store_id'])
    #     try:
    #         item.save_to_db()
    #     except:
    #         return {'message': 'An error occurred inserting the item.'}, 500 #invernal server error
        
    #     return item.json(), 201 #Creating status code, CREATED 
    #                      #202 ACCEPTED when delaying creation
    #                      #When creating takes a long time