"""
Task 3: Student Record Manager with File Handling
Skills: Dictionaries, file handling, exceptions
"""

import json
import os
import re

FILENAME = 'students.json'

def load_students():
    """Load student records from file"""
    if not os.path.exists(FILENAME):
        return {}
    
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("⚠️ Error reading file. Starting with empty records.")
        return {}
    except Exception as e:
        print(f"⚠️ Error loading data: {e}")
        return {}

def save_students(students):
    """Save student records to file"""
    try:
        with open(FILENAME, 'w') as file:
            json.dump(students, file, indent=4)
        return True
    except Exception as e:
        print(f"❌ Error saving data: {e}")
        return False

def validate_email(email):
    """Basic email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_grade(grade):
    """Validate grade input"""
    return grade.upper() in ['A', 'B', 'C', 'D', 'F']

def add_student(students):
    """Add a new student record"""
    print("\n" + "="*60)
    print("ADD NEW STUDENT")
    print("="*60)
    
    student_id = input("Enter Student ID: ").strip()
    
    if not student_id:
        print("❌ Student ID cannot be empty!")
        return
    
    if student_id in students:
        print(f"❌ Student ID '{student_id}' already exists!")
        return
    
    name = input("Enter Student Name: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        return
    
    try:
        age = int(input("Enter Age: "))
        if age < 5 or age > 100:
            print("❌ Please enter a valid age (5-100)!")
            return
    except ValueError:
        print("❌ Invalid age! Please enter a number.")
        return
    
    grade = input("Enter Grade (A/B/C/D/F): ").strip().upper()
    if not validate_grade(grade):
        print("❌ Invalid grade! Please enter A, B, C, D, or F.")
        return
    
    email = input("Enter Email: ").strip()
    if not validate_email(email):
        print("❌ Invalid email format!")
        return
    
    students[student_id] = {
        'name': name,
        'age': age,
        'grade': grade,
        'email': email
    }
    
    if save_students(students):
        print(f"\n✓ Student '{name}' added successfully!")
    else:
        print("\n❌ Failed to save student record.")

def view_students(students):
    """Display all student records"""
    print("\n" + "="*80)
    print("ALL STUDENT RECORDS")
    print("="*80)
    
    if not students:
        print("No student records found.")
        return
    
    print(f"{'ID':<10} {'Name':<20} {'Age':<5} {'Grade':<7} {'Email':<30}")
    print("-"*80)
    
    for student_id, info in students.items():
        print(f"{student_id:<10} {info['name']:<20} {info['age']:<5} "
              f"{info['grade']:<7} {info['email']:<30}")
    
    print("="*80)
    print(f"Total Students: {len(students)}")

def search_student(students):
    """Search for a student by ID"""
    print("\n" + "="*60)
    print("SEARCH STUDENT")
    print("="*60)
    
    student_id = input("Enter Student ID to search: ").strip()
    
    if student_id in students:
        info = students[student_id]
        print("\n✓ Student Found:")
        print("-"*60)
        print(f"ID:    {student_id}")
        print(f"Name:  {info['name']}")
        print(f"Age:   {info['age']}")
        print(f"Grade: {info['grade']}")
        print(f"Email: {info['email']}")
        print("-"*60)
    else:
        print(f"\n❌ No student found with ID '{student_id}'")

def update_student(students):
    """Update existing student information"""
    print("\n" + "="*60)
    print("UPDATE STUDENT")
    print("="*60)
    
    student_id = input("Enter Student ID to update: ").strip()
    
    if student_id not in students:
        print(f"\n❌ No student found with ID '{student_id}'")
        return
    
    info = students[student_id]
    print(f"\nCurrent Information for {info['name']}:")
    print(f"Age: {info['age']}, Grade: {info['grade']}, Email: {info['email']}")
    print("\nEnter new information (press Enter to keep current value):")
    
    name = input(f"Name [{info['name']}]: ").strip()
    if name:
        info['name'] = name
    
    age_input = input(f"Age [{info['age']}]: ").strip()
    if age_input:
        try:
            age = int(age_input)
            if 5 <= age <= 100:
                info['age'] = age
            else:
                print("⚠️ Invalid age. Keeping current value.")
        except ValueError:
            print("⚠️ Invalid age. Keeping current value.")
    
    grade_input = input(f"Grade [{info['grade']}]: ").strip().upper()
    if grade_input:
        if validate_grade(grade_input):
            info['grade'] = grade_input
        else:
            print("⚠️ Invalid grade. Keeping current value.")
    
    email_input = input(f"Email [{info['email']}]: ").strip()
    if email_input:
        if validate_email(email_input):
            info['email'] = email_input
        else:
            print("⚠️ Invalid email. Keeping current value.")
    
    if save_students(students):
        print(f"\n✓ Student '{info['name']}' updated successfully!")
    else:
        print("\n❌ Failed to update student record.")

def delete_student(students):
    """Delete a student record"""
    print("\n" + "="*60)
    print("DELETE STUDENT")
    print("="*60)
    
    student_id = input("Enter Student ID to delete: ").strip()
    
    if student_id not in students:
        print(f"\n❌ No student found with ID '{student_id}'")
        return
    
    name = students[student_id]['name']
    confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
    
    if confirm == 'y':
        del students[student_id]
        if save_students(students):
            print(f"\n✓ Student '{name}' deleted successfully!")
        else:
            print("\n❌ Failed to delete student record.")
    else:
        print("\n✓ Deletion cancelled.")

def display_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("STUDENT RECORD MANAGER")
    print("="*60)
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("="*60)

def main():
    """Main program function"""
    print("\n📚 Welcome to Student Record Manager!")
    students = load_students()
    
    while True:
        display_menu()
        choice = input("\nSelect option (1-6): ").strip()
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_student(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            print("\n✓ Data saved. Thank you for using Student Record Manager!")
            break
        else:
            print("\n❌ Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main()
