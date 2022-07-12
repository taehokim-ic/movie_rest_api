from db import db

class ActorPlayedModel(db.Model):
    
    __tablename__ = "actorsPlayed"
    ACTOR_CHAR_LIMIT = 80
    
    uid = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    name = db.Column(db.String(ACTOR_CHAR_LIMIT), unique=False, nullable=False)
    
    _movie = db.relationship('MovieModel', back_populates='_actorsPlayed')
    
    def __init__(self, movie_id: int, name: str) -> None:
        self.movie_id = movie_id
        self.name = name

    @classmethod
    def find_by_movie_id(cls, _movie_id: int):
        return cls.query.filter_by(movie_id=_movie_id)
    
    @classmethod 
    def find_by_movie_id_and_name(cls, _movie_id: int, _name: str):
        return cls.query.filter_by(movie_id=_movie_id, name=_name)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()