#   Control Structures

#   What are control structures?
"""
    Control structures allow us to control the flow of execution of our programs.
    In Python, the most common control structures are conditional statements and loops.
    These structures allow us to make decisions and repeat blocks of code based on
    certain conditions.
"""


#   Conditional Statements
"""
    Conditional statements allow us to execute different blocks of code depending on
    whether a certain condition is met or not. In Python, the most commonly used
    conditional structures are: if, if-else, and if-elif-else.
"""


#   IF Statement
"""
    The if statement is used to execute a block of code if a condition is true.
    Basic syntax:
    
    if condition:
        # Code block to execute if the condition is true
        instructions
"""

print("IF Statement Example:")
age = 18

if age >= 18:
    print(f"Age: {age} - You are an adult")

print()


#   IF-ELSE Statement
"""
    The if-else statement allows us to specify an alternative block of code
    that will be executed if the if condition is false.
    Basic syntax:
    
    if condition:
        # Code block if condition is true
        instructions
    else:
        # Code block if condition is false
        instructions
"""

print("IF-ELSE Statement Example:")
age = 15

if age >= 18:
    print(f"Age: {age} - You are an adult")
else:
    print(f"Age: {age} - You are a minor")

print()


#   IF-ELIF-ELSE Statement
"""
    The if-elif-else statement allows us to specify multiple conditions and
    alternative code blocks. Basic syntax:
    
    if condition1:
        # Code block if condition1 is true
        instructions
    elif condition2:
        # Code block if condition2 is true
        instructions
    elif condition3:
        # Code block if condition3 is true
        instructions
    else:
        # Code block if none of the above conditions are true
        instructions
"""

print("IF-ELIF-ELSE Statement Example:")
grade = 85

if grade >= 90:
    rating = "Excellent"
elif grade >= 80:
    rating = "Very Good"
elif grade >= 70:
    rating = "Good"
elif grade >= 60:
    rating = "Satisfactory"
else:
    rating = "Needs Improvement"

print(f"Grade: {grade} - Rating: {rating}")
print()


#   Multiple Examples
"""
    More examples to practice conditional statements.
"""

print("Additional Examples:")
print()

# Example 1: Check if a number is positive, negative, or zero
number = -5

if number > 0:
    result = "positive"
elif number < 0:
    result = "negative"
else:
    result = "zero"

print(f"Number: {number} - The number is {result}")
print()

# Example 2: Check if a person qualifies for a discount
age = 65
has_membership = True

if age >= 65 or has_membership:
    discount = "20%"
    print(f"Age: {age}, Membership: {has_membership} - You qualify for a {discount} discount")
else:
    print(f"Age: {age}, Membership: {has_membership} - You do not qualify for a discount")
print()

# Example 3: Check temperature and suggest clothing
temperature = 25

if temperature > 30:
    clothing = "light clothes (shorts, t-shirt)"
elif temperature > 20:
    clothing = "comfortable clothes (jeans, shirt)"
elif temperature > 10:
    clothing = "warm clothes (jacket, sweater)"
else:
    clothing = "heavy winter clothes (coat, gloves)"

print(f"Temperature: {temperature}°C - Suggested: {clothing}")
print()

print("Tip: Use conditional statements to make decisions in your programs")
print("and execute different code blocks based on specific conditions!")
