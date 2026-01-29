#   Input and Output Operations

#   What is Input and Output?
"""
    In Python, input and output operations allow us to interact with the user and
    manipulate files. We can request information from the user, display results on
    the screen, and read or write data in external files.
    
    Input (I): Getting data from the user or from files
    Output (O): Displaying data to the user or writing to files
    
    These operations are fundamental for creating interactive programs.
"""


#   User Input
"""
    To obtain information from the user during program execution, we can use the
    input() function. This function displays a message on the screen and waits for
    the user to enter a value.
    
    Syntax:
    variable = input("Prompt message: ")
    
    Important: The input() function always returns a string (text). If you want to
    work with other data types like integers or floats, you must perform an explicit
    conversion using functions like int() or float().
"""

print("=" * 80)
print("User Input Examples:")
print("=" * 80)
print()

# Example 1: Basic user input
print("Example 1: Basic user input (storing as strings)")
print()

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello, " + name + "!")
print("You are " + age + " years old.")

print()


# Example 2: Converting input to integers
print("Example 2: Converting input to integers")
print()

birth_year = int(input("Enter your birth year: "))
current_year = 2026
age_calculated = current_year - birth_year

print(f"You were born in {birth_year}")
print(f"You are approximately {age_calculated} years old")

print()


# Example 3: Converting input to floats
print("Example 3: Converting input to floats (decimal numbers)")
print()

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

print(f"Your height: {height} m")
print(f"Your weight: {weight} kg")

print()


# Example 4: Input with conditionals
print("Example 4: Conditional logic based on user input")
print()

age_input = int(input("Enter your age: "))

if age_input >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

print()


# Example 5: Multiple inputs for calculation
print("Example 5: Multiple inputs for arithmetic operations")
print()

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "undefined"

print(f"\nResults:")
print(f"Sum: {num1} + {num2} = {sum_result}")
print(f"Product: {num1} * {num2} = {product}")
print(f"Division: {num1} / {num2} = {quotient}")

print()


#   Output with Print Function
"""
    To display information on the screen, we use the print() function. This function
    takes one or more arguments and displays them in the console.
    
    Syntax:
    print(value1, value2, ..., sep=" ", end="\n")
    
    Parameters:
    - value1, value2, ...: Values to print
    - sep: Separator between values (default is space)
    - end: Character at the end of the line (default is newline)
"""

print("=" * 80)
print("Print Function Examples:")
print("=" * 80)
print()

# Example 1: Basic print statements
print("Example 1: Basic print statements")
print()

print("Hello, World!")
print("Python is awesome!")
print("Learning Python is fun!")

print()


# Example 2: Printing multiple values
print("Example 2: Printing multiple values with separator")
print()

print("apple", "banana", "orange")
print("apple", "banana", "orange", sep=", ")
print("apple", "banana", "orange", sep=" | ")

print()


# Example 3: Controlling the end character
print("Example 3: Controlling the end character")
print()

