#   Dictionaries

#   What are dictionaries?
"""
    A dictionary is a mutable and unordered data structure that allows storing pairs of
    key-value combinations. Each element in a dictionary consists of a unique key and its
    corresponding value. Dictionaries are enclosed in curly braces {}, and key-value pairs
    are separated by commas.
    
    Key characteristics:
    - Mutable: Can be modified after creation
    - Unordered: Items do not have a guaranteed order (though Python 3.7+ maintains insertion order)
    - Keys must be unique and immutable (strings, numbers, tuples)
    - Values can be of any data type
    - Fast access using keys
"""


#   Creating and Accessing Dictionaries
"""
    To create a dictionary, use curly braces and separate keys and values with a colon.
    To access values, use the corresponding key in square brackets.
    You can also use the get() method to safely retrieve values.
"""

print("Creating and Accessing Dictionaries:")
person = {"name": "Juan", "age": 25, "city": "Madrid"}

print(f"Dictionary: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")
print()

# Using get() method
print("Using get() method:")
print(f"Name: {person.get('name')}")
print(f"Job: {person.get('job')}")  # Returns None if key doesn't exist
print(f"Job with default: {person.get('job', 'Not specified')}")
print()

# Different data types
student = {
    "name": "Alice",
    "age": 20,
    "gpa": 3.85,
    "is_enrolled": True,
    "courses": ["Python", "Math", "Physics"]
}

print("Dictionary with mixed data types:")
print(f"Student: {student}")
print(f"Courses: {student['courses']}")
print()


#   Modifying Dictionaries
"""
    Dictionaries are mutable, so you can add, modify, or remove elements.
"""

print("Modifying Dictionaries:")
person = {"name": "Juan", "age": 25, "city": "Madrid"}
print(f"Original: {person}")
print()

# Add a new key-value pair
person["profession"] = "Engineer"
print(f"After adding profession: {person}")

# Modify an existing value
person["age"] = 26
print(f"After updating age: {person}")

# Delete a key-value pair
del person["city"]
print(f"After deleting city: {person}")
print()


#   Dictionary Methods
"""
    Dictionaries in Python have several built-in methods for manipulating and accessing elements.
    
    keys(): Returns a view of all the keys in the dictionary
    values(): Returns a view of all the values in the dictionary
    items(): Returns a view of all key-value pairs as tuples
    update(other_dict): Updates the dictionary with key-value pairs from another dictionary
    pop(key): Removes and returns the value of a specified key
    clear(): Removes all items from the dictionary
    copy(): Creates a shallow copy of the dictionary
"""

print("Dictionary Methods:")
person = {"name": "Juan", "age": 25, "city": "Madrid"}
print(f"Original dictionary: {person}")
print()

# keys() method
print("keys() - All keys:")
print(f"Keys: {person.keys()}")
print()

# values() method
print("values() - All values:")
print(f"Values: {person.values()}")
print()

# items() method
print("items() - All key-value pairs:")
print(f"Items: {person.items()}")
print()

# update() method
print("update() - Adding new key-value pairs:")
person.update({"profession": "Engineer", "salary": 50000})
print(f"After update: {person}")
print()

# pop() method
print("pop() - Remove and return a value:")
city = person.pop("city")
print(f"Removed city: {city}")
print(f"After pop: {person}")
print()

# copy() method
print("copy() - Create a copy:")
person_copy = person.copy()
person_copy["name"] = "Carlos"
print(f"Original person: {person}")
print(f"Copied person (modified): {person_copy}")
print()


#   Iterating Over Dictionaries
"""
    Common ways to iterate over dictionary elements.
"""

print("Iterating Over Dictionaries:")

student = {"name": "Alice", "age": 20, "gpa": 3.85}
print()

# Iterate over keys
print("Iterating over keys:")
for key in student:
    print(f"  Key: {key}")

print()

# Iterate over values
print("Iterating over values:")
for value in student.values():
    print(f"  Value: {value}")

print()

# Iterate over items
print("Iterating over items (key-value pairs):")
for key, value in student.items():
    print(f"  {key}: {value}")

print()


#   Practical Dictionary Examples
"""
    Real-world use cases for dictionaries.
"""

print("Practical Dictionary Examples:")
print()

# Example 1: Student grades
print("Example 1 - Student Grades:")
grades = {
    "Alice": 95,
    "Bob": 87,
    "Carlos": 92,
    "Diana": 88
}

print(f"Grades: {grades}")
for student, grade in grades.items():
    print(f"  {student}: {grade}")

average = sum(grades.values()) / len(grades)
print(f"Average grade: {average:.2f}")
print()

# Example 2: Configuration settings
print("Example 2 - Configuration Settings:")
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "timeout": 30
}

print(f"Configuration: {config}")
print(f"Connect to {config['host']}:{config['port']}")
if config["debug"]:
    print("Debug mode is enabled")
print()

# Example 3: Nested dictionaries
print("Example 3 - Nested Dictionaries:")
company = {
    "name": "TechCorp",
    "employees": {
        "manager": {"name": "Juan", "salary": 60000},
        "developer": {"name": "Alice", "salary": 50000},
        "designer": {"name": "Bob", "salary": 45000}
    }
}

print(f"Company: {company['name']}")
print("Employees:")
for position, info in company["employees"].items():
    print(f"  {position.capitalize()}: {info['name']} (${info['salary']})")
print()

# Example 4: Check if key exists
print("Example 4 - Check if Key Exists:")
person = {"name": "Juan", "age": 25}
print(f"'name' in person: {'name' in person}")
print(f"'email' in person: {'email' in person}")
print()

# Example 5: Get with default value
print("Example 5 - Safe Value Access:")
email = person.get("email", "not provided")
print(f"Email: {email}")
print()

print("Tip: Use dictionaries to store related data as key-value pairs.")
print("They are perfect for configuration data, mappings, and structured information!")
