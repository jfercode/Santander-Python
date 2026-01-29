
#   Functions

#   What are functions?
"""
    Functions are reusable blocks of code that allow us to encapsulate specific tasks
    and execute them when necessary. Functions help us organize our code, avoid
    repetition, and make our programs more modular and easier to maintain.
    
    A function is a named block of code that performs a specific task and can be
    called multiple times from different parts of the program.
"""


#   Definition and Calling of Functions
"""
    To define a function in Python, we use the keyword 'def' followed by the function
    name and parentheses. Optionally, we can specify parameters within the parentheses.
    The code block of the function is indented after the colon.
    
    To call a function, we simply write the function name followed by parentheses:
    
    Syntax:
    def function_name():
        # Code block (indented)
        instructions
    
    function_name()  # Function call
"""

print("Definition and Calling of Functions Example:")
print()


def greeting():
    """A simple function that prints a greeting."""
    print("Hello, World!")


# Calling the function
greeting()  # Prints "Hello, World!"

print()


#   Parameters and Arguments
"""
    Functions can accept parameters, which are values passed to the function when
    it is called. Parameters are specified within the parentheses in the function
    definition.
    
    When calling the function, we provide the arguments corresponding to the parameters:
    
    Syntax:
    def function_name(parameter1, parameter2):
        # Code block
        instructions
    
    function_name(argument1, argument2)  # Function call with arguments
"""

print("Parameters and Arguments Example:")
print()


def personalized_greeting(name):
    """A function that receives a parameter."""
    print(f"Hello, {name}!")


# Calling the function with arguments
personalized_greeting("Juan")    # Prints "Hello, John!"
personalized_greeting("María")   # Prints "Hello, Mary!"

print()


# Functions with multiple parameters
def add_numbers(a, b):
    """A function that adds two numbers."""
    total = a + b
    print(f"Sum of {a} + {b} = {total}")


add_numbers(5, 3)
add_numbers(10, 20)

print()

# Functions with default parameters
"""
    We can specify default values for parameters. If an argument is not provided
    when calling the function, the default value will be used.
"""

def power(base, exponent=2):
    """A function with a default parameter value."""
    result = base ** exponent
    print(f"{base} raised to the power of {exponent} = {result}")


power(5)        # Uses the default value of exponent (2)
power(5, 3)     # Specifies the value of exponent

print()


#   Return Values
"""
    Functions can return values using the 'return' keyword. The return value can
    be used by the code that calls the function.
    
    Syntax:
    def function_name(parameters):
        # Code block
        return value
    
    variable = function_name(arguments)  # The return value is assigned to a variable
"""

print("Return Values Example:")
print()


def sum_func(a, b):
    """A function that returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """A function that returns the subtraction of two numbers."""
    return a - b


def multiply(a, b):
    """A function that returns the multiplication of two numbers."""
    return a * b


def divide(a, b):
    """A function that returns the division of two numbers."""
    if b == 0:
        return "Error: Division by zero"
    return a / b


# Using return values
result1 = sum_func(3, 4)
print(f"Sum: {result1}")  # Prints 7

result2 = subtract(10, 5)
print(f"Subtraction: {result2}")  # Prints 5

result3 = multiply(6, 7)
print(f"Multiplication: {result3}")  # Prints 42

result4 = divide(20, 4)
print(f"Division: {result4}")  # Prints 5.0

print()

# Functions that return multiple values
"""
    A function can return multiple values using a tuple. These values can be
    unpacked into separate variables.
"""

def operations(a, b):
    """A function that returns multiple values."""
    sum_result = a + b
    subtract_result = a - b
    multiply_result = a * b
    return sum_result, subtract_result, multiply_result


s, r, m = operations(10, 5)
print("Operations with 10 and 5:")
print(f"Sum: {s}, Subtraction: {r}, Multiplication: {m}")

print()


#   Anonymous Functions (lambda)
"""
    Python allows us to create anonymous functions or lambda functions, which are
    functions without a name defined on a single line. They are commonly used for
    small and concise functions.
    
    Syntax:
    lambda arguments: expression
    
    Lambda functions are often used with functions like map(), filter(), and sorted()
"""

print("Anonymous Functions (lambda) Example:")
print()

# Lambda function to calculate the square
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")  # Prints 25

# Lambda function to multiply two numbers
multiply_lambda = lambda x, y: x * y
print(f"Multiplication of 4 * 6: {multiply_lambda(4, 6)}")  # Prints 24

# Lambda function with conditionals
rate_grade = lambda grade: "Passed" if grade >= 6 else "Failed"
print(f"Grade 7: {rate_grade(7)}")      # Prints "Passed"
print(f"Grade 4: {rate_grade(4)}")      # Prints "Failed"

print()

# Using lambda with map()
"""
    map() applies a function to each element of a sequence and returns a new sequence
