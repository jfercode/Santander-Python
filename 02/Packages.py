#   Packages in Python

#   What are Packages?
"""
    A package is a way to organize related modules into a hierarchical directory
    structure. Packages allow us to group related modules and avoid naming
    conflicts between modules.
    
    Key differences between modules and packages:
    - Module: A single .py file
    - Package: A directory containing modules and __init__.py file
    
    Benefits of packages:
    - Better code organization
    - Avoid naming conflicts (can have same module names in different packages)
    - Hierarchical structure (organized like a file system)
    - Better maintainability for large projects
    - Professional project structure
"""

import os
import sys

print("=" * 80)
print("Packages in Python:")
print("=" * 80)
print()


#   Package Structure
"""
    The key element that makes a directory a package is the __init__.py file.
    This file marks the directory as a Python package.
    
    Basic package structure:
    
    my_package/
    ├── __init__.py
    ├── module1.py
    ├── module2.py
    └── subpackage/
        ├── __init__.py
        ├── module3.py
        └── module4.py
    
    The __init__.py file can be:
    - Empty (just marks directory as package)
    - Contains initialization code for the package
    - Exports specific items from submodules
"""

print("=" * 80)
print("Creating Packages:")
print("=" * 80)
print()

# Example 1: Create a simple package structure
print("Example 1: Creating a simple package")
print()

# Create package directory
package_dir = "math_tools"
if not os.path.exists(package_dir):
    os.makedirs(package_dir)

# Create __init__.py (marks directory as package)
init_file = os.path.join(package_dir, "__init__.py")
with open(init_file, "w") as f:
    f.write('''"""
math_tools package - Mathematical utilities package.

This package provides various mathematical tools and operations.
"""

# Package version
__version__ = "1.0.0"
__author__ = "Python Developer"

# Export main items for easy access
from .basic_operations import add, subtract, multiply, divide
from .advanced_operations import power, factorial, fibonacci

__all__ = ['add', 'subtract', 'multiply', 'divide', 'power', 'factorial', 'fibonacci']
''')

# Create basic_operations module
basic_ops = os.path.join(package_dir, "basic_operations.py")
with open(basic_ops, "w") as f:
    f.write('''"""
basic_operations.py - Basic mathematical operations module.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
''')

# Create advanced_operations module
advanced_ops = os.path.join(package_dir, "advanced_operations.py")
with open(advanced_ops, "w") as f:
    f.write('''"""
advanced_operations.py - Advanced mathematical operations module.
"""

def power(base, exponent):
    """Raise base to the power of exponent."""
    return base ** exponent

def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    """Generate first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence
''')

print(f"Created package '{package_dir}' with structure:")
print(f"  {package_dir}/")
print(f"    __init__.py (marks directory as package)")
print(f"    basic_operations.py (add, subtract, multiply, divide)")
print(f"    advanced_operations.py (power, factorial, fibonacci)")
print()


#   Importing from Packages
print("=" * 80)
print("Importing from Packages:")
print("=" * 80)
print()

# Import methods
print("Method 1: Import entire module from package")
print()

from math_tools import basic_operations
result = basic_operations.add(10, 5)
print(f"  from math_tools import basic_operations")
print(f"  basic_operations.add(10, 5) = {result}")
print()


print("Method 2: Import specific function from module in package")
print()

from math_tools.advanced_operations import factorial
result = factorial(5)
print(f"  from math_tools.advanced_operations import factorial")
print(f"  factorial(5) = {result}")
print()


print("Method 3: Import items exported in __init__.py")
print()

from math_tools import add, multiply, fibonacci
print(f"  from math_tools import add, multiply, fibonacci")
print(f"  add(20, 30) = {add(20, 30)}")
print(f"  multiply(4, 7) = {multiply(4, 7)}")
print(f"  fibonacci(8) = {fibonacci(8)}")
print()


print("Method 4: Import entire package")
print()

import math_tools
result = math_tools.divide(100, 4)
print(f"  import math_tools")
print(f"  math_tools.divide(100, 4) = {result}")
print()


print("Method 5: Import with alias")
print()

from math_tools.advanced_operations import power as exp
result = exp(2, 10)
print(f"  from math_tools.advanced_operations import power as exp")
print(f"  exp(2, 10) = {result}")
print()


