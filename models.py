from flask_sqlalchemy import SQLAlchemy

from settings import db
# Create user table
class Users(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), nullable=False)
  password = db.Column(db.String(120), nullable=False)
  task = db.relationship('Tasks', backref='tasks', lazy=True)


class Tasks(db.Model):
  __tablename__ = 'tasks'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  title = db.Column(db.String(120), nullable=False)
  due = db.Column(db.String(120), nullable=False)
  task = db.Column(db.String(500), nullable=False)