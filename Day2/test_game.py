"""
Automated test/demo of the number guessing game
"""

import random

# Set seed for reproducible demo
random.seed(42)

print("\n" + "="*50)
print("🎮 NUMBER GUESSING GAME DEMO")
print("="*50)

# Simulate a game
secret_number = random.randint(1, 100)
print(f"\n[Demo Info: Secret number is {secret_number}]")
print("Game: I'm thinking of a number between 1 and 100.")
print("Can you guess it?")
print("="*50)

attempts = 0
max_attempts = 10

# Simulated guesses
guesses = [50, 75, 88, 82, 85, 87, 86]

for guess in guesses:
    attempts += 1
    remaining = max_attempts - attempts + 1
    
    print(f"\nAttempt {attempts}/{max_attempts} - Enter your guess: {guess}")
    
    if guess == secret_number:
        print(f"\n🎉 CONGRATULATIONS! You guessed it in {attempts} attempts!")
        print(f"The number was {secret_number}")
        break
    elif guess < secret_number:
        print(f"📈 Too low! Try higher. ({remaining} attempts remaining)")
    else:
        print(f"📉 Too high! Try lower. ({remaining} attempts remaining)")

print("\n" + "="*50)
print("DEMO COMPLETE")
print("="*50)
