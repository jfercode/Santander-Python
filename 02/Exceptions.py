#   Exceptions in Python

#   What are Exceptions?
"""
    Exceptions are events that occur during the execution of a program that disrupts
    the normal flow of the program's instructions. Python has built-in mechanisms to
    handle these exceptions.
    
    An exception is not necessarily an error. Sometimes exceptions are used to signal
    special conditions or to control the flow of a program.
"""


#   The Raise Statement
"""
    The raise statement allows us to manually raise an exception. This is useful
    when we want to signal that an error has occurred in our code.
    
    Syntax:
    raise ExceptionType("Error message")
"""

print("=" * 80)
print("Raise Statement Example:")
print("=" * 80)
print()

def validate_age(age):
    """A function that raises an exception if age is invalid."""
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return f"Valid age: {age}"


# Testing the function
try:
    print(validate_age(25))
    print(validate_age(-5))  # This will raise an exception
except ValueError as e:
    print(f"Validation error: {e}")

try:
    print(validate_age(200))  # This will raise an exception
except ValueError as e:
    print(f"Validation error: {e}")

print()


#   Detailed: Try, Except, and Finally
print("=" * 80)
print("Detailed: Try, Except, and Finally")
print("=" * 80)
print()

#   Try Block in Detail
"""
    The try block contains the code that might generate an exception. If an exception
    occurs within the try block, the execution flow is transferred to the corresponding
    except block.
    
    Syntax:
    try:
        # Code that might generate an exception
        statements
"""

print("1. Try Block - Code that might generate an exception:")
print()

try:
    # Code that can generate an exception
    result = 10 / 0  # Division by zero
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero")

print()


#   Except Block in Detail
"""
    The except block specifies the type of exception you want to catch and handle.
    You can have multiple except blocks to handle different types of exceptions.
    
    Syntax:
    try:
        # Code that might generate an exception
        statements
    except ExceptionType1:
        # Handle ExceptionType1
        statements
    except ExceptionType2:
        # Handle ExceptionType2
        statements
"""

print("2. Except Block - Handling multiple exception types:")
print()

try:
    # Code that can generate an exception
    result = 10 / 0  # Division by zero
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid value")

print()

# Another example with multiple exceptions
print("3. Multiple except blocks - Handling different scenarios:")
print()

def process_data(data_type, value):
    """Function that demonstrates handling multiple exceptions."""
    try:
        if data_type == "divide":
            result = 10 / int(value)
            print(f"Division result: {result}")
        elif data_type == "convert":
            number = int(value)
            print(f"Converted to integer: {number}")
        elif data_type == "access":
            my_list = [1, 2, 3]
            element = my_list[int(value)]
            print(f"Element: {element}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Invalid value provided")
    except IndexError:
        print("Error: Index out of range")


process_data("divide", 0)
process_data("convert", "abc")
process_data("access", 10)

print()


#   Finally Block in Detail
"""
    The finally block is optional and is executed always, regardless of whether
    an exception occurred or not. It is commonly used for cleanup tasks or resource
    release operations.
    
    Important: The finally block executes even if:
    - An exception occurs and is handled by except
    - An exception occurs and is not handled
    - No exception occurs (normal execution)
    - There is a return statement in try or except
    
    Syntax:
    try:
        # Code that might generate an exception
        statements
    except ExceptionType:
        # Handle exception
        statements
    finally:
        # Cleanup code that always runs
        statements
"""

print("=" * 80)
print("4. Finally Block - Code that always executes:")
print("=" * 80)
print()

def file_operations():
    """Demonstrates the finally block with file operations."""
    print("Attempting to open a file...")
    try:
        # Code that can generate an exception
        archivo = open("archivo.txt", "r")
        # Perform operations with the file
        content = archivo.read()
        print(f"File content: {content}")
    except FileNotFoundError:
        print("Error: File not found")
    finally:
        # Always close the file, even if an exception occurs
        print("Closing file resources...")
        # In a real scenario, you would close the file here
        # archivo.close()


