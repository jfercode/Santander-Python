#   Modules in Python

#   What are Modules?
"""
    A module is a file that contains definitions of functions, classes, and variables
    that can be used in other programs. Importing modules allows us to access
    functionality defined in other files and reuse code efficiently.
    
    Benefits of modules:
    - Code reusability: Write once, use many times
    - Code organization: Organize related functionality together
    - Namespace separation: Avoid naming conflicts
    - Maintainability: Easier to update and debug
    - Collaboration: Share code across projects
    
    Python comes with an extensive standard library that provides additional
    functionality without needing separate installation.
"""

print("=" * 80)
print("Modules in Python:")
print("=" * 80)
print()


#   Importing Modules
"""
    To use a module in our program, we must import it using the import statement.
    We can import an entire module or specific functions from a module.
    
    Different import styles:
    1. import module_name
    2. from module_name import function_name
    3. from module_name import function1, function2
    4. from module_name import *  (not recommended)
    5. import module_name as alias
    6. from module_name import function_name as alias
"""

print("=" * 80)
print("Importing Modules:")
print("=" * 80)
print()

# Example 1: Basic module import
print("Example 1: Importing the math module")
print()

import math

resultado = math.sqrt(25)
print(f"Square root of 25: {resultado}")

resultado2 = math.pi
print(f"Value of pi: {resultado2}")

resultado3 = math.ceil(4.3)
print(f"Ceiling of 4.3: {resultado3}")

print()


# Example 2: Importing specific functions
print("Example 2: Importing specific functions from a module")
print()

from math import sqrt, pow, floor

resultado = sqrt(36)
print(f"Square root of 36: {resultado}")

resultado2 = pow(2, 8)
print(f"2 to the power of 8: {resultado2}")

resultado3 = floor(7.9)
print(f"Floor of 7.9: {resultado3}")

print()


# Example 3: Importing multiple functions
print("Example 3: Importing multiple functions in one statement")
print()

from math import sin, cos, tan, radians

angle = 45
angle_radians = radians(angle)

sine_value = sin(angle_radians)
cosine_value = cos(angle_radians)
tangent_value = tan(angle_radians)

print(f"Angle: {angle} degrees")
print(f"Sine: {sine_value:.4f}")
print(f"Cosine: {cosine_value:.4f}")
print(f"Tangent: {tangent_value:.4f}")

print()


# Example 4: Using aliases
print("Example 4: Using aliases for modules and functions")
print()

import random as rnd
from datetime import datetime as dt

# Using alias for module
random_number = rnd.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

random_choice = rnd.choice(['apple', 'banana', 'orange', 'grape'])
print(f"Random choice: {random_choice}")

# Using alias for function
current_time = dt.now()
print(f"Current date and time: {current_time}")

print()


#   Standard Library Modules
"""
    Python's standard library provides many useful modules:
    
    - math: Mathematical operations
    - random: Random number generation
    - datetime: Date and time handling
    - os: Operating system interactions
    - sys: System-specific functionality
    - string: String constants and operations
    - json: JSON encoding and decoding
    - re: Regular expressions
    - collections: Specialized container datatypes
    - statistics: Mathematical statistics
"""

print("=" * 80)
print("Standard Library Modules:")
print("=" * 80)
print()

# The MATH module
print("MATH MODULE: Mathematical operations")
print("-" * 80)
print()

import math

print("Math constants:")
print(f"  PI (π): {math.pi}")
print(f"  E (e): {math.e}")
print()

print("Math functions:")
print(f"  sqrt(16): {math.sqrt(16)}")
print(f"  pow(2, 5): {math.pow(2, 5)}")
print(f"  ceil(4.2): {math.ceil(4.2)}")
print(f"  floor(4.9): {math.floor(4.9)}")
print(f"  abs(-10): {math.abs(-10)}")
print(f"  factorial(5): {math.factorial(5)}")
print(f"  gcd(48, 18): {math.gcd(48, 18)}")

print()


# The RANDOM module
print("RANDOM MODULE: Random number generation")
print("-" * 80)
print()

import random

print("Random number generation:")
print(f"  random(): {random.random():.4f}")  # Float between 0 and 1
print(f"  randint(1, 100): {random.randint(1, 100)}")  # Integer between 1 and 100
print(f"  uniform(1.5, 10.5): {random.uniform(1.5, 10.5):.2f}")  # Float in range
print()

items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Original list: {items}")
print(f"  choice(): {random.choice(items)}")  # Random element
print(f"  sample(list, 3): {random.sample(items, 3)}")  # Random sample
print()

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"  shuffle(): {numbers}")  # In-place shuffle

print()


# The DATETIME module
print("DATETIME MODULE: Date and time handling")
print("-" * 80)
print()

