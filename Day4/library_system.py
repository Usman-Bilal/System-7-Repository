"""
Task 4: Library Management System using OOP
Skills: Basic OOP, modules
"""

from datetime import datetime, timedelta

class Book:
    """Book class"""
    
    def __init__(self, isbn, title, author, quantity=1):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.total_quantity = quantity
        self.available_quantity = quantity
    
    def is_available(self):
        """Check if book is available"""
        return self.available_quantity > 0
    
    def borrow(self):
        """Borrow a book"""
        if self.available_quantity > 0:
            self.available_quantity -= 1
            return True
        return False
    
    def return_book(self):
        """Return a book"""
        if self.available_quantity < self.total_quantity:
            self.available_quantity += 1
            return True
        return False
    
    def __str__(self):
        return (f"'{self.title}' by {self.author} "
                f"[ISBN: {self.isbn}] - Available: {self.available_quantity}/{self.total_quantity}")


class Member:
    """Library member class"""
    
    member_counter = 1000
    
    def __init__(self, name, email):
        self.member_id = Member.member_counter
        Member.member_counter += 1
        self.name = name
        self.email = email
        self.borrowed_books = {}
    
    def __str__(self):
        return f"Member({self.member_id}): {self.name} - {self.email}"


class Library:
    """Library management system"""
    
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = {}
        self.borrow_records = []
    
    def add_book(self, isbn, title, author, quantity=1):
        """Add book to library"""
        if isbn in self.books:
            self.books[isbn].total_quantity += quantity
            self.books[isbn].available_quantity += quantity
            print(f"✓ Added {quantity} more copies of '{title}'")
        else:
            self.books[isbn] = Book(isbn, title, author, quantity)
            print(f"✓ Book '{title}' added to library!")
        return True
    
    def remove_book(self, isbn):
        """Remove book from library"""
        if isbn in self.books:
            book = self.books[isbn]
            if book.available_quantity < book.total_quantity:
                print(f"❌ Cannot remove '{book.title}' - some copies are borrowed!")
                return False
            del self.books[isbn]
            print(f"✓ Book removed from library!")
            return True
        else:
            print("❌ Book not found!")
            return False
    
    def search_books(self, query):
        """Search books by title, author, or ISBN"""
        results = []
        query = query.lower()
        
        for book in self.books.values():
            if (query in book.title.lower() or 
                query in book.author.lower() or 
                query in book.isbn.lower()):
                results.append(book)
        
        return results
    
    def display_books(self):
        """Display all books"""
        print("\n" + "="*80)
        print(f"{self.name} - BOOK CATALOG")
        print("="*80)
        
        if not self.books:
            print("No books in library.")
            return
        
        print(f"{'ISBN':<15} {'Title':<30} {'Author':<20} {'Available':<10}")
        print("-"*80)
        
        for book in self.books.values():
            print(f"{book.isbn:<15} {book.title:<30} {book.author:<20} "
                  f"{book.available_quantity}/{book.total_quantity}")
        
        print("="*80)
    
    def register_member(self, name, email):
        """Register new member"""
        member = Member(name, email)
        self.members[member.member_id] = member
        print(f"✓ Member registered! ID: {member.member_id}")
        return member.member_id
    
    def borrow_book(self, member_id, isbn):
        """Member borrows a book"""
        if member_id not in self.members:
            print("❌ Member not found!")
            return False
        
        if isbn not in self.books:
            print("❌ Book not found!")
            return False
        
        member = self.members[member_id]
        book = self.books[isbn]
        
        if not book.is_available():
            print(f"❌ '{book.title}' is not available!")
            return False
        
        if isbn in member.borrowed_books:
            print(f"❌ {member.name} already borrowed this book!")
            return False
        
        if book.borrow():
            due_date = datetime.now() + timedelta(days=14)
            member.borrowed_books[isbn] = {
                'book': book,
                'borrow_date': datetime.now(),
                'due_date': due_date
            }
            
            self.borrow_records.append({
                'member_id': member_id,
                'isbn': isbn,
                'action': 'borrowed',
                'date': datetime.now()
            })
            
            print(f"✓ '{book.title}' borrowed by {member.name}")
            print(f"Due date: {due_date.strftime('%Y-%m-%d')}")
            return True
        
        return False
    
    def return_book(self, member_id, isbn):
        """Member returns a book"""
        if member_id not in self.members:
            print("❌ Member not found!")
            return False
        
        member = self.members[member_id]
        
        if isbn not in member.borrowed_books:
            print(f"❌ {member.name} hasn't borrowed this book!")
            return False
        
        book_info = member.borrowed_books[isbn]
        book = book_info['book']
        due_date = book_info['due_date']
        
        book.return_book()
        del member.borrowed_books[isbn]
        
        self.borrow_records.append({
            'member_id': member_id,
            'isbn': isbn,
            'action': 'returned',
            'date': datetime.now()
        })
        
        # Calculate fine if overdue
        if datetime.now() > due_date:
            days_late = (datetime.now() - due_date).days
            fine = days_late * 0.50
            print(f"⚠️ Book is {days_late} days overdue!")
            print(f"Fine: ${fine:.2f} ($0.50 per day)")
        
        print(f"✓ '{book.title}' returned by {member.name}")
        return True
    
    def display_member_books(self, member_id):
        """Display books borrowed by member"""
        if member_id not in self.members:
            print("❌ Member not found!")
            return
        
        member = self.members[member_id]
        print(f"\n{'='*70}")
        print(f"Books borrowed by {member.name}")
        print("="*70)
        
        if not member.borrowed_books:
            print("No books currently borrowed.")
            return
        
        for isbn, info in member.borrowed_books.items():
            book = info['book']
            due_date = info['due_date']
            days_left = (due_date - datetime.now()).days
            
            print(f"\nTitle: {book.title}")
            print(f"Author: {book.author}")
            print(f"Due: {due_date.strftime('%Y-%m-%d')} ({days_left} days left)")
            
            if days_left < 0:
                print(f"⚠️ OVERDUE by {abs(days_left)} days!")
        
        print("="*70)
