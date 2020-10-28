from datetime import datetime
from app import db

posts = db.Table('posts',
		db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
		db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id'), primary_key=True)
		)

class User(db.Model):
	__tablename__ = 'user'
	__mapper_args__ = {'polymorphic_identity': 'user'}
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	role = db.Column(db.String(32), nullable=False)
	__mapper_args__ = {'polymorphic_on': role}
	
	def __repr__(self):
		return '<User {}>'.format(self.username)
		
class Teacher(User):
	__tablename__ = 'teacher'
	__mapper_args__ = {'polymorphic_identity': 'teacher'}
	id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	posts = db.relationship('Post', secondary=posts, lazy='subquery', 
			backref=db.backref('authors', lazy=True))
	
	def __repr__(self):
		return '<Teacher {}>'.format(self.username)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	
	def __repr__(self):
		return '<Post {}>'.format(self.body)