import datetime

# Current date and time
now = datetime.datetime.now()
print(f"Current date and time: {now}")
print(f"  Year: {now.year}")
print(f"  Month: {now.month}")
print(f"  Day: {now.day}")
print(f"  Hour: {now.hour}")
print(f"  Minute: {now.minute}")
print(f"  Second: {now.second}")
print()

# Create specific date
birthday = datetime.date(1990, 5, 15)
print(f"Birthday: {birthday}")
print()

# Time difference
today = datetime.date.today()
age_start = datetime.date(2000, 1, 1)
years_since = today - age_start
print(f"Days since 2000-01-01: {years_since.days}")
print()

# Formatting dates
formatted = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"Formatted datetime: {formatted}")

print()


# The OS module
print("OS MODULE: Operating system interactions")
print("-" * 80)
print()

import os

print("Operating system information:")
print(f"  Current working directory: {os.getcwd()}")
print(f"  Operating system: {os.name}")
print()

# List files in current directory
print("Files in current directory:")
files = os.listdir(".")
for file in files[:5]:  # Show first 5 files
    print(f"  - {file}")
if len(files) > 5:
    print(f"  ... and {len(files) - 5} more files")

print()


# The SYS module
print("SYS MODULE: System-specific functionality")
print("-" * 80)
print()

import sys

print("System information:")
print(f"  Python version: {sys.version.split()[0]}")
print(f"  Platform: {sys.platform}")
print(f"  Max int: {sys.maxsize}")
print()

print(f"Command line arguments: {sys.argv}")

print()


# The STATISTICS module
print("STATISTICS MODULE: Mathematical statistics")
print("-" * 80)
print()

from statistics import mean, median, mode, stdev

scores = [85, 90, 88, 92, 87, 90, 89, 91]

print(f"Scores: {scores}")
print(f"  Mean: {mean(scores):.2f}")
print(f"  Median: {median(scores):.2f}")
print(f"  Mode: {mode(scores):.2f}")
print(f"  Standard deviation: {stdev(scores):.2f}")

print()


# The STRING module
print("STRING MODULE: String constants and operations")
print("-" * 80)
print()

import string

print("String constants:")
print(f"  Digits: {string.digits}")
print(f"  ASCII letters: {string.ascii_letters}")
print(f"  Punctuation: {string.punctuation}")
print()

# Check character type
test_char = 'A'
print(f"Character '{test_char}':")
print(f"  Is digit: {test_char in string.digits}")
print(f"  Is letter: {test_char in string.ascii_letters}")
print(f"  Is uppercase: {test_char in string.ascii_uppercase}")
print(f"  Is lowercase: {test_char in string.ascii_lowercase}")

print()


# The JSON module
print("JSON MODULE: JSON encoding and decoding")
print("-" * 80)
print()

import json

# Dictionary to JSON
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'hobbies': ['reading', 'hiking', 'coding']
}

json_string = json.dumps(person)
print(f"Dictionary as JSON: {json_string}")
print()

# JSON to dictionary
json_data = '{"product": "laptop", "price": 999.99, "in_stock": true}'
parsed = json.loads(json_data)
print(f"JSON string parsed to dictionary:")
print(f"  Product: {parsed['product']}")
print(f"  Price: ${parsed['price']}")
print(f"  In stock: {parsed['in_stock']}")

print()


#   Practical Example: Using Multiple Modules
print("=" * 80)
print("Practical Example: Building a Random Quiz")
print("=" * 80)
print()

import random
import datetime

def run_quiz():
    """Run a simple quiz with random questions."""
    questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['London', 'Berlin', 'Paris', 'Madrid'],
            'answer': 'Paris'
        },
        {
            'question': 'Which planet is closest to the sun?',
            'options': ['Venus', 'Mercury', 'Mars', 'Earth'],
            'answer': 'Mercury'
        },
        {
            'question': 'What is the largest ocean?',
            'options': ['Atlantic', 'Indian', 'Arctic', 'Pacific'],
            'answer': 'Pacific'
        }
    ]
    
    # Shuffle questions
    random.shuffle(questions)
    
    score = 0
    start_time = datetime.datetime.now()
    
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for j, option in enumerate(q['options'], 1):
            print(f"  {j}. {option}")
        
        # In a real quiz, you would get user input here
        # For demonstration, we'll just show the answer
        print(f"  Correct answer: {q['answer']}")
        print()
        score += 1
    
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    
    print(f"Quiz completed!")
    print(f"Score: {score}/{len(questions)}")
    print(f"Duration: {duration.total_seconds():.2f} seconds")

run_quiz()

print()


