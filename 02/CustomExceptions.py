#   Custom Exceptions

#   What are Custom Exceptions?
"""
    Beyond the built-in exceptions in Python, you can also create your own custom
    exceptions. This is useful when you want to handle specific situations in your program.
    
    To create a custom exception, you must create a class that inherits from the base
    Exception class or one of its subclasses.
    
    Basic Syntax:
    class CustomException(Exception):
        pass
    
    Then you can raise it in your code:
    if condition:
        raise CustomException("Error description")
"""


#   Creating Simple Custom Exceptions
print("=" * 80)
print("Creating Simple Custom Exceptions:")
print("=" * 80)
print()

def custom_exception_function():
    """Function that can generate a custom exception."""
    value = 15
    # Code that can generate a custom exception
    if value < 0:
        raise Exception("Value cannot be negative!")
    if value > 100:
        raise Exception("Value exceeds maximum limit of 100!")
    return f"Valid value: {value}"


try:
    result = custom_exception_function()
    print(result)
except Exception as e:
    print(f"Error: {str(e)}")

print()

# Example with a negative value
print("Example with invalid value:")
print()

def validate_score(score):
    """Function that raises an exception for invalid scores."""
    if score < 0 or score > 100:
        raise Exception("Score must be between 0 and 100!")
    return f"Valid score: {score}"


try:
    result = validate_score(150)
    print(result)
except Exception as e:
    print(f"Error: {str(e)}")

print()


#   Creating Custom Exception Classes
"""
    For more advanced use cases, you can create custom exception classes that inherit
    from Exception and provide additional functionality.
"""

print("=" * 80)
print("Creating Custom Exception Classes:")
print("=" * 80)
print()

class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidEmailError(Exception):
    """Custom exception for invalid email."""
    def __init__(self, email):
        self.email = email
        self.message = f"Invalid email format: {email}"
        super().__init__(self.message)


def validate_user(name, age, email):
    """Function that validates user data using custom exceptions."""
    if age < 0 or age > 150:
        raise InvalidAgeError(f"Age must be between 0 and 150, got {age}")
    
    if "@" not in email or "." not in email:
        raise InvalidEmailError(email)
    
    return f"Valid user: {name}, Age: {age}, Email: {email}"


# Test the validation function
print("Test 1: Valid user")
try:
    result = validate_user("Alice", 30, "alice@example.com")
    print(result)
except InvalidAgeError as e:
    print(f"Age Error: {e}")
except InvalidEmailError as e:
    print(f"Email Error: {e}")

print()

print("Test 2: Invalid age")
try:
    result = validate_user("Bob", 200, "bob@example.com")
    print(result)
except InvalidAgeError as e:
    print(f"Age Error: {e}")
except InvalidEmailError as e:
    print(f"Email Error: {e}")

print()

print("Test 3: Invalid email")
try:
    result = validate_user("Charlie", 25, "charlie.invalid")
    print(result)
except InvalidAgeError as e:
    print(f"Age Error: {e}")
except InvalidEmailError as e:
    print(f"Email Error: {e}")

print()


#   More Custom Exception Examples
print("=" * 80)
print("Additional Custom Exception Examples:")
print("=" * 80)
print()

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass


class InvalidTransactionError(Exception):
    """Custom exception for invalid transactions."""
    pass


class BankAccount:
    """A simple bank account class with custom exceptions."""
    
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative!")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds! Available balance: ${self.balance}"
            )
        self.balance -= amount
        print(f"Withdrawal successful! New balance: ${self.balance}")
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative!")
        self.balance += amount
        print(f"Deposit successful! New balance: ${self.balance}")


# Using the custom exception
account = BankAccount("John Doe", 1000)

try:
    account.deposit(500)
except ValueError as e:
    print(f"Error: {e}")

try:
    account.withdraw(300)
except InsufficientFundsError as e:
    print(f"Error: {e}")

try:
    account.withdraw(2000)  # This will raise InsufficientFundsError
except InsufficientFundsError as e:
    print(f"Error: {e}")

print()


#   Complete Error Handling Workflow
"""
    The complete workflow for error handling in Python:
    
    1. Identify potential errors in your code
    2. Decide which errors to catch and how to handle them
    3. Use try-except blocks to capture exceptions
    4. Provide meaningful error messages
    5. Use finally for cleanup operations
    6. Log errors for debugging purposes
    
    This approach makes your programs more robust and reliable.
"""