file_operations()

print()

# Another example: Finally with successful execution
print("5. Finally block with successful try execution:")
print()

def calculate_with_cleanup(a, b):
    """Function demonstrating finally block with successful execution."""
    try:
        print(f"Attempting to divide {a} by {b}")
        result = a / b
        print(f"Result: {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    finally:
        print("Cleanup: Finalizing calculation...")
        print()


calculate_with_cleanup(10, 2)
calculate_with_cleanup(10, 0)

print()

# Example: Finally block with early return
print("6. Finally block with early return statement:")
print()

def check_age(age):
    """Function demonstrating finally block with return statements."""
    try:
        age_int = int(age)
        if age_int < 0:
            raise ValueError("Age cannot be negative")
        if age_int >= 18:
            return "Adult"
        else:
            return "Minor"
    except ValueError as e:
        print(f"Error: {e}")
        return None
    finally:
        # This executes even with return statements above
        print("Age check completed")


result1 = check_age(25)
print(f"Result: {result1}")
print()

result2 = check_age(-5)
print(f"Result: {result2}")
print()


#   Complete Example: Try-Except-Finally
"""
    A complete example showing try, except, and finally working together.
"""

print("=" * 80)
print("7. Complete Example: Try-Except-Finally")
print("=" * 80)
print()

class FileProcessor:
    """A class that demonstrates complete exception handling."""
    
    @staticmethod
    def process_file(filename):
        """Process a file with proper exception handling."""
        file_object = None
        try:
            print(f"Opening file: {filename}")
            file_object = open(filename, "r")
            
            print("Reading file contents...")
            lines = file_object.readlines()
            
            print(f"File has {len(lines)} lines")
            for i, line in enumerate(lines, 1):
                print(f"  Line {i}: {line.strip()}")
                
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
        except IOError as e:
            print(f"Error reading file: {e}")
        except Exception as e:
            print(f"Unexpected error: {type(e).__name__}: {e}")
        finally:
            print("Cleanup: Closing file resources")
            if file_object is not None:
                file_object.close()
            print("File operation completed")
            print()


# Test the file processor
FileProcessor.process_file("nonexistent.txt")

print()


#   Exception Hierarchy
"""
    Python exceptions follow a hierarchy. All built-in exceptions inherit from
    the BaseException class. Understanding this hierarchy helps in catching
    specific exceptions.
    
    The most common exceptions inherit from the Exception class:
    - BaseException (top of the hierarchy)
        - Exception (most exceptions inherit from this)
            - ValueError
            - TypeError
            - IndexError
            - KeyError
            - etc.
        - KeyboardInterrupt (Ctrl+C)
        - SystemExit (sys.exit())
"""

print("=" * 80)
print("Exception Hierarchy Example:")
print("=" * 80)
print()

def demonstrate_exception_hierarchy():
    """Shows how to catch exceptions at different levels."""
    try:
        # This could raise various exceptions
        data = {"name": "Alice", "age": "thirty"}
        age = int(data["age"])  # ValueError: invalid literal
    except ValueError as e:
        print(f"ValueError caught: {e}")
    except KeyError as e:
        print(f"KeyError caught: {e}")
    except Exception as e:
        print(f"Generic Exception caught: {type(e).__name__}: {e}")


demonstrate_exception_hierarchy()

print()

print("=" * 80)
print("SUMMARY OF EXCEPTIONS")
print("=" * 80)
print("""
✓ Exceptions are events that disrupt normal program flow
✓ Use raise to manually raise exceptions
✓ Use try-except blocks to catch and handle exceptions
✓ The finally block executes regardless of exceptions
✓ Multiple except blocks handle different exception types
✓ Finally blocks are useful for cleanup operations
✓ Exception hierarchy helps in specific exception catching
✓ Provide meaningful error messages in exceptions
✓ Use exception handling for I/O operations
✓ Follow best practices to write robust code
""")