#   Creating Your Own Module
"""
    You can create your own modules by writing Python code in separate files.
    Any .py file can be used as a module.
    
    Example structure:
    
    # my_module.py
    def greet(name):
        return f"Hello, {name}!"
    
    def add(a, b):
        return a + b
    
    CONSTANT = 42
    
    # Then in another file:
    import my_module
    print(my_module.greet("Alice"))
    print(my_module.add(3, 5))
    print(my_module.CONSTANT)
"""

print("=" * 80)
print("Creating Your Own Module:")
print("=" * 80)
print()

# Create a simple module file
module_content = '''"""
my_utils.py - A simple utility module
"""

def greet(name):
    """Greet someone by name."""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

# Module constant
PI_APPROXIMATION = 3.14159
AUTHOR = "Your Name"
'''

# Write the module to a file
with open("my_utils.py", "w") as f:
    f.write(module_content)

print("Created my_utils.py module")
print()

# Import and use the custom module
import my_utils

print("Using custom module:")
print(f"  greet('Bob'): {my_utils.greet('Bob')}")
print(f"  add(10, 20): {my_utils.add(10, 20)}")
print(f"  multiply(5, 7): {my_utils.multiply(5, 7)}")
print(f"  is_even(10): {my_utils.is_even(10)}")
print(f"  is_even(7): {my_utils.is_even(7)}")
print(f"  PI_APPROXIMATION: {my_utils.PI_APPROXIMATION}")

print()


#   Module and Namespace
print("=" * 80)
print("Modules and Namespaces:")
print("=" * 80)
print()

# Different modules can have functions with the same name
from math import sqrt as math_sqrt

def sqrt(x):
    """Custom square root function."""
    return x ** 0.5

print("Using functions with same name from different namespaces:")
print(f"  math.sqrt(16): {math_sqrt(16)}")
print(f"  custom sqrt(16): {sqrt(16)}")
print()

# Access all attributes of a module
print("Attributes in math module:")
math_attributes = [attr for attr in dir(math) if not attr.startswith('_')]
print(f"  Total: {len(math_attributes)} attributes")
print(f"  Examples: {math_attributes[:8]}")

print()


#   Best Practices for Modules
print("=" * 80)
print("Best Practices for Modules:")
print("=" * 80)
print("""
    1. USE SPECIFIC IMPORTS: Import only what you need
       ✓ from math import sqrt
       ✗ from math import *
       
    2. USE ALIASES WISELY: Use aliases for clarity and to avoid conflicts
       ✓ import numpy as np
       ✗ import something_with_long_name_as x
       
    3. ORGANIZE IMPORTS: Group imports logically
       - Standard library imports first
       - Third-party imports second
       - Local imports third
       
    4. CHECK MODULE DOCUMENTATION: Use help() and dir() to explore
       print(dir(module_name))
       help(module_name.function_name)
       
    5. UNDERSTAND NAMESPACES: Be aware of namespace conflicts
       
    6. USE __name__ == '__main__': Protect execution code
       if __name__ == '__main__':
           # Run code only when executed directly
           
    7. DOCUMENT YOUR MODULES: Include docstrings and comments
       
    8. AVOID CIRCULAR IMPORTS: Prevent module A importing B that imports A
       
    9. USE RELATIVE IMPORTS: In packages, use relative imports
       from . import module_name
       
    10. TEST YOUR MODULES: Write tests for your custom modules
""")

print()


#   dir() and help() Functions
print("=" * 80)
print("Exploring Modules with dir() and help():")
print("=" * 80)
print()

print("All attributes in math module:")
print(f"Number of attributes: {len(dir(math))}")
print()

print("Some useful math functions:")
useful = ['sqrt', 'pow', 'sin', 'cos', 'tan', 'log', 'exp', 'ceil', 'floor']
for func_name in useful:
    if hasattr(math, func_name):
        print(f"  ✓ {func_name}")

print()
print("Getting help about a specific function:")
print()

# Show help for math.sqrt
import inspect
sqrt_signature = inspect.signature(math.sqrt)
print(f"math.sqrt signature: {sqrt_signature}")
print(f"math.sqrt docstring: {math.sqrt.__doc__}")

print()


print("=" * 80)
print("SUMMARY OF MODULES")
print("=" * 80)
print("""
✓ Modules are .py files containing reusable code
✓ Import modules using 'import' or 'from ... import'
✓ Python has extensive standard library with many modules
✓ Use specific imports to avoid namespace pollution
✓ Create your own modules to organize code
✓ Use aliases to handle naming conflicts
✓ Use dir() to explore module contents
✓ Use help() to get documentation
✓ Organize imports in groups (stdlib, third-party, local)
✓ Follow best practices for clean, maintainable code
✓ Common modules: math, random, datetime, os, sys, json, re
✓ Custom modules enable code reusability and organization
""")