print("=" * 80)
print("Complete Error Handling Workflow Example:")
print("=" * 80)
print()

class BankAccountWithLogging:
    """A bank account class with comprehensive error handling."""
    
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
        self.transaction_log = []
    
    def deposit(self, amount):
        """Deposit money with error handling."""
        try:
            # Validate input
            if not isinstance(amount, (int, float)):
                raise TypeError("Amount must be a number")
            
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            
            # Perform operation
            self.balance += amount
            self.transaction_log.append(f"DEPOSIT: +${amount}")
            print(f"✓ Deposit successful: +${amount}")
            
        except TypeError as e:
            print(f"✗ Type Error: {e}")
        except ValueError as e:
            print(f"✗ Validation Error: {e}")
        finally:
            print(f"  Current balance: ${self.balance}")
    
    def withdraw(self, amount):
        """Withdraw money with error handling."""
        try:
            # Validate input
            if not isinstance(amount, (int, float)):
                raise TypeError("Amount must be a number")
            
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            
            if amount > self.balance:
                raise ValueError(
                    f"Insufficient funds! Available: ${self.balance}"
                )
            
            # Perform operation
            self.balance -= amount
            self.transaction_log.append(f"WITHDRAW: -${amount}")
            print(f"✓ Withdrawal successful: -${amount}")
            
        except (TypeError, ValueError) as e:
            print(f"✗ Error: {e}")
        finally:
            print(f"  Current balance: ${self.balance}")
    
    def display_statement(self):
        """Display account statement."""
        print(f"\n{'=' * 50}")
        print(f"Account Statement")
        print(f"Account Number: {self.account_number}")
        print(f"Holder: {self.holder_name}")
        print(f"Balance: ${self.balance}")
        print(f"\nTransaction History:")
        for transaction in self.transaction_log:
            print(f"  - {transaction}")
        print(f"{'=' * 50}\n")


# Test the account
account = BankAccountWithLogging("123456", "John Smith", 1000)

print("Testing account operations:")
print()

account.deposit(500)
print()

account.withdraw(200)
print()

account.withdraw(2000)  # Insufficient funds
print()

account.deposit(-100)  # Invalid amount
print()

account.display_statement()


#   Key Takeaways
"""
    Error handling and exception management is a fundamental part of programming in Python.
    It allows you to handle unexpected situations in a controlled way and prevent your
    program from crashing or stopping abruptly.
    
    When an error occurs in your code, Python generates an exception. By using try-except
    blocks, you can catch and handle these exceptions appropriately. You can specify
    different except blocks to handle different types of exceptions and perform specific
    actions in each case.
    
    Additionally, the finally block allows you to execute cleanup code or resource release,
    regardless of whether an exception occurred or not. This is useful to ensure that
    certain actions are always performed, such as closing files or database connections.
    
    IMPORTANT:
    Consider the possible errors that can occur in your code and use appropriate exception
    handling to manage them correctly. This will make your programs more robust and reliable.
"""

print("=" * 80)
print("Key Principles for Robust Error Handling")
print("=" * 80)
print("""
    1. ANTICIPATE: Identify potential errors before they happen
    2. CATCH: Use try-except blocks to catch exceptions
    3. HANDLE: Provide meaningful error messages and recovery options
    4. CLEANUP: Use finally blocks to release resources
    5. LOG: Record errors for debugging and monitoring
    6. TEST: Test error scenarios to ensure proper handling
    7. CUSTOM: Create custom exceptions for specific scenarios
    
    Remember: Good error handling makes your code more reliable!
""")

print("=" * 80)
print("SUMMARY OF CUSTOM EXCEPTIONS")
print("=" * 80)
print("""
✓ Create custom exceptions for application-specific errors
✓ Custom exceptions inherit from the Exception class
✓ Use meaningful exception names and messages
✓ Custom exceptions improve code clarity and maintainability
✓ Combine custom exceptions with try-except blocks
✓ Use finally blocks for resource cleanup
✓ Log custom exceptions for debugging
✓ Test custom exception scenarios
✓ Follow best practices for exception handling
✓ Build more robust and reliable applications
""")
