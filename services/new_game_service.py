from flask import Response, jsonify
import requests, random
from models import db, Game, Player

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

        # NEW GAME PLAYER LOGIC
        #get player name from requests data (player: Belle)
        player_name = data.get("player")

        #if theres no player data from request, require player name
        if not player_name:
            return jsonify({"error": "Player name is required."}), 400
        
        # look up if player exists in db, if player does not exist create player
        player = Player.query.filter_by(name=player_name).first()
        if not player:
            player = Player(name=player_name)
            db.session.add(player)
            db.session.commit()

        #set the playere of the game and return amsg
        welcome_msg = self.set_player(player_name)

        #create a new entry in the Game table
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
            "message": welcome_msg,
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
            resp = requests.get(url, params=params, timeout=5)
            resp.raise_for_status()
            self.code = [int(x) for x in resp.text.strip().split()]
            print("API code:", self.code)
        except Exception as e:
            self.code = [random.randint(0, 7) for _ in range(4)]
            print("Fallback code:", self.code, "Reason:", e)

        self.rounds_used = 0
        self.status = "IN_PROGRESS"
        self.guess_record = []
        return self.code

    def set_player(self,player: str) -> str:
        self.player= player

        return f"Welcome to the game, {player}"


        


