#   Custom Modules in Python

#   What are Custom Modules?
"""
    In addition to using Python's standard library modules, we can create our own
    custom modules to organize and reuse our code. Custom modules allow us to:
    
    - Organize code by functionality
    - Reuse code across multiple programs
    - Keep code DRY (Don't Repeat Yourself)
    - Make code more maintainable
    - Create a clear structure for larger projects
    
    A custom module is simply a .py file containing functions, classes, and
    variables that can be imported and used in other Python programs.
"""

print("=" * 80)
print("Custom Modules in Python:")
print("=" * 80)
print()


#   Creating Custom Modules
"""
    To create a custom module, we simply create a new Python file (.py) with
    the desired name and define the functions, classes, and variables we want
    to include.
    
    Steps:
    1. Create a new .py file with a descriptive name
    2. Write functions, classes, and variables in it
    3. Save the file in the same directory or in Python's path
    4. Import and use it in other Python files
    
    Naming conventions for modules:
    - Use lowercase names (PEP 8 convention)
    - Use underscores for multiple words (my_module, not MyModule)
    - Use descriptive names that reflect the module's purpose
    - Avoid names that conflict with standard library modules
"""

print("=" * 80)
print("Creating Custom Modules:")
print("=" * 80)
print()

# Example 1: Create a simple operations module
print("Example 1: Creating a simple math operations module")
print()

operations_content = '''"""
operations.py - Mathematical operations module

This module contains basic mathematical operations.
"""

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide a by b and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """Raise base to the power of exponent."""
    return base ** exponent

def average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)

# Module constant
MODULE_VERSION = "1.0"
AUTHOR = "Python Developer"
'''

# Write the operations module
with open("operations.py", "w") as f:
    f.write(operations_content)

print("Created operations.py module with mathematical functions")
print()

# Now import and use the module
import operations

print("Using operations module:")
print(f"  add(10, 5): {operations.add(10, 5)}")
print(f"  subtract(10, 5): {operations.subtract(10, 5)}")
print(f"  multiply(10, 5): {operations.multiply(10, 5)}")
print(f"  divide(10, 5): {operations.divide(10, 5)}")
print(f"  power(2, 8): {operations.power(2, 8)}")
print(f"  average([10, 20, 30, 40]): {operations.average([10, 20, 30, 40])}")
print(f"  Module version: {operations.MODULE_VERSION}")

print()


# Example 2: Create a utilities module
print("Example 2: Creating a general utilities module")
print()

utilities_content = '''"""
utilities.py - General utility functions

This module contains commonly used utility functions.
"""

def print_message(message, style="normal"):
    """
    Print a message with optional styling.
    
    Args:
        message: The message to print
        style: 'normal', 'uppercase', or 'centered'
    """
    if style == "uppercase":
        print(message.upper())
    elif style == "centered":
        print(message.center(50))
    else:
        print(message)

def get_user_name():
    """Get the user's name from input."""
    return input("Enter your name: ")

def get_user_age():
    """Get the user's age from input with validation."""
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0 or age > 150:
                print("Please enter a valid age (0-150)")
                continue
            return age
        except ValueError:
            print("Please enter a valid integer")

def is_valid_email(email):
    """Check if an email has a valid format."""
    return "@" in email and "." in email.split("@")[1]

def validate_password(password):
    """Check if a password is strong."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit"
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter"
    return True, "Password is strong"

def repeat_string(string, times):
    """Repeat a string a specified number of times."""
    return string * times

def reverse_string(string):
    """Reverse a string."""
    return string[::-1]

def is_palindrome(string):
    """Check if a string is a palindrome (ignoring spaces)."""
    cleaned = string.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
'''

# Write the utilities module
with open("utilities.py", "w") as f:
    f.write(utilities_content)

print("Created utilities.py module with utility functions")
print()

# Import and use the utilities module
import utilities

print("Using utilities module:")
print()
utilities.print_message("Hello from utilities module")
utilities.print_message("IMPORTANT MESSAGE", style="uppercase")
utilities.print_message("CENTERED TEXT", style="centered")
print()

print(f"Email validation:")
print(f"  'user@example.com' is valid: {utilities.is_valid_email('user@example.com')}")
print(f"  'invalid-email' is valid: {utilities.is_valid_email('invalid-email')}")
print()

print(f"Password validation:")
valid, message = utilities.validate_password("weak")
print(f"  'weak' password: {message}")
valid, message = utilities.validate_password("Strong123")
print(f"  'Strong123' password: {message}")
print()

print(f"String operations:")
print(f"  repeat_string('Ha', 3): {utilities.repeat_string('Ha', 3)}")
print(f"  reverse_string('Python'): {utilities.reverse_string('Python')}")
print(f"  is_palindrome('racecar'): {utilities.is_palindrome('racecar')}")
print(f"  is_palindrome('hello'): {utilities.is_palindrome('hello')}")

print()


# Example 3: Create a data processing module
print("Example 3: Creating a data processing module")
print()

