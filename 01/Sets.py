#   Sets

#   What are sets?
"""
    A set is a mutable and unordered data structure that allows storing a collection
    of unique elements. Sets are enclosed in curly braces {} or created using the set() function.
    
    Key characteristics:
    - Mutable: Can be modified after creation
    - Unordered: Items do not have a specific order
    - Unique elements: Duplicates are automatically removed
    - Cannot contain mutable elements (lists, dictionaries, sets)
    - Optimized for membership testing and removing duplicates
"""


#   Creating Sets
"""
    To create a set, use curly braces or the set() function.
    Note: Empty set must be created with set(), not {} (which creates an empty dictionary).
"""

print("Creating Sets:")

# Using curly braces
fruits = {"apple", "banana", "orange"}
print(f"Fruits set: {fruits}")

# Using set() function
numbers = set([1, 2, 3, 4, 5])
print(f"Numbers set: {numbers}")

# Empty set (correct way)
empty_set = set()
print(f"Empty set: {empty_set}")
print()

# Duplicates are automatically removed
mixed = {1, 2, 2, 3, 3, 3, 4}
print(f"Set with duplicates removed: {mixed}")
print()


#   Set Operations
"""
    Sets support mathematical set operations:
    
    Union (|): Combines all elements from both sets
    Intersection (&): Elements common to both sets
    Difference (-): Elements in the first set but not in the second
    Symmetric Difference (^): Elements in either set but not in both
"""

print("Set Operations:")
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print()

# Union - all unique elements from both sets
union = set1 | set2
print(f"Union (set1 | set2): {union}")

# Alternative: set1.union(set2)
union_alt = set1.union(set2)
print(f"Union using .union(): {union_alt}")
print()

# Intersection - elements common to both sets
intersection = set1 & set2
print(f"Intersection (set1 & set2): {intersection}")

# Alternative: set1.intersection(set2)
intersection_alt = set1.intersection(set2)
print(f"Intersection using .intersection(): {intersection_alt}")
print()

# Difference - elements in set1 but not in set2
difference = set1 - set2
print(f"Difference (set1 - set2): {difference}")

# Alternative: set1.difference(set2)
difference_alt = set1.difference(set2)
print(f"Difference using .difference(): {difference_alt}")
print()

# Symmetric Difference - elements in either set but not in both
sym_difference = set1 ^ set2
print(f"Symmetric Difference (set1 ^ set2): {sym_difference}")

# Alternative: set1.symmetric_difference(set2)
sym_difference_alt = set1.symmetric_difference(set2)
print(f"Symmetric Difference using .symmetric_difference(): {sym_difference_alt}")
print()


#   Set Methods
"""
    Sets in Python have several built-in methods for manipulating elements:
    
    add(element): Adds a single element to the set
    update(iterable): Adds multiple elements from an iterable
    remove(element): Removes an element. Raises error if not found
    discard(element): Removes an element if present. No error if not found
    pop(): Removes and returns an arbitrary element
    clear(): Removes all elements from the set
    copy(): Creates a shallow copy of the set
"""

print("Set Methods:")
fruits = {"apple", "banana", "orange"}
print(f"Original set: {fruits}")
print()

# add() method
print("add() - Add a single element:")
fruits.add("pear")
print(f"After add('pear'): {fruits}")
print()

# update() method
print("update() - Add multiple elements:")
fruits.update(["grape", "mango"])
print(f"After update(['grape', 'mango']): {fruits}")
print()

# remove() method
print("remove() - Remove an element:")
fruits.remove("banana")
print(f"After remove('banana'): {fruits}")
print()

# discard() method - safe removal
print("discard() - Remove safely (no error if missing):")
fruits.discard("kiwi")  # Does not exist, but no error
print(f"After discard('kiwi'): {fruits}")
print()

# pop() method
print("pop() - Remove and return an arbitrary element:")
removed = fruits.pop()
print(f"Removed element: {removed}")
print(f"After pop(): {fruits}")
print()

# copy() method
print("copy() - Create a copy:")
fruits_copy = fruits.copy()
fruits_copy.add("watermelon")
print(f"Original fruits: {fruits}")
print(f"Copied fruits (modified): {fruits_copy}")
print()

# clear() method
print("clear() - Remove all elements:")
temp_set = {1, 2, 3}
print(f"Before clear: {temp_set}")
temp_set.clear()
print(f"After clear: {temp_set}")
print()


#   Membership Testing
"""
    Sets are optimized for checking if an element exists in the collection.
    This operation is very efficient with sets compared to lists.
"""

print("Membership Testing:")
numbers = {1, 2, 3, 4, 5}
print(f"Set: {numbers}")
print(f"3 in numbers: {3 in numbers}")
print(f"10 in numbers: {10 in numbers}")
print()


#   Iterating Over Sets
"""
    You can iterate over set elements, but remember sets are unordered.
"""

print("Iterating Over Sets:")
colors = {"red", "green", "blue", "yellow"}
print("Using for loop (order is not guaranteed):")
for color in colors:
    print(f"  - {color}")
print()


#   Practical Set Examples
"""
    Real-world use cases for sets.
"""

print("Practical Set Examples:")
print()

# Example 1: Remove duplicates from a list
print("Example 1 - Remove Duplicates from List:")
numbers_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print(f"Original list: {numbers_list}")
print(f"Unique numbers: {unique_numbers}")
print(f"Back to list: {sorted(list(unique_numbers))}")
print()

# Example 2: Find common interests
print("Example 2 - Find Common Interests:")
alice_interests = {"python", "music", "reading", "gaming"}
bob_interests = {"gaming", "sports", "music", "coding"}
common = alice_interests & bob_interests
print(f"Alice's interests: {alice_interests}")
print(f"Bob's interests: {bob_interests}")
print(f"Common interests: {common}")
print()

# Example 3: Find unique visitors
print("Example 3 - Unique Visitors to Websites:")
site_a_visitors = {"user1", "user2", "user3", "user4"}
site_b_visitors = {"user3", "user4", "user5", "user6"}
all_visitors = site_a_visitors | site_b_visitors
only_site_a = site_a_visitors - site_b_visitors
only_site_b = site_b_visitors - site_a_visitors
print(f"Site A visitors: {site_a_visitors}")
print(f"Site B visitors: {site_b_visitors}")
print(f"All visitors (union): {all_visitors}")
print(f"Only Site A visitors: {only_site_a}")
print(f"Only Site B visitors: {only_site_b}")
print()

# Example 4: Check for common elements
print("Example 4 - Check for Common Elements:")
string1 = set("hello")
string2 = set("world")
print(f"Letters in 'hello': {string1}")
print(f"Letters in 'world': {string2}")
print(f"Common letters: {string1 & string2}")
print()


#   Set Comparison
"""
    Summary of data structures covered:
    
    Lists: Ordered, mutable, allows duplicates, indexed access
    Tuples: Ordered, immutable, allows duplicates, indexed access
    Dictionaries: Unordered, mutable, unique keys with values, key-based access
    Sets: Unordered, mutable, unique elements, optimized for membership testing
"""

print("Tip: Use sets for finding unique elements, removing duplicates,")
print("and performing mathematical set operations efficiently!")