print("Loading", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(" Complete!")

print()


# Example 4: Printing with tabs and newlines
print("Example 4: Special characters in print")
print()

print("Name\tAge\tCity")
print("John\t25\tNew York")
print("Maria\t30\tLos Angeles")
print("Carlos\t28\tMiami")

print()


#   String Formatting with F-Strings
"""
    F-strings (formatted string literals) provide a concise and readable way to embed
    expressions inside string literals. They are prefixed with an 'f' and use curly
    braces {} to embed variables and expressions.
    
    Syntax:
    f"text {variable} more text"
    f"expression: {expression}"
    f"formatted: {variable:format}"
"""

print("=" * 80)
print("F-String Formatting Examples:")
print("=" * 80)
print()

# Example 1: Basic f-string
print("Example 1: Basic variable embedding with f-strings")
print()

name = "Alice"
age = 28
city = "Boston"

print(f"Hello, my name is {name} and I am {age} years old.")
print(f"I live in {city}.")

print()


# Example 2: Expressions in f-strings
print("Example 2: Expressions within f-strings")
print()

x = 10
y = 20

print(f"The sum of {x} and {y} is {x + y}")
print(f"The product of {x} and {y} is {x * y}")
print(f"The average of {x} and {y} is {(x + y) / 2}")

print()


# Example 3: Formatting numbers
print("Example 3: Number formatting with f-strings")
print()

pi = 3.14159265
price = 19.99

print(f"Pi rounded to 2 decimals: {pi:.2f}")
print(f"Price: ${price:.2f}")
print(f"Large number: {1000000:,}")
print(f"Percentage: {0.75:.0%}")

print()


# Example 4: String alignment
print("Example 4: String alignment")
print()

product = "Laptop"
cost = 999.99

print(f"{product:<20} ${cost:>8.2f}")
print(f"{product:^20} ${cost:^8.2f}")
print(f"{product:>20} ${cost:<8.2f}")

print()


#   Combining Input and Output
print("=" * 80)
print("Combining Input and Output - Interactive Program:")
print("=" * 80)
print()

def create_profile():
    """Create a user profile with input and output."""
    print("Welcome to the User Profile Creator!")
    print()
    
    # Get user information
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = int(input("Age: "))
    email = input("Email: ")
    salary = float(input("Annual salary: "))
    
    # Calculate additional information
    monthly_salary = salary / 12
    years_to_retirement = 65 - age
    
    # Display profile
    print()
    print("=" * 60)
    print("USER PROFILE")
    print("=" * 60)
    print(f"Name:               {first_name} {last_name}")
    print(f"Age:                {age} years old")
    print(f"Email:              {email}")
    print(f"Annual Salary:      ${salary:,.2f}")
    print(f"Monthly Salary:     ${monthly_salary:,.2f}")
    print(f"Years to retirement: {years_to_retirement}")
    print("=" * 60)


# Run the profile creator
create_profile()

print()


#   Input Validation and Error Handling
"""
    When working with user input, it's important to validate the data and handle
    potential errors (exceptions) that may occur during conversion or processing.
"""

print("=" * 80)
print("Input Validation and Error Handling:")
print("=" * 80)
print()

def get_valid_number(prompt, data_type=int):
    """Get a valid number from the user."""
    while True:
        try:
            value = data_type(input(prompt))
            return value
        except ValueError:
            print(f"Error: Please enter a valid {data_type.__name__}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


print("Example: Getting a valid integer")
number = get_valid_number("Enter a number: ", int)
print(f"You entered: {number}")

print()

print("Example: Getting a valid decimal number")
decimal = get_valid_number("Enter a decimal number: ", float)
print(f"You entered: {decimal}")

print()


#   Advanced Output Formatting
print("=" * 80)
print("Advanced Output Formatting:")
print("=" * 80)
print()

# Example 1: Creating a table
print("Example 1: Formatted Table")
print()

print(f"{'ID':<5} {'Name':<15} {'Score':<8} {'Grade':<6}")
print("-" * 40)
print(f"{'1':<5} {'Alice':<15} {'95':<8} {'A':<6}")
print(f"{'2':<5} {'Bob':<15} {'87':<8} {'B':<6}")
print(f"{'3':<5} {'Charlie':<15} {'92':<8} {'A':<6}")
print(f"{'4':<5} {'Diana':<15} {'78':<8} {'C':<6}")

print()

# Example 2: Multi-line output
print("Example 2: Multi-line output with special formatting")
print()

banner = """
╔════════════════════════════════════╗
║                                    ║
║   Welcome to Python Programming    ║
║                                    ║
║   Learn, Code, and Master Python   ║
║                                    ║
╚════════════════════════════════════╝
"""
print(banner)


#   Best Practices for Input/Output
print("=" * 80)
print("Best Practices for Input/Output Operations:")
print("=" * 80)
print("""
    1. VALIDATE: Always validate user input
    2. CONVERT: Convert input to the appropriate data type
    3. FEEDBACK: Provide clear prompts and feedback to users
    4. FORMAT: Use f-strings for clean and readable output
    5. HANDLE: Use try-except blocks to handle input errors
    6. DOCUMENT: Provide clear instructions to users
    7. CONFIRM: Show users what you received from their input
    8. HELPFUL: Provide helpful error messages
""")

print()

print("=" * 80)
print("SUMMARY OF INPUT AND OUTPUT")
print("=" * 80)
print("""
✓ Use input() to get user data (returns strings)
✓ Convert input using int(), float(), etc.
✓ Use print() to display output
✓ F-strings provide clean string formatting
✓ Validate and handle user input errors
✓ Provide clear prompts and feedback
✓ Use proper formatting for readable output
✓ Combine input and output for interactive programs
✓ Test with different types of input
✓ Always consider edge cases and error scenarios
""")