#   The __init__.py File
print("=" * 80)
print("The __init__.py File:")
print("=" * 80)
print("""
The __init__.py file serves several purposes:

1. MARKS DIRECTORY AS PACKAGE
   Without __init__.py, Python treats directory as namespace package
   (works differently, not recommended for beginners)

2. INITIALIZATION CODE
   Code in __init__.py runs when package is imported

3. EXPORTS AND SHORTCUTS
   Can import items from submodules to make them easily accessible
   from package import item (instead of from package.module import item)

4. PACKAGE CONFIGURATION
   Can define package-level variables and configuration

5. NAMESPACE DEFINITION
   Can define what items are public vs private

EXAMPLE __init__.py:

'''
\"\"\"
my_package/__init__.py - Package initialization file.
\"\"\"

# Import submodules
from . import module1
from . import module2

# Import and expose specific items
from .module1 import function1
from .module2 import function2

# Define package metadata
__version__ = "1.0.0"
__author__ = "Author Name"

# Define public API
__all__ = ['function1', 'function2', 'module1', 'module2']

# Initialization code
print("Package initialized")
'''
""")

print()


#   Subpackages
print("=" * 80)
print("Creating Subpackages:")
print("=" * 80)
print()

# Create a package with subpackages
print("Example 2: Creating package with subpackages")
print()

# Create utils package with subpackages
utils_dir = "utilities_pkg"
utils_string = os.path.join(utils_dir, "string_utils")
utils_math = os.path.join(utils_dir, "math_utils")

for directory in [utils_dir, utils_string, utils_math]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Create main __init__.py for utilities_pkg
with open(os.path.join(utils_dir, "__init__.py"), "w") as f:
    f.write('''"""
utilities_pkg - Main utilities package with subpackages.
"""

from . import string_utils
from . import math_utils

__version__ = "1.0.0"
''')

# Create string_utils subpackage
with open(os.path.join(utils_string, "__init__.py"), "w") as f:
    f.write('''"""
string_utils - String manipulation utilities subpackage.
"""

from .text_processing import reverse_string, is_palindrome, capitalize_words
from .text_analysis import count_words, count_characters

__all__ = ['reverse_string', 'is_palindrome', 'capitalize_words', 
           'count_words', 'count_characters']
''')

# Create text_processing module
with open(os.path.join(utils_string, "text_processing.py"), "w") as f:
    f.write('''"""
text_processing.py - Text processing utilities.
"""

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def is_palindrome(text):
    """Check if text is palindrome."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def capitalize_words(text):
    """Capitalize first letter of each word."""
    return " ".join(word.capitalize() for word in text.split())
''')

# Create text_analysis module
with open(os.path.join(utils_string, "text_analysis.py"), "w") as f:
    f.write('''"""
text_analysis.py - Text analysis utilities.
"""

def count_words(text):
    """Count words in text."""
    return len(text.split())

def count_characters(text):
    """Count characters in text."""
    return len(text)
''')

# Create math_utils subpackage
with open(os.path.join(utils_math, "__init__.py"), "w") as f:
    f.write('''"""
math_utils - Mathematical utilities subpackage.
"""

from .calculations import add, subtract, multiply, divide
from .statistics import mean, median, standard_deviation

__all__ = ['add', 'subtract', 'multiply', 'divide', 
           'mean', 'median', 'standard_deviation']
''')

# Create calculations module
with open(os.path.join(utils_math, "calculations.py"), "w") as f:
    f.write('''"""
calculations.py - Basic calculations.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
''')

# Create statistics module
with open(os.path.join(utils_math, "statistics.py"), "w") as f:
    f.write('''"""
statistics.py - Statistical calculations.
"""

def mean(numbers):
    """Calculate mean average."""
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calculate median."""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:
        return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    return sorted_nums[n//2]

def standard_deviation(numbers):
    """Calculate standard deviation."""
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5
''')

print("Created utilities_pkg with subpackages:")
print("  utilities_pkg/")
print("    __init__.py")
print("    string_utils/")
print("      __init__.py")
print("      text_processing.py")
print("      text_analysis.py")
print("    math_utils/")
print("      __init__.py")
print("      calculations.py")
print("      statistics.py")
print()


#   Using Subpackages
print("=" * 80)
print("Using Subpackages:")
print("=" * 80)
print()

print("Method 1: Import from subpackage module")
from utilities_pkg.string_utils.text_processing import reverse_string
result = reverse_string("Python")
print(f"  from utilities_pkg.string_utils.text_processing import reverse_string")
print(f"  reverse_string('Python') = '{result}'")
print()