"""
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# Using lambda with filter()
"""
    filter() creates a new sequence with elements that meet a condition
"""
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

print()


#   Variable Scope (local vs. global)
"""
    Variables defined inside a function have a local scope, which means they are
    only accessible within the function. On the other hand, variables defined
    outside any function have a global scope and can be accessed from anywhere
    in the program.
    
    Local scope: Variables inside a function
    Global scope: Variables outside any function
"""

print("Variable Scope (local vs. global) Example:")
print()

# Global variable
global_variable = 20


def local_function():
    """A function that uses a local variable."""
    local_variable = 10
    print(f"Local variable inside the function: {local_variable}")
    print(f"Global variable inside the function: {global_variable}")


def global_access_function():
    """A function that accesses the global variable."""
    print(f"Accessing the global variable: {global_variable}")


# Calling the functions
local_function()         # Prints 10 and 20
global_access_function() # Prints 20

print(f"Global variable outside the function: {global_variable}")  # Prints 20

print()

# Attempting to access a local variable outside its scope (error)
print("Note: Accessing 'variable_local' outside the function would cause an error")
print("because it is only defined within the function's scope.")

print()


#   Modifying Global Variables from a Function
"""
    To modify a global variable from within a function, we must use the 'global'
    keyword before the variable name.
"""

print("Modifying Global Variables Example:")
print()

contador = 0


def increment():
    """A function that modifies a global variable using 'global'."""
    global contador
    contador += 1
    print(f"Counter: {contador}")


increment()  # Counter: 1
increment()  # Counter: 2
increment()  # Counter: 3

print()


#   Documentation of Functions (docstrings)
"""
    It is a good practice to document our functions using docstrings. Docstrings
    are text strings that describe the purpose, parameters, and return value of
    a function. They are placed immediately after the function definition and are
    enclosed in triple double quotes.
    
    This helps other developers (and your future self) understand what a function
    does without having to read the entire code.
"""

print("Documentation of Functions (docstrings) Example:")
print()


def rectangle_area(base, height):
    """
    Calculates the area of a rectangle.
    
    Args:
        base (float): The base of the rectangle.
        height (float): The height of the rectangle.
    
    Returns:
        float: The area of the rectangle.
    """
    return base * height


# Using the function
area = rectangle_area(5, 10)
print(f"Area of rectangle with base 5 and height 10: {area}")

# Accessing the docstring
print(f"Function documentation:\n{rectangle_area.__doc__}")

print()


#   Functions with Variable Number of Arguments
"""
    Python allows us to define functions that accept a variable number of arguments.
    This is achieved by using the * operator before the parameter name.
    
    Syntax:
    def function_name(*args):
        # args is a tuple containing all arguments
        instructions
"""

print("Functions with Variable Number of Arguments Example:")
print()


def variable_sum(*numbers):
    """A function that accepts a variable number of arguments."""
    total = 0
    for number in numbers:
        total += number
    return total


result1 = variable_sum(1, 2, 3)
print(f"variable_sum(1, 2, 3) = {result1}")  # Prints 6

result2 = variable_sum(4, 5, 6, 7)
print(f"variable_sum(4, 5, 6, 7) = {result2}")  # Prints 22

result3 = variable_sum(10, 20, 30, 40, 50)
print(f"variable_sum(10, 20, 30, 40, 50) = {result3}")  # Prints 150

print()


#   Practical Example: Simple Calculator
"""
    Let's create a practical example that demonstrates the use of functions
    to build a simple calculator program.
"""

print("Practical Example: Simple Calculator")
print()


def calc_add(a, b):
    return a + b


def calc_subtract(a, b):
    return a - b


def calc_multiply(a, b):
    return a * b


def calc_divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# Using the calculator functions
print("Calculator Results:")
print(f"5 + 3 = {calc_add(5, 3)}")
print(f"10 - 4 = {calc_subtract(10, 4)}")
print(f"6 * 7 = {calc_multiply(6, 7)}")
print(f"20 / 4 = {calc_divide(20, 4)}")
print(f"20 / 0 = {calc_divide(20, 0)}")

print()

print("=" * 80)
print("SUMMARY OF FUNCTIONS")
print("=" * 80)
print("""
✓ Functions encapsulate reusable code
✓ Parameters allow us to customize function behavior
✓ The return statement returns values to the caller
✓ Lambda functions are useful for small operations
✓ Variable scope can be local or global
✓ The 'global' keyword allows modifying global variables from within a function
✓ Functions improve code organization and maintainability
✓ Docstrings provide documentation for functions
✓ Functions are a fundamental tool in programming
✓ Python also provides built-in functions like print(), len(), range(), etc.
""")
