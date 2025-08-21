from flask import jsonify
from models import db, Game, Guess

class GameResult:
    def __init__(self, game_id:int):
        #fetch the game row from db and store eit in self.game
        self.game = Game.query.get(game_id)

        #validate game
        if not self.game:
            raise ValueError ("Game id: {id} not found.")
    def end_game(self, id:int, guesses):
        self.gather_results(id)

        return jsonify ({
            "status": self.game.status,
            "rounds_used": self.game.rounds_used,
            "code": self.game.code,
            "guesses": guesses,
            "message": self.gather_results(self.game.status)})

    def gather_results(self, status):
        game_id = self.game.game_id
        guesses = Guess.query.filter_by(game_id=self.game.game_id).all

        if self.game.status == 'WON':
            message =  "Congratulations, you won!"
        if self.game.status == 'LOST':
            message ="Better luck next time!"
        else:
            message = "Game in progress."

        return {"guesses": guesses,
            "message": message }



        