print("Method 2: Import from subpackage __init__")
from utilities_pkg.string_utils import count_words, is_palindrome
result1 = count_words("Hello World Python Programming")
result2 = is_palindrome("A man a plan a canal Panama")
print(f"  from utilities_pkg.string_utils import count_words, is_palindrome")
print(f"  count_words('Hello World Python Programming') = {result1}")
print(f"  is_palindrome('A man a plan a canal Panama') = {result2}")
print()

print("Method 3: Import from math subpackage")
from utilities_pkg.math_utils import mean, median, standard_deviation
numbers = [10, 20, 30, 40, 50]
print(f"  Numbers: {numbers}")
print(f"  mean() = {mean(numbers)}")
print(f"  median() = {median(numbers)}")
print(f"  standard_deviation() = {standard_deviation(numbers):.2f}")
print()


#   Relative Imports
print("=" * 80)
print("Relative Imports (within packages):")
print("=" * 80)
print("""
Within a package, you can use relative imports to reference other modules:

ABSOLUTE IMPORT:
    from package.subpackage.module import function

RELATIVE IMPORT (from within package):
    from . import sibling_module
    from ..parent_package import module
    from .subpackage.module import function

Symbols:
    . = current package
    .. = parent package
    ... = grandparent package

EXAMPLE (in utilities_pkg/math_utils/__init__.py):
    from .calculations import add, divide
    from .statistics import mean

ADVANTAGES OF RELATIVE IMPORTS:
✓ Packages remain movable
✓ Explicit about package structure
✓ Cleaner import statements within packages
✓ Avoid absolute path complexity
""")

print()


#   Package Organization Best Practices
print("=" * 80)
print("Package Organization Best Practices:")
print("=" * 80)
print("""
1. CLEAR HIERARCHY
   ✓ Organize related functionality together
   ✓ Use subpackages for major functional areas
   ✗ Avoid overly deep nesting

2. MEANINGFUL NAMES
   ✓ Use descriptive package and module names
   ✗ Avoid generic names like 'utils', 'common'

3. SINGLE RESPONSIBILITY
   ✓ Each package handles one main area
   ✗ Don't mix unrelated functionality

4. DOCUMENTATION
   ✓ Include docstrings in __init__.py
   ✓ Document module purposes
   ✗ Don't leave __init__.py empty without reason

5. EXPLICIT EXPORTS
   ✓ Use __all__ to define public API
   ✓ Import and expose main functions in __init__.py
   ✗ Don't expose implementation details

6. AVOID CIRCULAR IMPORTS
   ✓ Plan module dependencies carefully
   ✗ Module A imports B and B imports A

7. CONSISTENT STRUCTURE
   ✓ Similar organization across packages
   ✗ Inconsistent patterns in different packages

8. TESTING INTEGRATION
   ✓ Include tests alongside code
   ✗ Separate tests far from implementation
""")

print()


#   Package Example: Data Processing System
print("=" * 80)
print("Complete Example: Data Processing Package")
print("=" * 80)
print()

# Create complete data processing package
data_pkg = "data_processing_pkg"
data_io = os.path.join(data_pkg, "io")
data_analysis = os.path.join(data_pkg, "analysis")

for directory in [data_pkg, data_io, data_analysis]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Main package __init__.py
with open(os.path.join(data_pkg, "__init__.py"), "w") as f:
    f.write('''"""
data_processing_pkg - Comprehensive data processing package.

This package provides tools for data input/output and analysis.
"""

from .io import reader, writer
from .analysis import statistics, aggregation

__version__ = "2.0.0"
__all__ = ['reader', 'writer', 'statistics', 'aggregation']
''')

# IO subpackage
with open(os.path.join(data_io, "__init__.py"), "w") as f:
    f.write('''"""
io - Input/Output operations subpackage.
"""

from . import reader
from . import writer
''')

# Reader module
with open(os.path.join(data_io, "reader.py"), "w") as f:
    f.write('''"""
reader.py - Data reading utilities.
"""

def read_csv_like(data):
    """Parse CSV-like data."""
    lines = data.strip().split('\\n')
    headers = lines[0].split(',')
    rows = []
    for line in lines[1:]:
        values = line.split(',')
        rows.append(dict(zip(headers, values)))
    return rows
''')

