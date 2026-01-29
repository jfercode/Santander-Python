#   File Operations

#   What are File Operations?
"""
    Python allows us to read and write data in external files. We can open files in
    different modes, such as reading ("r"), writing ("w"), or appending ("a"), and
    perform read and write operations.
    
    File operations are essential for:
    - Saving data persistently
    - Processing large amounts of data
    - Creating logs and reports
    - Data analysis and manipulation
    - Backing up information
"""


#   File Opening Modes
"""
    When opening a file with open(), you must specify the mode:
    
    "r"  - Read (default): Opens file for reading. File must exist.
    "w"  - Write: Opens file for writing. Creates file if it doesn't exist,
           truncates (clears) if it exists.
    "a"  - Append: Opens file for appending. Creates file if it doesn't exist,
           adds to end if it exists.
    "r+" - Read and Write: Opens file for both reading and writing.
    "x"  - Create: Creates a new file. Fails if file already exists.
    
    Binary modes:
    "rb" - Read binary
    "wb" - Write binary
"""

print("=" * 80)
print("File Operations in Python:")
print("=" * 80)
print()


#   Reading Files
"""
    To read the content of a file, we first open it using the open() function in
    read mode ("r"). Then, we can read the content using methods like read() or
    readlines().
    
    Key methods:
    - read(): Returns the entire file content as a string
    - readline(): Returns one line at a time
    - readlines(): Returns all lines as a list
"""

print("=" * 80)
print("Reading Files:")
print("=" * 80)
print()

# Example 1: Basic file reading with read()
print("Example 1: Reading entire file content with read()")
print()

try:
    archivo = open("sample.txt", "r")
    contenido = archivo.read()
    print(contenido)
    archivo.close()
except FileNotFoundError:
    print("Note: sample.txt file not found. Creating example content...")
    # Create a sample file for demonstration
    with open("sample.txt", "w") as f:
        f.write("Line 1: Hello, World!\n")
        f.write("Line 2: Welcome to Python.\n")
        f.write("Line 3: File operations are useful.\n")
    
    # Now read it
    with open("sample.txt", "r") as f:
        contenido = f.read()
        print(contenido)

print()


# Example 2: Reading file line by line with readline()
print("Example 2: Reading file line by line with readline()")
print()

try:
    with open("sample.txt", "r") as archivo:
        line1 = archivo.readline()
        line2 = archivo.readline()
        print("First line:", line1.strip())
        print("Second line:", line2.strip())
except FileNotFoundError:
    print("File not found")

print()


# Example 3: Reading all lines with readlines()
print("Example 3: Reading all lines with readlines()")
print()

try:
    with open("sample.txt", "r") as archivo:
        lineas = archivo.readlines()
        for i, linea in enumerate(lineas, 1):
            print(f"Line {i}: {linea.strip()}")
except FileNotFoundError:
    print("File not found")

print()


# Example 4: Iterating through file lines
print("Example 4: Iterating through file lines (memory efficient)")
print()

try:
    with open("sample.txt", "r") as archivo:
        for numero_linea, linea in enumerate(archivo, 1):
            print(f"Line {numero_linea}: {linea.strip()}")
except FileNotFoundError:
    print("File not found")

print()


#   Writing Files
"""
    To write data to a file, we open it in write mode ("w") using the open() function.
    If the file doesn't exist, it will be created automatically. If the file already
    exists, its content will be overwritten.
    
    Key methods:
    - write(): Writes a string to the file
    - writelines(): Writes a list of strings to the file
"""

print("=" * 80)
print("Writing Files:")
print("=" * 80)
print()

# Example 1: Basic file writing
print("Example 1: Writing content to a new file")
print()

archivo = open("greeting.txt", "w")
archivo.write("Hello, World!\n")
archivo.write("This is a test file.\n")
archivo.write("File operations are fundamental in programming.\n")
archivo.close()

print("File 'greeting.txt' has been created with content.")

# Read and display the file
with open("greeting.txt", "r") as f:
    print("\nContent of greeting.txt:")
    print(f.read())

print()


# Example 2: Writing with multiple calls
print("Example 2: Writing data from variables")
print()

name = "Alice"
age = 30
city = "Boston"

with open("user_info.txt", "w") as archivo:
    archivo.write(f"Name: {name}\n")
    archivo.write(f"Age: {age}\n")
    archivo.write(f"City: {city}\n")

print("File 'user_info.txt' has been created.")

# Read and display the file
with open("user_info.txt", "r") as f:
    print("\nContent of user_info.txt:")
    print(f.read())

print()


# Example 3: Writing multiple lines at once
print("Example 3: Writing multiple lines with writelines()")
print()

lines = [
    "First line of the file\n",
    "Second line of the file\n",
    "Third line of the file\n"
]

with open("multiline.txt", "w") as archivo:
    archivo.writelines(lines)

print("File 'multiline.txt' has been created.")

# Read and display the file
with open("multiline.txt", "r") as f:
    print("\nContent of multiline.txt:")
    for linea in f:
        print(f"  {linea.strip()}")

print()


#   Appending to Files
"""
    The append mode ("a") allows us to add content to the end of an existing file
    without overwriting the current content.
"""

print("=" * 80)
print("Appending to Files:")
print("=" * 80)
print()

