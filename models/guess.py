from. import db

class Guess(db.Model):
    __tablename__="guesses"
    id = db.Column(db.Integer, primary_key =True)
    guess = db.Column(db.String)
    num_match = db.Column(db.Integer)
    exact_match = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"), nullable = False)
    player = db.relationship("Player", back_populates="guesses")
    game = db.relationship("Game", back_populates="guesses")