"""
Task 2: Number Guessing Game
Skills: Input/output, loops, functions, random module
"""

import random

def play_game():
    """Main game function"""
    print("\n" + "="*50)
    print("🎮 NUMBER GUESSING GAME")
    print("="*50)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")
    print("="*50)
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1
        
        try:
            guess = int(input(f"\nAttempt {attempts}/{max_attempts} - Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("❌ Please enter a number between 1 and 100!")
                attempts -= 1  # Don't count invalid attempts
                continue
            
            if guess == secret_number:
                print(f"\n🎉 CONGRATULATIONS! You guessed it in {attempts} attempts!")
                print(f"The number was {secret_number}")
                return True
            elif guess < secret_number:
                print(f"📈 Too low! Try higher. ({remaining} attempts remaining)")
            else:
                print(f"📉 Too high! Try lower. ({remaining} attempts remaining)")
                
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            attempts -= 1  # Don't count invalid attempts
    
    print(f"\n😢 Game Over! You've used all {max_attempts} attempts.")
    print(f"The number was {secret_number}")
    return False

def play_with_difficulty():
    """Game with difficulty levels"""
    print("\n" + "="*50)
    print("🎮 NUMBER GUESSING GAME - DIFFICULTY MODE")
    print("="*50)
    print("Select difficulty level:")
    print("1. Easy (1-50, 15 attempts)")
    print("2. Medium (1-100, 10 attempts)")
    print("3. Hard (1-200, 7 attempts)")
    print("="*50)
    
    choice = input("\nSelect difficulty (1-3): ").strip()
    
    if choice == '1':
        max_num, max_attempts = 50, 15
        level = "Easy"
    elif choice == '2':
        max_num, max_attempts = 100, 10
        level = "Medium"
    elif choice == '3':
        max_num, max_attempts = 200, 7
        level = "Hard"
    else:
        print("Invalid choice! Defaulting to Medium.")
        max_num, max_attempts = 100, 10
        level = "Medium"
    
    print(f"\n🎯 Level: {level}")
    print(f"Guess the number between 1 and {max_num}")
    print(f"You have {max_attempts} attempts")
    
    secret_number = random.randint(1, max_num)
    attempts = 0
    
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1
        
        try:
            guess = int(input(f"\nAttempt {attempts}/{max_attempts} - Enter your guess: "))
            
            if guess < 1 or guess > max_num:
                print(f"❌ Please enter a number between 1 and {max_num}!")
                attempts -= 1
                continue
            
            if guess == secret_number:
                print(f"\n🎉 CONGRATULATIONS! You won at {level} level!")
                print(f"You guessed {secret_number} in {attempts} attempts!")
                return True
            elif guess < secret_number:
                print(f"📈 Too low! ({remaining} attempts remaining)")
            else:
                print(f"📉 Too high! ({remaining} attempts remaining)")
                
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            attempts -= 1
    
    print(f"\n😢 Game Over! The number was {secret_number}")
    return False

def main():
    """Main function with menu"""
    print("\n🎮 Welcome to Number Guessing Game!")
    
    while True:
        print("\n" + "="*50)
        print("MAIN MENU")
        print("="*50)
        print("1. Play Classic Mode (1-100, 10 attempts)")
        print("2. Play with Difficulty Levels")
        print("3. Exit")
        print("="*50)
        
        choice = input("\nSelect option (1-3): ").strip()
        
        if choice == '1':
            won = play_game()
        elif choice == '2':
            won = play_with_difficulty()
        elif choice == '3':
            print("\n✓ Thanks for playing! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select 1-3.")
            continue
        
        if choice in ['1', '2']:
            play_again = input("\nPlay again? (y/n): ").strip().lower()
            if play_again != 'y':
                print("\n✓ Thanks for playing! Goodbye!")
                break

if __name__ == "__main__":
    main()
