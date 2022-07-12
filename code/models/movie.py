from db import db

class MovieModel(db.Model):
    
	__tablename__ = "movies"
	TITLE_CHAR_LIMIT = 120
	NAME_CHAR_LIMIT = 40

	movie_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(TITLE_CHAR_LIMIT), nullable=False)
	year = db.Column(db.Integer, nullable=False)
	original_title = db.Column(db.String(TITLE_CHAR_LIMIT), nullable=True)
	running_time = db.Column(db.Integer, nullable=False)
	director = db.Column(db.String(NAME_CHAR_LIMIT), nullable=False)
	summary = db.Column(db.Text, nullable=True)
	
	_movieClips = db.relationship('MovieClipsModel', lazy='dynamic', back_populates='_movie')
	_movieGenre = db.relationship('MovieGenreModel', lazy='dynamic', back_populates='_movie')
	_actorsPlayed = db.relationship('ActorPlayedModel', lazy='dynamic', back_populates='_movie')
	
	def __init__(self, movie_id, title, year, original_title, running_time, director, summary):
     
		self.movie_id = movie_id
		self.title = title
		self.year = year
		self.original_title = original_title
		self.running_time = running_time
		self.director = director
		self.summary = summary
  
	def  json(self) -> dict:
		return {
			'movie_id': self.movie_id,
			'title': self.title,
			'year': self.year,
			'original_title': self.original_title,
			'genres': [genre.genre for genre in self._movieGenre.all()],
			'running_time': self.running_time,
			'director': self.director,
			'cast': [actor.name for actor in self._actorsPlayed.all()],
			'movie_clips': [clip.link for clip in self._movieClips.all()],
			'summary': self.summary
		}
		
	@classmethod
	def find_by_movie_id(cls, _movie_id):
		return cls.query.filter_by(movie_id=_movie_id).first()

	def save_to_db(self):
		db.session.add(self) 
		db.session.commit()
        
	def delete_from_db(self):
		db.session.delete(self)	
		db.session.commit()
    