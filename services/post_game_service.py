from flask import jsonify
from models import db, Game, Player

class GameResult:
    def __init__(self, id: int):
        #fetch the game row from db and store eit in self.game
        self.game = Game.query.get(id)

        #validate game
        if not self.game:
            raise ValueError ("Game id: {id} not found.")
    def end_game(self, id:int):
        game = self.gather_results(id)


        return jsonify ({
            "status": self.game.status,
            "rounds_used": self.game.rounds_used,
            "code": self.game.code,
            "guesses": [], #to add later
            "message": self.gather_results(self.game.status)})

    def gather_results(self, status):
        if self.game.status == 'WON':
            return "Congratulations, you won!"
        if self.game.status == 'LOST':
            return "Better luck next time!"
        else:
            return "Game in progress."


        