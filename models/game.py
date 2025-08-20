
from sqlalchemy import JSON
from . import db
from datetime import datetime
from models.guess import Guess

class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(JSON, nullable=False) #stored as [1,2,3,4]
    status = db.Column(db.String)
    rounds_allowed = db.Column(db.Integer, default=10) 
    rounds_used = db.Column(db.Integer, default=0) 
    player_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    player = db.relationship("Player", back_populates="games")
    guesses = db.relationship("Guess", back_populates="game")

   

