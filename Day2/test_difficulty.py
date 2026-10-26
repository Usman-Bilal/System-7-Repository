"""
Demo of difficulty levels in the guessing game
"""

import random

def demo_difficulty(level_name, max_num, max_attempts, secret):
    print("\n" + "="*50)
    print(f"🎮 {level_name.upper()} MODE DEMO")
    print("="*50)
    print(f"Guess the number between 1 and {max_num}")
    print(f"You have {max_attempts} attempts")
    print(f"[Demo: Secret number is {secret}]")
    print("="*50)
    
    attempts = 0
    
    # Smart guessing algorithm (binary search-ish)
    low, high = 1, max_num
    
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1
        
        guess = (low + high) // 2
        print(f"\nAttempt {attempts}/{max_attempts} - Guess: {guess}")
        
        if guess == secret:
            print(f"\n🎉 CONGRATULATIONS! Won in {attempts} attempts!")
            return True
        elif guess < secret:
            print(f"📈 Too low! ({remaining} attempts remaining)")
            low = guess + 1
        else:
            print(f"📉 Too high! ({remaining} attempts remaining)")
            high = guess - 1
    
    print(f"\n😢 Game Over! The number was {secret}")
    return False

# Demo Easy Mode
random.seed(10)
secret = random.randint(1, 50)
demo_difficulty("Easy", 50, 15, secret)

# Demo Medium Mode
print("\n" + "="*70)
random.seed(20)
secret = random.randint(1, 100)
demo_difficulty("Medium", 100, 10, secret)

# Demo Hard Mode
print("\n" + "="*70)
random.seed(30)
secret = random.randint(1, 200)
demo_difficulty("Hard", 200, 7, secret)

print("\n" + "="*50)
print("ALL DIFFICULTY LEVELS DEMONSTRATED!")
print("="*50)
