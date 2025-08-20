from flask import jsonify
from models import db, Game, Guess


class GameSession():
    def __init__(self, id: int):
        #fetch the game row from db and store eit in self.game
        self.game = Game.query.get(id)

        #validate game
        if not self.game:
            raise ValueError ("Game id: {id} not found.")
        

    def check_player_guess(self, guess: list):
        try:
            guess = self.validate_guess(guess)

            #validate game
            if self.game.status != 'IN_PROGRESS':
                return 'Try again this game is not in progress!' 
            
                
            #count matches
            else:
                    matches = self.count_matches(guess)
                    exact_match = matches["exact_match"]
                    num_match = matches['num_match']
                    #update rounds and status
                    self.update_rounds()
                    self.update_status(exact_match)
                    self.add_guess(guess,num_match, exact_match)
                    
                    db.session.commit()

                
            return jsonify({
                "game_id": self.game.id,
                "exact_match": exact_match,
                "num_match": num_match,
                "rounds_used": self.game.rounds_used,
                "status": self.game.status,
                "code": self.game.code
            })
        
        except ValueError as e:
            return {"error":str(e)} 

#HELPER FUNCTIONS
    def validate_guess(self, guess):
        #validate guesslength
        if len(guess) != len(self.game.code):
            raise ValueError (f'Try again with {len(self.game.code)} digits')
        #validate guess characters
        for digit in guess:
            if not str(digit).isdigit():
                raise ValueError("Please enter only numbers betweeen 0 and 7.")
            if digit < 0 or digit > 7:
                raise ValueError("Each digit must be between 0 and 7.")
        return guess
     
    
    def count_matches(self, guess: list) -> tuple[int, int]:
        code = self.game.code
        exact_match = 0

        code_counts = {}
        guess_counts = {}

        for i in range(len(code)):
            if code[i] == guess[i]:
                exact_match += 1
            else:
                code_counts[code[i]] = code_counts.get(code[i], 0) + 1
                guess_counts[guess[i]] = guess_counts.get(guess[i], 0) + 1

        # count all correct numbers (including exacts)
        num_match = exact_match
        for num in guess_counts:
            if num in code_counts:
                num_match += min(code_counts[num], guess_counts[num])

        return {
            "exact_match": exact_match,
            "num_match": num_match
        }
    def update_rounds(self):
        self.game.rounds_used += 1

    def update_status (self, exact_match:int) -> str:
        if exact_match == 4:
            self.game.status = 'WON'
        elif self.game.rounds_used >= self.game.rounds_allowed:
            self.game.status ='LOST' 
        else: 
            self.game.status ='IN_PROGRESS'
        return self.game.status        
    
    def add_guess (self, guess, exact_match, num_match):
        new_guess = Guess(
            player_id =self.game.player_id,
            game_id = self.game.id,
            guess_data = self.guess,
            num_match = self.num_match,
            exact_match = self.exact_match
        )

        db.session(new_guess)
        db.session.commit()

        return new_guess
