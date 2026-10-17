"""
Library Management System Demo
"""

from library_system import Library

def main():
    print("\n" + "="*60)
    print("LIBRARY MANAGEMENT SYSTEM DEMO")
    print("="*60)
    
    # Create library
    library = Library("City Public Library")
    
    # Add books
    print("\n--- Adding Books ---")
    library.add_book("978-0-13-110362-7", "Clean Code", "Robert Martin", 3)
    library.add_book("978-0-13-468599-1", "Python Crash Course", "Eric Matthes", 2)
    library.add_book("978-0-596-00976-6", "Learning Python", "Mark Lutz", 2)
    library.add_book("978-1-449-35573-9", "Data Science from Scratch", "Joel Grus", 1)
    
    # Display all books
    library.display_books()
    
    # Register members
    print("\n--- Registering Members ---")
    member1 = library.register_member("Alice Johnson", "alice@email.com")
    member2 = library.register_member("Bob Smith", "bob@email.com")
    
    # Search books
    print("\n--- Searching Books ---")
    results = library.search_books("Python")
    print(f"Found {len(results)} books matching 'Python':")
    for book in results:
        print(f"  - {book}")
    
    # Borrow books
    print("\n--- Borrowing Books ---")
    library.borrow_book(member1, "978-0-13-110362-7")
    library.borrow_book(member1, "978-0-13-468599-1")
    library.borrow_book(member2, "978-0-596-00976-6")
    
    # Display member's borrowed books
    library.display_member_books(member1)
    
    # Display updated catalog
    library.display_books()
    
    # Return a book
    print("\n--- Returning Books ---")
    library.return_book(member1, "978-0-13-110362-7")
    
    # Display updated catalog
    library.display_books()
    
    print("\n" + "="*60)
    print("DEMO COMPLETE")
    print("="*60)

if __name__ == "__main__":
    main()
