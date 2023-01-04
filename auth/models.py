from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

Base = db.Model


class User(UserMixin, Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    dob = db.Column(db.Integer, unique=False, nullable=False)

    # add user roles to differentiate between admin, quizzer, spectator, etc.

