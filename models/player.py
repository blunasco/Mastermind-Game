from . import db

class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    gender = db.Column(db.String)
    games = db.relationship("Game", back_populates="player", cascade="all, delete-orphan")
    guesses = db.relationship("Guess", back_populates="player")



