
from sqlalchemy import JSON
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# create db once
db = SQLAlchemy()
class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(JSON, nullable=False) #stored as [1,2,3,4]
    status = db.Column(db.String)
    rounds_allowed = db.Column(db.Integer, default=10) 
    rounds_used = db.Column(db.Integer, default=0) 
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    player = db.relationship("Player", back_populates="games")
    guesses = db.relationship("Guess", back_populates="game")

   
class Guess(db.Model):
    __tablename__="guesses"
    id = db.Column(db.Integer, primary_key =True)
    guess = db.Column(JSON)
    num_match = db.Column(db.Integer)
    exact_match = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"), nullable = False)
    player = db.relationship("Player", back_populates="guesses")
    game = db.relationship("Game", back_populates="guesses")

class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    gender = db.Column(db.String)
    games = db.relationship("Game", back_populates="player", cascade="all, delete-orphan")
    guesses = db.relationship("Guess", back_populates="player")


