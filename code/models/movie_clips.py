from db import db

class MovieClipsModel(db.Model):
    
    __tablename__ = "movieClips"
    LINK_CHAR_LIMIT = 512
    
    uid = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    link = db.Column(db.String(LINK_CHAR_LIMIT))
    
    _movie = db.relationship('MovieModel', back_populates='_movieClips')
    
    def __init__(self, movie_id: int, link: str) -> None:
        self.movie_id = movie_id
        self.link = link
        
    @classmethod
    def find_by_movie_id(cls, _movie_id: int):
        return cls.query.filter_by(movie_id=_movie_id)
        
    @classmethod
    def find_by_movie_id_and_link(cls, _movie_id: int, _link: str):
        return cls.query.filter_by(movie_id=_movie_id, link=_link) 
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()