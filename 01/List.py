
#   LISTS
"""
    A list is a mutable and ordered data structure that allows storing a collection of elements.
    The elements in a list can be of different data types and are enclosed in square brackets [],
    separated by commas.
    
    Key characteristics:
    - Mutable: Can be modified after creation
    - Ordered: Elements have a specific position (index)
    - Allows duplicates
    - Can contain different data types
"""


#   Creating and Accessing Lists
"""
    To create a list, simply enclose the elements in square brackets.
    To access elements, use the index inside square brackets.
    Indices start from 0 for the first element.
    Negative indices count from the end: -1 is the last element, -2 is second-to-last, etc.
"""

print("Creating and Accessing Lists:")
fruits = ["apple", "banana", "orange"]

print(f"List: {fruits}")
print(f"First element (index 0): {fruits[0]}")
print(f"Second element (index 1): {fruits[1]}")
print(f"Third element (index 2): {fruits[2]}")
print()

print("Accessing with negative indices:")
print(f"Last element (index -1): {fruits[-1]}")
print(f"Second-to-last (index -2): {fruits[-2]}")
print(f"Third-to-last (index -3): {fruits[-3]}")
print()

# List with mixed data types
mixed_list = [1, "hello", 3.14, True]
print(f"Mixed data types list: {mixed_list}")
print()


#   List Methods
"""
    Lists in Python have several built-in methods that allow us to manipulate
    and modify the elements. Common methods include:
    
    append(element): Adds an element to the end of the list
    insert(index, element): Inserts an element at a specific position
    remove(element): Removes the first occurrence of an element
    pop(index): Removes and returns the element at a specific position
    sort(): Sorts the list in ascending order
    reverse(): Reverses the order of elements
    len(): Returns the number of elements (not a method, but a function)
"""

print("List Methods:")
fruits = ["apple", "banana", "orange"]
print(f"Original list: {fruits}")
print()

# append
fruits.append("pear")
print(f"After append('pear'): {fruits}")

# insert
fruits.insert(1, "grape")
print(f"After insert(1, 'grape'): {fruits}")

# remove
fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

# pop
removed_fruit = fruits.pop(2)
print(f"After pop(2): {fruits}")
print(f"Removed element: {removed_fruit}")

# sort
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(f"After sort(): {numbers}")

# reverse
numbers.reverse()
print(f"After reverse(): {numbers}")

# len
print(f"Length of list: {len(numbers)}")
print()


#   List Slicing
"""
    List slicing allows you to extract a portion of a list using the syntax:
    list[start:end:step]
    
    - start: Starting index (inclusive)
    - end: Ending index (exclusive)
    - step: Interval between elements (optional)
"""

print("List Slicing:")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {numbers}")
print(f"numbers[2:5] (from index 2 to 4): {numbers[2:5]}")
print(f"numbers[:4] (first 4 elements): {numbers[:4]}")
print(f"numbers[6:] (from index 6 to end): {numbers[6:]}")
print(f"numbers[::2] (every 2nd element): {numbers[::2]}")
print(f"numbers[::-1] (reversed): {numbers[::-1]}")
print()


#   List Comprehensions
"""
    List comprehensions are a concise way to create new lists based on an existing sequence.
    They allow filtering and transforming list elements in a single line of code.
    
    Syntax: new_list = [expression for element in sequence if condition]
"""

print("List Comprehensions:")

# Example 1: Squares of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(f"Original numbers: {numbers}")
print(f"Squares of even numbers: {even_squares}")
print()

# Example 2: Convert strings to uppercase
words = ["apple", "banana", "orange"]
uppercase_words = [word.upper() for word in words]
print(f"Original words: {words}")
print(f"Uppercase words: {uppercase_words}")
print()

# Example 3: Filter numbers greater than 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = [x for x in numbers if x > 5]
print(f"Numbers greater than 5: {filtered_numbers}")
print()

# Example 4: Complex transformation
pairs = [(x, x ** 2) for x in range(1, 6)]
print(f"Pairs of (number, square): {pairs}")
print()


#   Iterating Over Lists
"""
    Common ways to iterate over list elements.
"""

print("Iterating Over Lists:")

# Using for loop
print("Using for loop:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"  - {fruit}")

print()

# Using enumerate for index and value
print("Using enumerate (with index):")
for index, fruit in enumerate(fruits):
    print(f"  Index {index}: {fruit}")

print()

# Using range with len
print("Using range with len:")
for i in range(len(fruits)):
    print(f"  Position {i}: {fruits[i]}")

print()


#   Common List Operations
"""
    Additional useful list operations.
"""

print("Common List Operations:")

# Check if element exists
fruits = ["apple", "banana", "orange"]
print(f"'apple' in list: {'apple' in fruits}")
print(f"'grape' in list: {'grape' in fruits}")
print()

# Count occurrences
numbers = [1, 2, 2, 3, 3, 3, 4]
print(f"Numbers: {numbers}")
print(f"Count of 3: {numbers.count(3)}")
print()

# Find index
print(f"Index of 'banana': {fruits.index('banana')}")
print()

# Copy a list (important: use .copy() to avoid reference issues)
fruits_copy = fruits.copy()
fruits_copy.append("grape")
print(f"Original list: {fruits}")
print(f"Copied list (modified): {fruits_copy}")
print()

print("Tip: Lists are very versatile! Use them to store ordered collections of data.")
print("Remember: Lists are mutable, so you can modify them after creation.")
print()
print()
