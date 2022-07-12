from db import db

class MovieGenreModel(db.Model):
    
    __tablename__ = "movieGenre"
    GENRE_CHAR_LIMIT = 40
    
    uid = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    genre = db.Column(db.String(GENRE_CHAR_LIMIT), nullable=False)
    
    _movie = db.relationship('MovieModel', back_populates='_movieGenre')
    
    def __init__(self, movie_id: int, genre: str) -> None:
        self.movie_id = movie_id
        self.genre = genre
        
    @classmethod
    def find_by_movie_id(cls, _movie_id: int):
        return cls.query.filter_by(movie_id=_movie_id)
    
    @classmethod
    def find_by_movie_id_and_genre(cls, _movie_id: int, _genre: str):
        return cls.query.filter_by(movie_id=_movie_id, genre=_genre)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()