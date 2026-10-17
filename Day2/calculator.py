"""
Task 2: Command-line Calculator
Skills: Input/output, loops, functions
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

def modulus(a, b):
    """Return remainder of a divided by b"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a % b

def display_menu():
    """Display calculator menu"""
    print("\n" + "="*50)
    print("COMMAND-LINE CALCULATOR")
    print("="*50)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("7. Exit")
    print("="*50)

def get_number(prompt):
    """Get a valid number from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculator():
    """Main calculator function"""
    print("\n🧮 Welcome to the Command-Line Calculator!")
    
    while True:
        display_menu()
        
        choice = input("\nSelect operation (1-7): ").strip()
        
        if choice == '7':
            print("\n✓ Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("\n❌ Invalid choice! Please select 1-7.")
            continue
        
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "/"
        elif choice == '5':
            result = power(num1, num2)
            operation = "^"
        elif choice == '6':
            result = modulus(num1, num2)
            operation = "%"
        
        print(f"\n✓ Result: {num1} {operation} {num2} = {result}")
        
        continue_calc = input("\nPerform another calculation? (y/n): ").strip().lower()
        if continue_calc != 'y':
            print("\n✓ Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
