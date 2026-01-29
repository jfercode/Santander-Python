#   Operators

#   What are operators?
"""
    Operators are special symbols that allow us to perform operations on variables and values.
    Python provides different types of operators to perform arithmetic operations,
    comparisons, and logical operations.
"""


#   Arithmetic Operators
"""
    Arithmetic operators are used to perform basic mathematical operations.
    The main arithmetic operators in Python are:
    
    Addition (+): Adds two values.
    Subtraction (-): Subtracts the second value from the first.
    Multiplication (*): Multiplies two values.
    Division (/): Divides the first value by the second and returns a float result.
    Integer Division (//): Divides the first value by the second and returns an integer result (decimal part is discarded).
    Modulo (%): Returns the remainder of the division between two values.
    Exponentiation (**): Raises the first value to the power of the second.
"""

a = 10
b = 3

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
integer_division = a // b
modulo = a % b
exponentiation = a ** b

print("Arithmetic Operators:")
print(f"a = {a}, b = {b}")
print(f"Addition (+): {a} + {b} = {addition}")
print(f"Subtraction (-): {a} - {b} = {subtraction}")
print(f"Multiplication (*): {a} * {b} = {multiplication}")
print(f"Division (/): {a} / {b} = {division}")
print(f"Integer Division (//): {a} // {b} = {integer_division}")
print(f"Modulo (%): {a} % {b} = {modulo}")
print(f"Exponentiation (**): {a} ** {b} = {exponentiation}")
print()


#   Comparison Operators
"""
    Comparison operators are used to compare two values and return a boolean value
    (True or False) based on the result of the comparison.
    The comparison operators in Python are:
    
    Equal to (==): Returns True if both values are equal.
    Not equal to (!=): Returns True if the values are different.
    Greater than (>): Returns True if the first value is greater than the second.
    Less than (<): Returns True if the first value is less than the second.
    Greater than or equal to (>=): Returns True if the first value is greater than or equal to the second.
    Less than or equal to (<=): Returns True if the first value is less than or equal to the second.
"""

a = 10
b = 3

equal_to = a == b
not_equal_to = a != b
greater_than = a > b
less_than = a < b
greater_or_equal = a >= b
less_or_equal = a <= b

print("Comparison Operators:")
print(f"a = {a}, b = {b}")
print(f"Equal to (==): {a} == {b} = {equal_to}")
print(f"Not equal to (!=): {a} != {b} = {not_equal_to}")
print(f"Greater than (>): {a} > {b} = {greater_than}")
print(f"Less than (<): {a} < {b} = {less_than}")
print(f"Greater or equal (>=): {a} >= {b} = {greater_or_equal}")
print(f"Less or equal (<=): {a} <= {b} = {less_or_equal}")
print()


#   Logical Operators
"""
    Logical operators are used to combine conditional expressions and evaluate
    multiple conditions. The logical operators in Python are:
    
    AND (and): Returns True if both conditions are true.
    OR (or): Returns True if at least one of the conditions is true.
    NOT (not): Inverts the value of a condition. Returns True if the condition is false
               and False if the condition is true.
"""

a = 10
b = 3

result_and = (a > 5) and (b < 5)
result_or = (a > 15) or (b < 5)
result_not = not (a > 5)

print("Logical Operators:")
print(f"a = {a}, b = {b}")
print(f"AND (and): (a > 5) and (b < 5) = {result_and}")
print(f"OR (or): (a > 15) or (b < 5) = {result_or}")
print(f"NOT (not): not (a > 5) = {result_not}")
print()


#   Operator Precedence
"""
    Important: Python follows operator precedence rules, where certain operators
    have priority over others. In general, precedence follows this order:
    
    1. Parentheses ()
    2. Exponentiation (**)
    3. Multiplication (*), Division (/), Integer Division (//), Modulo (%)
    4. Addition (+), Subtraction (-)
    5. Comparison operators (==, !=, >, <, >=, <=)
    6. Logical operators (and, or, not)
"""

a = 2
b = 3
c = 4

result_with_parentheses = (a + b) * c
result_without_parentheses = a + b * c

print("Operator Precedence:")
print(f"a = {a}, b = {b}, c = {c}")
print(f"With parentheses: (a + b) * c = ({a} + {b}) * {c} = {result_with_parentheses}")
print(f"Without parentheses: a + b * c = {a} + ({b} * {c}) = {result_without_parentheses}")
print()

print("Tip: Use these operators to perform calculations, make decisions based on comparisons,")
print("and combine logical conditions in your programs!")
