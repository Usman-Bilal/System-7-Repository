"""
Interactive demonstration - This simulates user playing the game
"""

import subprocess
import sys

# Simulate user inputs for the game
user_inputs = [
    "1",      # Select Classic Mode
    "50",     # First guess
    "75",     # Second guess
    "88",     # Third guess
    "82",     # Fourth guess (likely to win around here)
    "n"       # Don't play again
]

input_string = "\n".join(user_inputs)

print("="*60)
print("SIMULATING INTERACTIVE GAME SESSION")
print("="*60)
print("User will select Classic Mode and guess numbers...")
print("="*60 + "\n")

# Run the actual game with simulated inputs
process = subprocess.Popen(
    [sys.executable, "Day2/number_guessing_game.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

output, error = process.communicate(input=input_string)
print(output)

if error:
    print("Errors:", error)
