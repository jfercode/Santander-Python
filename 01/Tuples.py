
#   TUPLES
"""
    A tuple is an immutable and ordered data structure that allows storing a collection of elements.
    The elements in a tuple are enclosed in parentheses (), separated by commas.
    
    Key characteristics:
    - Immutable: Cannot be modified after creation
    - Ordered: Elements have a specific position (index)
    - Allows duplicates
    - Can contain different data types
    - More memory efficient than lists
"""


#   Creating and Accessing Tuples
"""
    To create a tuple, enclose the elements in parentheses.
    To access elements, use the index inside square brackets, similar to lists.
    Indices start from 0.
    
    Note: Tuples are useful when you need to store data that should not be modified,
    such as coordinates, configuration data, or function return values.
"""

print("Creating and Accessing Tuples:")
point = (3, 4)
person = ("Juan", 25, "Spain")
empty_tuple = ()
single_element = (42,)  # Note: comma is required for single-element tuple

print(f"Point tuple: {point}")
print(f"First element (x): {point[0]}")
print(f"Second element (y): {point[1]}")
print()

print(f"Person tuple: {person}")
print(f"Name: {person[0]}")
print(f"Age: {person[1]}")
print(f"Country: {person[2]}")
print()

print(f"Empty tuple: {empty_tuple}")
print(f"Single element tuple: {single_element}")
print()

# Accessing with negative indices
print("Accessing with negative indices:")
print(f"Last element (index -1): {person[-1]}")
print(f"Second-to-last (index -2): {person[-2]}")
print()


#   Tuple Immutability
"""
    Unlike lists, tuples are immutable. Once created, you cannot:
    - Add elements
    - Remove elements
    - Modify existing elements
    
    Attempting to do so will result in an error.
    This immutability makes tuples more efficient and safer for constant data.
"""

print("Tuple Immutability:")
coordinates = (10, 20)
print(f"Original tuple: {coordinates}")
print("Tuples cannot be modified - attempting to change an element would cause an error")
print("# coordinates[0] = 15  # This would cause: TypeError")
print()


#   Tuple Methods
"""
    Although tuples are immutable, Python provides several useful methods:
    
    count(element): Returns the number of times an element appears in the tuple
    index(element): Returns the index of the first occurrence of an element
                    Optionally, you can specify start and end positions for the search
    len(tuple): Built-in function that returns the number of elements in the tuple
"""

print("Tuple Methods:")
my_tuple = (1, 2, 3, 2, 4, 2, 5)
print(f"Tuple: {my_tuple}")
print()

# count method
count_of_2 = my_tuple.count(2)
print(f"Count of 2: {count_of_2}")
print()

# index method
index_of_2 = my_tuple.index(2)
print(f"Index of first 2: {index_of_2}")

index_of_2_from_2 = my_tuple.index(2, 2)
print(f"Index of 2 starting from position 2: {index_of_2_from_2}")

index_of_2_range = my_tuple.index(2, 2, 5)
print(f"Index of 2 between positions 2-5: {index_of_2_range}")
print()

# len function
print(f"Length of tuple: {len(my_tuple)}")
print()


#   Tuple Unpacking
"""
    Tuple unpacking allows you to assign tuple elements to multiple variables in one statement.
    This is a convenient way to extract values from a tuple.
"""

print("Tuple Unpacking:")
person = ("Alice", 28, "London")
name, age, city = person
print(f"Tuple: {person}")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print()

# Unpacking with multiple assignment
coordinates = (5, 10)
x, y = coordinates
print(f"Coordinates: {coordinates}")
print(f"x = {x}, y = {y}")
print()


#   Tuple vs List
"""
    Comparison of tuples and lists:
    
    Tuples:
    - Immutable (cannot be modified)
    - Slightly faster and more memory efficient
    - Can be used as dictionary keys
    - Good for protecting data from modification
    
    Lists:
    - Mutable (can be modified)
    - More flexible with many methods
    - Cannot be used as dictionary keys
    - Better for dynamic collections
"""

print("Tuples vs Lists Comparison:")
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print(f"List: {my_list} - Type: {type(my_list).__name__}")
print(f"Tuple: {my_tuple} - Type: {type(my_tuple).__name__}")
print()

print("List is mutable - we can modify it:")
my_list[0] = 10
print(f"Modified list: {my_list}")
print()

print("Tuple is immutable - we cannot modify it directly")
print("(Attempting to modify would cause: TypeError)")
print()


#   Iterating Over Tuples
"""
    Similar to lists, you can iterate over tuples using for loops.
"""

print("Iterating Over Tuples:")
colors = ("red", "green", "blue")
for color in colors:
    print(f"  - {color}")
print()

print("Using enumerate:")
for index, color in enumerate(colors):
    print(f"  Index {index}: {color}")
print()

print("Tip: Use tuples for fixed collections of data that should not change.")
print("They are perfect for function return values and as dictionary keys!")