# First, create a file with initial content
with open("log.txt", "w") as f:
    f.write("[2026-01-29] Program started\n")

print("Initial log.txt created with content.")

# Append new entries
with open("log.txt", "a") as f:
    f.write("[2026-01-29] User logged in\n")
    f.write("[2026-01-29] Data processed\n")
    f.write("[2026-01-29] Program ended\n")

print("Additional lines appended to log.txt")

# Read and display the complete file
print("\nComplete log.txt content:")
with open("log.txt", "r") as f:
    print(f.read())

print()


#   The WITH Statement (Context Manager)
"""
    The with statement is the recommended way to handle file operations. It
    automatically closes the file when exiting the block, even if an exception occurs.
    
    Benefits:
    - Automatic file closure
    - Exception safe
    - Cleaner, more readable code
    - No need to manually call close()
    
    Syntax:
    with open(filename, mode) as variable:
        # File operations
        statements
"""

print("=" * 80)
print("Using the WITH Statement (Best Practice):")
print("=" * 80)
print()

# Example 1: WITH for reading
print("Example 1: Reading with WITH statement")
print()

with open("sample.txt", "r") as archivo:
    contenido = archivo.read()
    print("File content read successfully with WITH statement")
    print(contenido)

print()


# Example 2: WITH for writing
print("Example 2: Writing with WITH statement")
print()

with open("poem.txt", "w") as archivo:
    archivo.write("Roses are red,\n")
    archivo.write("Violets are blue,\n")
    archivo.write("Python is awesome,\n")
    archivo.write("And so are you!\n")

print("Poem written successfully with WITH statement")

# Read back
with open("poem.txt", "r") as archivo:
    print("\nPoem content:")
    print(archivo.read())

print()


#   File Operations with Error Handling
"""
    File operations can raise exceptions such as:
    - FileNotFoundError: When trying to read a file that doesn't exist
    - IOError: When there's an input/output problem
    - PermissionError: When lacking permissions to access the file
    
    Always use try-except blocks to handle these exceptions gracefully.
"""

print("=" * 80)
print("File Operations with Error Handling:")
print("=" * 80)
print()

def safe_read_file(filename):
    """Safely read a file with error handling."""
    try:
        with open(filename, "r") as archivo:
            contenido = archivo.read()
            print(f"Successfully read {filename}")
            return contenido
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")
        return None


print("Example: Trying to read existing and non-existing files")
print()

# Try reading existing file
content = safe_read_file("sample.txt")
if content:
    print(f"Content length: {len(content)} characters\n")

# Try reading non-existing file
content = safe_read_file("nonexistent.txt")

print()


#   Practical Example: Data Processing
print("=" * 80)
print("Practical Example: Processing Data from Files:")
print("=" * 80)
print()

# Create a CSV-like file
data_file = "students.txt"

with open(data_file, "w") as f:
    f.write("Name,Score,Grade\n")
    f.write("Alice,95,A\n")
    f.write("Bob,87,B\n")
    f.write("Charlie,92,A\n")
    f.write("Diana,78,C\n")
    f.write("Eva,88,B\n")

print(f"Created {data_file} with student data\n")

# Read and process the file
print("Processing student data:")
print()

total_score = 0
student_count = 0

with open(data_file, "r") as f:
    # Skip header
    header = f.readline()
    print(header.strip())
    print("-" * 30)
    
    for linea in f:
        parts = linea.strip().split(",")
        if len(parts) == 3:
            name, score, grade = parts
            score = int(score)
            
            print(f"{name:<10} {score:>5} {grade:>5}")
            total_score += score
            student_count += 1

if student_count > 0:
    average = total_score / student_count
    print("-" * 30)
    print(f"Average Score: {average:.2f}")

print()


#   Best Practices for File Operations
print("=" * 80)
print("Best Practices for File Operations:")
print("=" * 80)
print("""
    1. ALWAYS USE WITH: Use 'with' statements for file operations
    2. HANDLE ERRORS: Use try-except for file operations
    3. CHECK EXISTENCE: Verify files exist before reading
    4. CLOSE FILES: Always close files (with statement does this)
    5. USE ABSOLUTE PATHS: Use full paths or relative paths carefully
    6. HANDLE ENCODING: Specify encoding if needed (UTF-8 is default)
    7. BE CAREFUL WITH MODES: "w" mode overwrites, use "a" for append
    8. MANAGE RESOURCES: Don't keep files open longer than necessary
    9. LOG OPERATIONS: Record file operations for debugging
    10. TEST EDGE CASES: Test with empty files, large files, etc.
""")

print()

print("=" * 80)
print("SUMMARY OF FILE OPERATIONS")
print("=" * 80)
print("""
✓ Use open() to work with files
✓ Use read() to get entire content
✓ Use readline() for single lines
✓ Use readlines() for all lines as list
✓ Use write() to write content
✓ Use writelines() for multiple lines
✓ Use "w" mode to write (overwrites)
✓ Use "a" mode to append (adds to end)
✓ Always use 'with' statement for file handling
✓ Always handle FileNotFoundError and IOError
✓ Use try-except blocks for error handling
✓ Always close files when done
✓ Consider file encoding
✓ Follow best practices for robust code
✓ Test with different file scenarios
""")
