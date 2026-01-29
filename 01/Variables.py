#   Variables

#   What are variables?
"""
    Variables are containers that allow us to store and manipulate data in our programs.
    You can think of a variable as a label that you assign to a specific value.
    In Python, you don't need to declare the data type of a variable in advance,
    as Python automatically infers the data type based on the assigned value.
"""


#   Variable Declaration and Assignment
"""
    To declare and assign a value to a variable in Python, we use the assignment operator (=).
    The variable name goes on the left side of the operator,
    and the value you want to assign goes on the right side.
"""

# Example: Basic variable declaration and assignment
name = "Juan"
age = 25
height = 1.75
is_student = True

print("Variable Declaration and Assignment:")
print(f"name: {name} (type: {type(name).__name__})")
print(f"age: {age} (type: {type(age).__name__})")
print(f"height: {height} (type: {type(height).__name__})")
print(f"is_student: {is_student} (type: {type(is_student).__name__})")
print()

# Multiple assignment: assign the same value to multiple variables
a = b = c = 10
print("Multiple Assignment:")
print(f"a: {a}, b: {b}, c: {c}")
print()


#   Rules for Naming Variables
"""
    When naming variables in Python, it is important to follow some rules
    to keep your code readable and avoid errors:
    
    1. Variable names can only contain letters (a-z, A-Z), numbers (0-9), and underscores (_).
       They cannot start with a number.
    
    2. Python is case-sensitive, so 'name' and 'Name' are different variables.
    
    3. You cannot use Python reserved keywords as variable names
       (for example: if, else, for, while, etc.).
    
    4. Use descriptive names that clearly indicate their purpose:
       age, full_name, total_sales, etc.
"""

# Valid variable names:
print("Valid Variable Names:")
age = 30
full_name = "Pepito Pepitez"
total_sales = 5000.50
_counter = 0
student_id_001 = 12345

print(f"age: {age}")
print(f"full_name: {full_name}")
print(f"total_sales: {total_sales}")
print(f"_counter: {_counter}")
print(f"student_id_001: {student_id_001}")
print()

# Invalid variable names (these would cause errors if you tried to run them):
print("Invalid Variable Names (Examples - DO NOT USE):")
print("1age")            # Cannot start with a number
print("full-name")       # Uses hyphen instead of underscore
print("if")              # Reserved Python keyword
print()

print("Important: Choose descriptive names for your variables!")
print("This makes your code easier to read and understand for you and other developers.")
