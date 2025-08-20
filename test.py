from services.in_game_service import GameSession
from services.new_game_service import GameInitializer

# Step 1: Initialize a new game
initializer = GameInitializer()
initializer.set_code()
initializer.set_player("Belle")

# Step 2: Create a session that uses initializer’s code
g = GameSession()
g.code = initializer.code
g.rounds_allowed = initializer.rounds_allowed
g.rounds_used = 0
g.status = "IN_PROGRESS"

print("Secret code:", g.code)

# Step 3: Play the game
print(g.check_player_guess([9,9,9,9]))
print(g.check_player_guess([8,8,8,8]))
print(g.check_player_guess([7,7,7,7]))
print(g.check_player_guess([1,2,3,4]))