data_processing_content = '''"""
data_processing.py - Data processing and analysis functions

This module contains functions for processing and analyzing data.
"""

def remove_duplicates(items):
    """Remove duplicates from a list while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def filter_by_condition(items, condition_func):
    """Filter items based on a condition function."""
    return [item for item in items if condition_func(item)]

def transform_items(items, transform_func):
    """Transform items using a function."""
    return [transform_func(item) for item in items]

def group_by_key(items, key_func):
    """Group items by a key function."""
    groups = {}
    for item in items:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

def find_max(items):
    """Find the maximum value in a list."""
    if not items:
        raise ValueError("Cannot find max of empty list")
    return max(items)

def find_min(items):
    """Find the minimum value in a list."""
    if not items:
        raise ValueError("Cannot find min of empty list")
    return min(items)

def sort_items(items, reverse=False):
    """Sort items in ascending or descending order."""
    return sorted(items, reverse=reverse)

def sum_items(items):
    """Calculate the sum of items."""
    return sum(items)

def count_occurrences(items):
    """Count occurrences of each item."""
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts
'''

# Write the data processing module
with open("data_processing.py", "w") as f:
    f.write(data_processing_content)

print("Created data_processing.py module")
print()

# Import and use the data processing module
import data_processing

print("Using data_processing module:")
print()

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
print(f"Original list: {numbers}")
print(f"  remove_duplicates(): {data_processing.remove_duplicates(numbers)}")
print(f"  find_max(): {data_processing.find_max(numbers)}")
print(f"  find_min(): {data_processing.find_min(numbers)}")
print(f"  sum_items(): {data_processing.sum_items(numbers)}")
print(f"  count_occurrences(): {data_processing.count_occurrences(numbers)}")
print()

# Filter even numbers
even_numbers = data_processing.filter_by_condition(numbers, lambda x: x % 2 == 0)
print(f"Even numbers: {even_numbers}")

# Transform: square each number
squared = data_processing.transform_items(numbers, lambda x: x ** 2)
print(f"Squared numbers: {squared}")

print()


#   Organizing Code into Modules
print("=" * 80)
print("Code Organization with Modules:")
print("=" * 80)
print()

print("""
Good practices for organizing code:

1. FUNCTIONAL ORGANIZATION
   - Group related functions in the same module
   - One module per main functionality
   - Example: calculations.py, file_handling.py, networking.py

2. CLEAR NAMING
   - Use descriptive module names
   - Use lowercase with underscores
   - Examples: user_management.py, report_generator.py

3. SINGLE RESPONSIBILITY
   - Each module should have one clear purpose
   - Avoid dumping everything into one module

4. DOCUMENTATION
   - Include module docstrings
   - Document all functions
   - Provide usage examples

5. DEPENDENCIES
   - Keep dependencies between modules minimal
   - Avoid circular imports

6. SIZE
   - Keep modules reasonably sized (100-500 lines)
   - Split large modules into smaller ones
""")

print()


#   Practical Example: User Management System
print("=" * 80)
print("Practical Example: User Management System")
print("=" * 80)
print()

user_management_content = '''"""
user_management.py - User management system

This module provides functions for managing user accounts.
"""

class User:
    """Represents a user account."""
    
    def __init__(self, username, email, password):
        """Initialize a user."""
        if not username or len(username) < 3:
            raise ValueError("Username must be at least 3 characters")
        if "@" not in email:
            raise ValueError("Invalid email format")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        
        self.username = username
        self.email = email
        self.password = password
        self.is_active = True
    
    def __str__(self):
        """String representation of user."""
        return f"User(username={self.username}, email={self.email}, active={self.is_active})"
    
    def deactivate(self):
        """Deactivate the user account."""
        self.is_active = False
    
    def activate(self):
        """Activate the user account."""
        self.is_active = True

class UserDatabase:
    """Manages a collection of users."""
    
    def __init__(self):
        """Initialize the database."""
        self.users = {}
    
    def add_user(self, user):
        """Add a user to the database."""
        if user.username in self.users:
            raise ValueError(f"User '{user.username}' already exists")
        self.users[user.username] = user
    
    def get_user(self, username):
        """Get a user by username."""
        return self.users.get(username)
    
    def remove_user(self, username):
        """Remove a user from the database."""
        if username in self.users:
            del self.users[username]
    
    def list_users(self):
        """List all users."""
        return list(self.users.values())
    
    def count_users(self):
        """Count total users."""
        return len(self.users)
    
    def count_active_users(self):
        """Count active users."""
        return sum(1 for u in self.users.values() if u.is_active)
'''

# Write the user management module
with open("user_management.py", "w") as f:
    f.write(user_management_content)

print("Created user_management.py module")
print()

# Import and use the user management module
from user_management import User, UserDatabase

# Create a database
db = UserDatabase()

# Create and add users
try:
    user1 = User("alice", "alice@example.com", "SecurePass123")
    user2 = User("bob", "bob@example.com", "AnotherPass456")
    user3 = User("charlie", "charlie@example.com", "ThirdPass789")
    
    db.add_user(user1)
    db.add_user(user2)
    db.add_user(user3)
    
    print("Users added successfully")
    print(f"Total users: {db.count_users()}")
    print(f"Active users: {db.count_active_users()}")
    print()
    
    print("User list:")
    for user in db.list_users():
        print(f"  - {user}")
    print()
    
    # Deactivate a user
    alice = db.get_user("alice")
    alice.deactivate()
    print(f"Deactivated alice: {alice}")
    print(f"Active users now: {db.count_active_users()}")
    
