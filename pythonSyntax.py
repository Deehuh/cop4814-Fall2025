"""
Basic Python Syntax
----------------------------
This file is a guided template for learning Python basics.
Students should fork and clone this repository from Greg's repo.
Explanations and examples will be added by Greg.
"""

# ==========================================================
# 1. PRINTING AND COMMENTS
# ----------------------------------------------------------
# - Print statements
# - Single-line comments
# - Multi-line comments (docstrings)
# ==========================================================

print("Gregory",9,3,2025)

""" This is a comment bro"""

# ==========================================================
# 2. VARIABLES AND DATA TYPES
# ----------------------------------------------------------
# - Strings
# - Integers, floats
# - Booleans
# - Type checking with type()
# ==========================================================

message = "Welcome to FIU"
print(type(message)) # type() is a function

a = 10
b = 2
print(type(a), type(b))

isOpen = True
print(type(isOpen))

print(message[0])

# ==========================================================
# 3. BASIC OPERATORS
# ----------------------------------------------------------
# - Arithmetic (+, -, *, /, //, %, **)
# - Comparison (==, !=, >, <, >=, <=)
# - Logical (and, or, not)
# ==========================================================
print (a + b) # addition
print (a - b) # subtraction
print (a * b) # multiplication
print (a / b) # division
print (7 / 5) # division again
print (7 // 5) # integer division
print (a ** b) # exponentiation
print (a % b) # modulus

# ==========================================================
# 4. STRING OPERATIONS
# ----------------------------------------------------------
# - Concatenation
# - f-strings - formats curly brackets
# - Common methods (.upper(), .lower(), .strip(), etc.)
# - Cannot use operations for two different data types Ex: '+' between an int & string
# ==========================================================

first_name = "demetrius"
last_name = "smith"

print(first_name + last_name)
print(first_name + " " + last_name)
print(first_name, last_name)

print(f"My name is {first_name.upper()} {last_name.title()}.")
print("2" + "3")
print("***Welcome to Software Dev***".strip('*'))
# ==========================================================
# 5. LISTS
# ----------------------------------------------------------
# - Creating lists
# - Indexing and slicing
# - Adding/removing elements
# - Useful methods (.append(), .remove(), .sort(), etc.)
# ==========================================================

animals = ["zebra", "lion", "tiger", "elephant", "squirrel", "anteater"]
print(type(animals))
print(animals[0])
print(animals[-1])
print(animals[2:5]) # accessing indices 2,3, and 4; not upper bound
print(animals[:5]) # accessing from index 0 to 4
print(animals[3:]) # accessing indices 3 to the end
print(animals[:]) # can prevent looping errors by copying the list

animals.append("gorilla") # append is one value at a time
print(animals)
animals.extend(["frog", "buffalo", "cheetah"]) # extend can add multiple values at once
print(animals)
animals.insert(2,"bear") # chooses a position to add values
print(animals)
animals.remove("tiger")
print(animals)
x=animals.pop(5)
print(animals,x)
animals.reverse() # reverses order of the list
print(animals)

animals.sort()  # alphabetically
print(animals)
animals.sort(reverse=True) # reverses the sorting
print(animals)


# ==========================================================
# 6. TUPLES AND SETS
# ----------------------------------------------------------
# - Tuples: immutable sequences
# - Sets: unique collections
# ==========================================================

grades = (88.3, 78.6, 99.5)
print(type(grades))
# grades[0]= 91.3

members = {"greg", "richard", "greg"}
print(members) # answer for a future assignment


# ==========================================================
# 7. DICTIONARIES
# ----------------------------------------------------------
# - Key-value pairs
# - Accessing and modifying values
# - Common methods (.keys(), .values(), .items())
# ==========================================================



# ==========================================================
# 8. CONDITIONALS
# ----------------------------------------------------------
# - if, elif, else
# - Nested conditionals
# ==========================================================



# ==========================================================
# 9. LOOPS
# ----------------------------------------------------------
# - for loops
# - while loops
# - break and continue
# ==========================================================



# ==========================================================
# 10. FUNCTIONS
# ----------------------------------------------------------
# - Defining functions
# - Parameters and return values
# - Default arguments
# ==========================================================



# ==========================================================
# 11. IMPORTING MODULES
# ----------------------------------------------------------
# - Importing built-in modules (e.g., math, random)
# - Using functions from modules
# ==========================================================



# ==========================================================
# 12. ERROR HANDLING (OPTIONAL)
# ----------------------------------------------------------
# - try, except
# - Handling different exception types
# ==========================================================



