
#   Data Types in Python

#   What are Data Types?
"""
    A data type is a classification that tells Python how to interpret and work
    with data values. Python has several built-in data types:
    
    - int: Integer numbers (whole numbers)
    - float: Floating-point numbers (decimals)
    - str: Strings (text)
    - bool: Booleans (True or False)
"""

print("=" * 80)
print("Data Types in Python:")
print("=" * 80)
print()


#   Integer Numbers (int)
"""
    Integer numbers are whole numbers without decimals.
    They can be positive, negative, or zero.
    In Python, they are represented by writing the number without quotes
    or decimal points.
"""

print("Example 1: Integer Numbers (int)")
print()

year = 2026
month = 1
day = 29
temperature = -5
count = 42

print(f"Year: {year} (type: {type(year).__name__})")
print(f"Month: {month} (type: {type(month).__name__})")
print(f"Day: {day} (type: {type(day).__name__})")
print(f"Temperature: {temperature} (type: {type(temperature).__name__})")
print(f"Count: {count} (type: {type(count).__name__})")
print(f"Date: {day}/{month}/{year}")
print()


#   Floating-point Numbers (float)
"""
    Floating-point numbers are numbers that have a decimal part.
    In Python, they are represented using a period to separate the integer part from the decimal part.
"""

print("Example 2: Floating-point Numbers (float)")
print()

price = 9.99
height = 1.75
temperature = 37.5
pi_approximation = 3.14159

print(f"Price: {price} (type: {type(price).__name__})")
print(f"Height: {height} (type: {type(height).__name__})")
print(f"Temperature: {temperature} (type: {type(temperature).__name__})")
print(f"Pi Approximation: {pi_approximation} (type: {type(pi_approximation).__name__})")
print()


#   Strings (str)
"""
    Strings are sequences of characters enclosed in single quotes ('...') or double quotes ("...").
    They are used to represent text in Python.
    You can include special characters using escape sequences like backslash-n for newline.
    For multiple-line strings, use triple quotes (triple single or triple double quotes).
"""

print("Example 3: Strings (str)")
print()

name = "Juan"
greeting = 'Hello, World!'
message = "Python is awesome!"
multi_line = """This is a
multi-line string
in Python"""

print(f"Name: {name} (type: {type(name).__name__})")
print(f"Greeting: {greeting} (type: {type(greeting).__name__})")
print(f"Message: {message} (type: {type(message).__name__})")
print(f"Multi-line: {multi_line}")
print()


#   Booleans (bool)
"""
    Boolean values represent truth values: True and False.
    They are commonly used in conditional expressions and logical operations.
    Booleans are the result of comparisons and logical operations.
"""

print("Example 4: Booleans (bool)")
print()

is_adult = True
has_discount = False
is_valid = 10 > 5

print(f"Is Adult: {is_adult} (type: {type(is_adult).__name__})")
print(f"Has Discount: {has_discount} (type: {type(has_discount).__name__})")
print(f"Is Valid (10 > 5): {is_valid} (type: {type(is_valid).__name__})")
print()


#   Type Checking
"""
    You can check the data type of a value using the type() function.
    This is useful for debugging and understanding your data.
"""

print("Example 5: Type Checking")
print()

values = [42, 3.14, "Hello", True, None]
for value in values:
    print(f"Value: {value}, Type: {type(value).__name__}")
print()


#   Type Conversion
"""
    Python allows you to convert values from one type to another using:
    - int(): Convert to integer
    - float(): Convert to floating-point
    - str(): Convert to string
    - bool(): Convert to boolean
"""

print("Example 6: Type Conversion")
print()

# String to integer
string_number = "123"
integer = int(string_number)
print(f"str '123' to int: {integer} (type: {type(integer).__name__})")

# Integer to float
integer_value = 10
float_value = float(integer_value)
print(f"int 10 to float: {float_value} (type: {type(float_value).__name__})")

# Float to integer (truncates decimal part)
float_number = 9.99
truncated = int(float_number)
print(f"float 9.99 to int: {truncated} (type: {type(truncated).__name__})")

# Number to string
number = 42
string = str(number)
print(f"int 42 to str: '{string}' (type: {type(string).__name__})")

print()


print("=" * 80)
print("SUMMARY OF DATA TYPES")
print("=" * 80)
print("""
[INT] Whole numbers without decimals (-5, 0, 100)
[FLOAT] Numbers with decimal points (3.14, 9.99, -2.5)
[STR] Text enclosed in quotes ('hello', "world")
[BOOL] True or False values
[TYPE] Use type() function to check data type
[CONVERT] Convert between types using int(), float(), str(), bool()
[DYNAMIC] Python infers data type automatically (dynamic typing)
[METHODS] Each type has specific operations and methods
[IMPORTANT] Understanding data types is crucial for error-free code
""")
