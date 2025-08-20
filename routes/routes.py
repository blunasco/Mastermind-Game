
from flask import  Blueprint, jsonify, request
from services import GameInitializer, GameSession, GameResult


# game = Game()
current_initializer = None
current_game = None

new_game_bp = Blueprint("new_game", __name__, url_prefix="/start")
guess_bp = Blueprint("guess", __name__, url_prefix="/guess")
end_game_bp = Blueprint("end_game",__name__,url_prefix="/end")


# Start a new game
@new_game_bp.route("", methods=["POST"]) #creates endpoint
def create_new_game():
    data = request.get_json() #reads what client sends, auto parses it into a python dict
    print("DEBUG new game data received:", data)  #this is a python dict
    response = GameInitializer().initialize_game(data) #creates a new GameInitializer object, calls its method, and pass in the request data
    return response 

# Play the game (make a guess)
@guess_bp.route("", methods=["POST"])
def play_game():
    data = request.get_json()
    print("DEBUG in game data received:", data)
    id = data.get("id")
    guess = data.get("guess")

    session = GameSession(id)
    response = session.check_player_guess(guess)
    return response

#End the game
@end_game_bp.route("", methods=["POST"])
def end_game():
    data = request.get_json()
    id = data.get("id")
    
    response = GameResult(id).end_game(id)
    return response




