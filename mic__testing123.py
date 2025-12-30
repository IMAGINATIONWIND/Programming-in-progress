import numpy as np
import random

# numpy.ndarray of strings (3x3 outcome matrix)
# Rows = Player, Columns = Computer
outcome = np.array([
    ["D", "W", "L"],  # Player = S
    ["L", "D", "W"],  # Player = W
    ["W", "L", "D"]   # Player = G
])

# numpy.ndarray of strings (choices)
choices = np.array(["S", "W", "G"])

# str
player: str = input("Enter your choice (S for Snake, W for Water, G for Gun): ").upper()
computer: str = random.choice(choices)

# int
player_index: int = np.where(choices == player)[0][0]
computer_index: int = np.where(choices == computer)[0][0]

# str
result: str = outcome[player_index, computer_index]

print(f"Player: {player}, Computer: {computer}, Result: {result}")

