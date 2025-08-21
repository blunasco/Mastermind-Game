from models import Game, Guess


class GameResult:

    def end_game(self, data):

        #fetch the game row from db and store eit in self.game
        id = data.get("id")
        self.game = Game.query.get(id)

        #validate game
        if not self.game:
            raise ValueError (f"Game id: {id} not found.")

        guesses, message = self.gather_results()
       
        return {
            "status": self.game.status,
            "rounds_used": self.game.rounds_used,
            "guesses": guesses,
            "message": message
        }

    def gather_results(self):
        guesses = Guess.query.filter_by(game_id=self.game.id).all()

        guess_list = []
        for guess in guesses:
            guess_list.append({
                "guess": guess.guess,       
            })

        if self.game.status == 'WON':
            message =  "Congratulations, you won!"
        elif self.game.status == 'LOST':
            message ="Better luck next time!"
        else:
            message = "Game in progress."

        return  guess_list, message