# Writer module
with open(os.path.join(data_io, "writer.py"), "w") as f:
    f.write('''"""
writer.py - Data writing utilities.
"""

def format_table(data, headers):
    """Format data as table."""
    # Calculate column widths
    col_widths = [len(h) for h in headers]
    for row in data:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))
    
    # Create table
    table = []
    table.append(' | '.join(h.ljust(col_widths[i]) for i, h in enumerate(headers)))
    table.append('-' * (sum(col_widths) + len(headers) * 3 - 1))
    
    for row in data:
        table.append(' | '.join(str(v).ljust(col_widths[i]) for i, v in enumerate(row)))
    
    return '\\n'.join(table)
''')

# Analysis subpackage
with open(os.path.join(data_analysis, "__init__.py"), "w") as f:
    f.write('''"""
analysis - Data analysis subpackage.
"""

from . import statistics
from . import aggregation
''')

# Statistics module
with open(os.path.join(data_analysis, "statistics.py"), "w") as f:
    f.write('''"""
statistics.py - Statistical analysis utilities.
"""

def calculate_mean(numbers):
    """Calculate mean."""
    return sum(numbers) / len(numbers)

def calculate_min_max(numbers):
    """Calculate min and max."""
    return min(numbers), max(numbers)
''')

# Aggregation module
with open(os.path.join(data_analysis, "aggregation.py"), "w") as f:
    f.write('''"""
aggregation.py - Data aggregation utilities.
"""

def sum_column(data, column_index):
    """Sum values in column."""
    return sum(row[column_index] for row in data)
''')

print("Created data_processing_pkg package with structure:")
print("  data_processing_pkg/")
print("    __init__.py")
print("    io/")
print("      __init__.py")
print("      reader.py (read_csv_like)")
print("      writer.py (format_table)")
print("    analysis/")
print("      __init__.py")
print("      statistics.py (calculate_mean, calculate_min_max)")
print("      aggregation.py (sum_column)")
print()


#   Using Complete Package
print("Using the complete data_processing_pkg:")
print()

from data_processing_pkg.io import reader, writer
from data_processing_pkg.analysis import statistics

# Create sample data
csv_data = """Name,Score,Grade
Alice,95,A
Bob,87,B
Charlie,92,A
Diana,78,C"""

# Read data
data = reader.read_csv_like(csv_data)
print("Parsed data:")
for row in data:
    print(f"  {row}")
print()

# Analyze data
scores = [int(d['Score']) for d in data]
print(f"Score statistics:")
print(f"  Mean: {statistics.calculate_mean(scores):.2f}")
print(f"  Min/Max: {statistics.calculate_min_max(scores)}")
print()


#   Package Advantages
print("=" * 80)
print("Advantages of Packages:")
print("=" * 80)
print("""
1. NAMESPACE MANAGEMENT
   ✓ Avoid naming conflicts
   ✓ Same module name in different packages
   
2. CODE ORGANIZATION
   ✓ Group related modules logically
   ✓ Large projects become manageable
   
3. REUSABILITY
   ✓ Share entire packages
   ✓ Easier to distribute code
   
4. MAINTAINABILITY
   ✓ Clear structure makes updates easier
   ✓ Related code stays together
   
5. SCALABILITY
   ✓ Easy to expand packages
   ✓ Add subpackages as needed
   
6. ENCAPSULATION
   ✓ Control what's exposed
   ✓ Hide implementation details
   
7. DOCUMENTATION
   ✓ Self-documenting structure
   ✓ __init__.py serves as entry point
   
8. PROFESSIONALISM
   ✓ Industry-standard organization
   ✓ Better for team collaboration
""")

print()


print("=" * 80)
print("SUMMARY OF PACKAGES")
print("=" * 80)
print("""
✓ Packages are directories containing modules and __init__.py
✓ __init__.py marks directory as package (can be empty)
✓ Use packages to organize related modules
✓ Create subpackages for hierarchical organization
✓ Use relative imports within packages
✓ Export items in __init__.py for easy access
✓ Define __all__ for explicit public API
✓ Avoid circular imports between modules
✓ Use meaningful, descriptive package names
✓ Keep packages focused on single responsibility
✓ Document packages and modules well
✓ Use __version__ and metadata in __init__.py
✓ Packages enable scalable, professional code organization
✓ Perfect for distributing reusable code
""")
