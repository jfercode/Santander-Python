#   Loops

#   What are loops?
"""
    Loops allow us to repeat a block of code multiple times.
    In Python, the most common loops are: for and while.
    Loops are essential for automating repetitive tasks and processing collections of data.
"""


#   FOR Loop
"""
    The for loop is used to iterate over a sequence (like a list, tuple, or string)
    or any iterable object. Basic syntax:
    
    for variable in sequence:
        # Code block to repeat
        instructions
    
    In each iteration, the variable takes the value of an element from the sequence,
    and the code block is executed.
"""

print("FOR Loop Example - Iterating over a list:")
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(f"Fruit: {fruit}")

print()

# FOR loop with range
print("FOR Loop with range() - Numbers from 0 to 4:")
for i in range(5):
    print(f"Number: {i}")

print()


#   WHILE Loop
"""
    The while loop is used to repeat a block of code while a condition is true.
    Basic syntax:
    
    while condition:
        # Code block to repeat
        instructions
    
    The loop continues as long as the condition remains true.
    Be careful to avoid infinite loops - the condition must eventually become false.
"""

print("WHILE Loop Example - Counting from 0 to 4:")
counter = 0

while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

print()


#   Loop Control Statements
"""
    Python provides special statements to control the flow of execution within loops:
    - break: Exit the loop prematurely
    - continue: Skip the rest of the current iteration
    - pass: Null operation (do nothing)
"""


#   BREAK Statement
"""
    The break statement is used to exit a loop prematurely, regardless of the condition.
    When break is encountered, the loop stops and execution continues with the next
    instruction after the loop.
"""

print("BREAK Statement Example - Stop when counter reaches 5:")
counter = 0

while True:
    print(f"Counter: {counter}")
    counter += 1
    
    if counter == 5:
        print("Breaking out of the loop!")
        break

print()


#   CONTINUE Statement
"""
    The continue statement is used to skip the rest of the code block in a loop
    and move to the next iteration.
"""

print("CONTINUE Statement Example - Print only odd numbers from 0 to 9:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")

print()


#   PASS Statement
"""
    The pass statement is a null operation that does nothing.
    It is used as a placeholder when a statement is required syntactically,
    but you don't want to execute any code.
    Useful for creating structure while developing your program.
"""

print("PASS Statement Example - Placeholder loop:")
for i in range(3):
    pass
print("Loop completed (no action performed)")

print()


#   Additional Practical Examples
"""
    More examples to practice loops and loop control statements.
"""

print("Additional Examples:")
print()

# Example 1: Sum numbers from 1 to 10 using a for loop
print("Example 1 - Sum numbers from 1 to 10:")
total = 0

for num in range(1, 11):
    total += num

print(f"Sum: {total}")
print()

# Example 2: Find the first number divisible by 7 in a range
print("Example 2 - Find first number divisible by 7 (0-50):")
for num in range(51):
    if num % 7 == 0 and num != 0:
        print(f"Found: {num}")
        break

print()

# Example 3: Print multiplication table with continue
print("Example 3 - Multiplication table for 5 (skip 5 itself):")
for i in range(1, 6):
    if i == 5:
        continue
    result = 5 * i
    print(f"5 × {i} = {result}")

print()

# Example 4: Iterate over a string
print("Example 4 - Iterate over a string:")
word = "Python"

for letter in word:
    print(f"Letter: {letter}")

print()

# Example 5: Nested loops - multiplication table
print("Example 5 - Multiplication table (2×2 to 4×4):")
for i in range(2, 5):
    for j in range(2, 5):
        result = i * j
        print(f"{i} × {j} = {result}", end="  ")
    print()

print()

print("Tip: Use loops to automate repetitive tasks and process data efficiently!")
print("Remember to avoid infinite loops by ensuring your condition will eventually become false.")
