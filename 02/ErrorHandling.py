#   Error Handling

#   What is Exception Handling?
"""
    When we write programs, it is common to encounter unexpected situations or errors
    during execution. Python provides a mechanism to handle these errors in a controlled
    way using exception handling. This allows us to capture and handle specific errors
    without the program stopping abruptly.
    
    Exception handling is a way to gracefully deal with errors and prevent program crashes.
    Instead of stopping execution, we can catch the error, handle it, and continue running
    the program or display a user-friendly error message.
"""


#   Common Errors in Python
"""
    Before diving into exception handling, let's look at some common errors you may
    encounter in Python:
    
    1. SyntaxError: Occurs when Python cannot parse the code (invalid syntax)
    2. NameError: Occurs when trying to use a variable that hasn't been defined
    3. TypeError: Occurs when an operation is applied to an object of inappropriate type
    4. IndexError: Occurs when trying to access an index that doesn't exist
    5. ValueError: Occurs when a function receives an argument of the right type but inappropriate value
    6. KeyError: Occurs when trying to access a key that doesn't exist in a dictionary
    7. ZeroDivisionError: Occurs when trying to divide by zero
    8. FileNotFoundError: Occurs when trying to open a file that doesn't exist
    
    When an error occurs, Python generates an exception and displays an error message
    that includes the exception type and a description of the problem.
"""

print("Common Errors in Python:")
print()

#   Example 1: NameError
print("1. NameError - Using an undefined variable:")
try:
    # This would cause a NameError if not inside try-except
    # print(undefined_variable)
    print("   Would occur if we try to use a variable that doesn't exist")
except NameError as e:
    print(f"   Error caught: {e}")

print()

#   Example 2: TypeError
print("2. TypeError - Operating on incompatible types:")
try:
    result = "Hello" + 5  # Cannot concatenate string and integer
except TypeError as e:
    print(f"   Error caught: {type(e).__name__}: {e}")

print()

#   Example 3: IndexError
print("3. IndexError - Accessing non-existent list index:")
try:
    my_list = [1, 2, 3]
    value = my_list[10]  # Index 10 doesn't exist
except IndexError as e:
    print(f"   Error caught: {type(e).__name__}: {e}")

print()

#   Example 4: ZeroDivisionError
print("4. ZeroDivisionError - Division by zero:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"   Error caught: {type(e).__name__}: {e}")

print()


#   Try-Except Block
"""
    The try-except block is the fundamental structure for exception handling.
    
    Syntax:
    try:
        # Code that might raise an exception
        statements
    except ExceptionType:
        # Code to handle the exception
        statements
    
    The code inside the try block is executed. If an exception of type ExceptionType
    occurs, the code inside the except block is executed. If no exception occurs,
    the except block is skipped.
"""

print("=" * 80)
print("Try-Except Block Examples:")
print("=" * 80)
print()

#   Example 1: Basic try-except
print("Example 1: Basic try-except block")

try:
    age = int(input("Enter your age (or press Enter to skip): ") or "25")
    print(f"Your age: {age}")
except ValueError:
    print("Invalid input! Please enter a valid number.")

print()

#   Example 2: Handling multiple exception types
print("Example 2: Handling multiple exception types")

numbers = [1, 2, 3, 4, 5]

try:
    index = int(input("Enter an index (0-4) (or press Enter to skip): ") or "0")
    result = numbers[index]
    print(f"Value at index {index}: {result}")
except ValueError:
    print("Error: Please enter a valid integer.")
except IndexError:
    print("Error: Index out of range! The list only has 5 elements.")

print()

#   Example 3: Generic exception handling
print("Example 3: Generic exception handling (catch all)")

try:
    # Some operation
    x = 10
    y = 0
    result = x / y
    print(f"Result: {result}")
except Exception as e:
    print(f"An unexpected error occurred: {type(e).__name__}: {e}")

print()


#   The Finally Block
"""
    The finally block is optional and is executed regardless of whether an exception
    occurred or not. It is useful for cleanup operations such as closing files or
    releasing resources.
    
    Syntax:
    try:
        # Code that might raise an exception
        statements
    except ExceptionType:
        # Code to handle the exception
        statements
    finally:
        # Code that always executes
        statements
"""

print("=" * 80)
print("Finally Block Example:")
print("=" * 80)
print()

def divide_numbers(a, b):
    """A function that demonstrates the finally block."""
    try:
        result = a / b
        print(f"Division result: {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    finally:
        print("Cleanup: This code always executes")
        print()


divide_numbers(10, 2)
divide_numbers(10, 0)


#   The Else Block
"""
    The else block is executed if no exception occurs in the try block.
    It is useful when you want to execute code only if the try block succeeds.
    
    Syntax:
    try:
        # Code that might raise an exception
        statements
    except ExceptionType:
        # Code to handle the exception
        statements
    else:
        # Code that executes if no exception occurs
        statements
"""

print("=" * 80)
print("Else Block Example:")
print("=" * 80)
print()

def process_number(value):
    """A function that demonstrates the else block."""
    try:
        number = int(value)
    except ValueError:
        print(f"Error: '{value}' is not a valid number.")
    else:
        # This executes only if no exception occurred
        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")


process_number("42")
process_number("invalid")
process_number("7")

print()


#   Best Practices for Error Handling
"""
    1. Be specific with exception types - catch only the exceptions you expect
    2. Don't use bare except clauses - always specify the exception type
    3. Use finally for cleanup operations (closing files, releasing resources)
    4. Provide meaningful error messages
    5. Log errors for debugging purposes
    6. Raise exceptions when appropriate in your own code
    7. Don't suppress exceptions silently without good reason
    8. Use custom exceptions for application-specific errors
"""

print("=" * 80)
print("Best Practices Example:")
print("=" * 80)
print()

def safe_divide(a, b):
    """
    A function that follows best practices for exception handling.
    
    Args:
        a (float): The dividend
        b (float): The divisor
    
    Returns:
        float: The result of division, or None if an error occurred
    """
    try:
        # Validate inputs
        a = float(a)
        b = float(b)
        
        # Perform operation
        result = a / b
        print(f"Division successful: {a} / {b} = {result}")
        return result
    
    except ValueError:
        print("Error: Both arguments must be numbers.")
        return None
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    
    except TypeError as e:
        print(f"Error: Invalid type - {e}")
        return None
    
    finally:
        print("Division operation completed.")


safe_divide(10, 2)
safe_divide(10, 0)
safe_divide("10", "two")

print()

print("=" * 80)
print("SUMMARY OF ERROR HANDLING")
print("=" * 80)
print("""
✓ Exception handling allows us to handle errors gracefully
✓ Use try-except blocks to catch and handle exceptions
✓ The finally block executes regardless of exceptions
✓ The else block executes only if no exception occurs
✓ Be specific with exception types when catching errors
✓ Provide meaningful error messages
✓ Use finally for cleanup operations
✓ Follow best practices to write robust, maintainable code
""")
