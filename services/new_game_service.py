from flask import Response, jsonify
import requests, random
from models import db, Game, Player, Guess

class GameInitializer():
    def __init__(self):
        self.code = []
        self.player = None
        self.rounds_allowed = 10
        self.rounds_used = 0
        self.status = "NOT_STARTED"
        self.guess_record = []
   
    from models import db, Game, Player

    def initialize_game(self, data) -> Response:
        code = self.set_code()
        
        #set the playere of the game and return amsg
        player = self.set_player(data)

        #creates game object
        game = Game(
            player=player,#saves as player id
            code=code,
            #rounds_allowed = default 10
            #rounds_used = default 0
            status="IN_PROGRESS"
        )
        #saves the entry to table 
        db.session.add(game)
        db.session.commit()

        # converts the response form the method into JSON
        return jsonify({
            "message": "hello " + player.name + ".",
            "code": code
        })

    def set_code(self) -> list:
        try:
            url = "https://www.random.org/integers/"
            params = {
                "num": 4,
                "min": 0,
                "max": 7,
                "col": 1,
                "base": 10,
                "format": "plain",
                "rnd": "new"
            }
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            self.code = [int(num) for num in response.text.strip().split()]

        #if api fails utilize random method for a fall back code
        except Exception as e:
            self.code = [random.randint(0, 7) for _ in range(4)]

        return self.code

    def set_player(self,data) -> Player:
        # self.player= player

         #store player data from client (player: Belle)
        player_name = data.get("player_name")

        #if theres no player data entered, require player name
        if not player_name:
            return jsonify({"error": "Player name is required."})
        
        
        # SQL = SELECT* FROM players, find first instancee
        player = Player.query.filter_by(name=player_name).first()

        #create a player if its not in the db
        if not player:
            player = Player(name=player_name)
            db.session.add(player)
            db.session.commit()
        return player
