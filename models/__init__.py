from flask_sqlalchemy import SQLAlchemy

# create db once
db = SQLAlchemy()

# import models AFTER db is defined
from .player import Player
from .game import Game
from .guess import Guess

__all__ = ["db", "Game", "Player","Guess"]