except ValueError as e:
    print(f"Error: {e}")

print()


#   Module Structure Best Practices
print("=" * 80)
print("Module Structure Best Practices:")
print("=" * 80)
print("""
RECOMMENDED MODULE STRUCTURE:

my_module.py:
├─ Module docstring (what the module does)
├─ Import statements (standard library, third-party, local)
├─ Constants (UPPERCASE_NAMES)
├─ Classes (CamelCase names)
├─ Functions (lowercase_with_underscores)
└─ if __name__ == '__main__': (test code)

EXAMPLE:
'''
\"\"\"
mymodule.py - Brief description of the module.

More detailed explanation of what this module does,
its main functions, and usage examples.
\"\"\"

import os
import sys
from datetime import datetime

# Constants
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

class MyClass:
    \"\"\"Description of the class.\"\"\"
    pass

def my_function():
    \"\"\"Description of the function.\"\"\"
    pass

if __name__ == '__main__':
    # Test code here
    print(my_function())
'''

WHY THIS STRUCTURE?

✓ Clarity: Easy to find what you're looking for
✓ Consistency: All modules follow the same pattern
✓ Maintainability: Clear organization makes updates easier
✓ Reusability: Well-organized code is easier to reuse
✓ Testing: Test code separated from actual code
""")

print()


#   Importing from Custom Modules
print("=" * 80)
print("Different Ways to Import from Custom Modules:")
print("=" * 80)
print()

print("Method 1: Import entire module")
print("  import operations")
print("  result = operations.add(5, 3)")
print()

print("Method 2: Import specific function")
print("  from operations import add")
print("  result = add(5, 3)")
print()

print("Method 3: Import multiple items")
print("  from operations import add, subtract, multiply")
print("  result = add(5, 3)")
print()

print("Method 4: Import with alias")
print("  import operations as ops")
print("  result = ops.add(5, 3)")
print()

print("Method 5: Import function with alias")
print("  from operations import add as addition")
print("  result = addition(5, 3)")
print()


#   Avoiding Common Mistakes
print("=" * 80)
print("Common Mistakes to Avoid:")
print("=" * 80)
print("""
1. NAMING CONFLICTS
   ✗ Don't name modules the same as standard library modules
   ✗ my_math.py, not math.py
   
2. CIRCULAR IMPORTS
   ✗ module_a imports module_b and vice versa
   ✗ Restructure to avoid this
   
3. MODIFYING GLOBAL STATE
   ✗ Avoid functions that change global variables
   ✓ Return values instead
   
4. MISSING DOCSTRINGS
   ✗ Don't create modules without documentation
   ✓ Include module and function docstrings
   
5. TOO MANY DEPENDENCIES
   ✗ Don't make modules that import many other modules
   ✓ Keep external dependencies minimal
   
6. POOR ORGANIZATION
   ✗ Don't put everything in one file
   ✓ Organize by functionality
   
7. NO ERROR HANDLING
   ✗ Don't assume inputs are always valid
   ✓ Include error checking and validation
   
8. HARDCODED VALUES
   ✗ Don't hardcode paths or constants in functions
   ✓ Use parameters or module constants
""")

print()


#   Module Discovery
print("=" * 80)
print("Discovering Module Contents:")
print("=" * 80)
print()

print("Using dir() to list module contents:")
print(f"operations module attributes: {len(dir(operations))}")
print()

# Show only public attributes (not starting with _)
public_attrs = [attr for attr in dir(operations) if not attr.startswith('_')]
print(f"Public attributes: {public_attrs}")
print()

print("Using help() to get documentation:")
print()
help(operations.add)

print()


#   Module __name__ Variable
print("=" * 80)
print("The __name__ Variable:")
print("=" * 80)
print("""
Every Python module has a special variable __name__ that:
- Contains '__main__' when the file is run directly
- Contains the module name when imported

This allows you to write code that runs only when executed directly:

if __name__ == '__main__':
    # This code runs only when file is executed directly
    # Not when imported as a module
    print("Running as main program")
else:
    print("Running as imported module")

BENEFITS:
✓ Write test code in the same file as the module
✓ Use the same file for testing and importing
✓ Distinguish between direct execution and import
""")

print()


print("=" * 80)
print("SUMMARY OF CUSTOM MODULES")
print("=" * 80)
print("""
✓ Custom modules are .py files with reusable code
✓ Create modules by writing functions and classes in .py files
✓ Import modules with 'import' or 'from ... import'
✓ Organize code by functionality into separate modules
✓ Use descriptive, lowercase names for modules
✓ Include docstrings for modules and functions
✓ Keep modules focused on single responsibility
✓ Avoid circular imports and naming conflicts
✓ Use __name__ == '__main__' for test code
✓ Document modules for future developers
✓ Use dir() and help() to explore module contents
✓ Create well-structured, maintainable code
✓ Reuse modules across multiple projects
""")
