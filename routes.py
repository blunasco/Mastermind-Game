from flask import  Blueprint, request, jsonify
from services import GameInitializer, GameSession, GameResult


new_game_bp = Blueprint("new_game", __name__, url_prefix="/start")
guess_bp = Blueprint("guess", __name__, url_prefix="/guess")
end_game_bp = Blueprint("end_game",__name__,url_prefix="/end")

@new_game_bp.route("", methods=["POST"])
def create_new_game():
    data = request.get_json()
    response = GameInitializer().initialize_game(data)
    return response 

@guess_bp.route("", methods=["POST"])
def play_game():
    data = request.get_json()
    
    id = data.get("id")
    guess = data.get("guess")

    session = GameSession(id)
    response = session.check_player_guess(guess)
    return response

@end_game_bp.route("", methods=["POST"])
def end_game():
    data = request.get_json()
    return jsonify(GameResult().end_game(data))
