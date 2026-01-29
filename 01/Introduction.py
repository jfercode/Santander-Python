
#   Introduction to Python

#   What is Python?
"""
    Python is a high-level, interpreted programming language known for its simplicity
    and readability. It was created by Guido van Rossum and first released in 1991.
    Python is widely used for:
    
    - Web development
    - Data science and machine learning
    - Automation and scripting
    - Scientific computing
    - Game development
    - And much more!
"""

print("=" * 80)
print("Introduction to Python:")
print("=" * 80)
print()


#   Running Python Scripts
"""
    To run a Python script, use the following command in your terminal:
    
    python filename.py
    
    Python is an interpreted language, which means:
    - No compilation step is needed
    - Code is executed directly from the .py file
    - Errors are detected at runtime (when code runs)
"""

print("=" * 80)
print("Basic Python Concepts:")
print("=" * 80)
print()

# Example 1: Simple print statement
print("Example 1: Using print() to output text")
print("Hello World!")
print()


#   Comments in Python
"""
    Comments are lines of text that Python ignores when running code.
    They are useful for explaining what your code does.
    
    Types of comments:
    1. Single-line comments: Start with #
    2. Multi-line comments: Use triple quotes (triple single or triple double quotes)
"""

print("Example 2: Comments in Python")
print()

# This is a single-line comment
# Python ignores everything after the # symbol

"""
    This is a multi-line comment using triple quotes.
    It can span multiple lines without needing # on each line.
    This is often used for documentation and docstrings.
"""

print("Comments help explain code and make programs more readable!")
print()


#   Variables and Basic Data Types
"""
    A variable is a container for storing data values.
    Python automatically determines the data type based on the value assigned.
    
    Basic data types in Python:
    - int: Integers (whole numbers)
    - float: Floating-point numbers (decimals)
    - str: Strings (text)
    - bool: Booleans (True or False)
"""

print("Example 3: Variables and Basic Data Types")
print()

name = "Alice"
age = 25
height = 5.7
is_student = True

print(f"Name: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Height: {height} (type: {type(height).__name__})")
print(f"Is Student: {is_student} (type: {type(is_student).__name__})")
print()


#   Case Sensitivity
"""
    Python is case-sensitive, which means:
    - 'Variable' and 'variable' are different variables
    - 'print' and 'Print' are different
    - 'True' and 'true' are different (True is correct)
"""

print("Example 4: Case Sensitivity")
print()

Variable = 0
VARIABLE = 1
variable = 2

print(f"Variable = {Variable}")
print(f"VARIABLE = {VARIABLE}")
print(f"variable = {variable}")
print("Note: These are three different variables because Python is case-sensitive")
print()


#   Operator Precedence
"""
    Operator precedence determines which calculations are performed first.
    Parentheses () have the highest precedence and are evaluated first.
    
    General precedence order:
    1. Parentheses ()
    2. Exponentiation **
    3. Multiplication, Division, Modulo *, /, //, %
    4. Addition, Subtraction +, -
"""

print("Example 5: Operator Precedence")
print()

a = 2
b = 3
c = 4

result1 = (a + b) * c
result2 = a + b * c

print(f"With parentheses: ({a} + {b}) * {c} = {result1}")
print(f"Without parentheses: {a} + {b} * {c} = {result2}")
print("Notice how parentheses change the order of operations!")
print()


#   Conditional Statements
"""
    Conditional statements allow us to execute different code based on conditions.
    The main conditional structure is if-else.
    
    Syntax:
    if condition:
        # Code executes if condition is True
    else:
        # Code executes if condition is False
"""

print("Example 6: Conditional Statements (if-else)")
print()

age = 18

if age >= 18:
    print(f"Age: {age} - You are an adult!")
else:
    print(f"Age: {age} - You are a minor!")
print()


#   Input and Output
"""
    Python allows interaction with users through:
    - print(): Output text to the console
    - input(): Get text input from the user
    - f-strings: Format strings with variables
"""

print("Example 7: String Formatting")
print()

first_name = "John"
last_name = "Doe"
birth_year = 1995

current_year = 2026
age = current_year - birth_year

print(f"Name: {first_name} {last_name}")
print(f"Age: {age} years old")
print()


print("=" * 80)
print("SUMMARY OF INTRODUCTION")
print("=" * 80)
print("""
✓ Python is a simple, readable programming language
✓ Use print() to display output
✓ Use # for single-line comments
✓ Use triple quotes for multi-line comments
✓ Variables store data values
✓ Python is case-sensitive
✓ Parentheses control operator precedence
✓ if-else statements make decisions
✓ f-strings format text with variables
✓ Python is beginner-friendly and powerful
""")


