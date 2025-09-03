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

print("Steven", 3.14,10) #this is how we print in python

"""This 
is
a block
comment"""



# ==========================================================
# 2. VARIABLES AND DATA TYPES
# ----------------------------------------------------------
# - Strings
# - Integers, floats
# - Booleans
# - Type checking with type()
# ==========================================================

message = "Welcome to FIU"
print(type(message)) # type() is a function too

a = 10
b = 2
print(type(a).__name__,type(b).__name__)

isOpen = True
print(type(isOpen))

print(message[8])



# ==========================================================
# 3. BASIC OPERATORS
# ----------------------------------------------------------
# - Arithmetic (+, -, *, /, //, %, **)
# - Comparison (==, !=, >, <, >=, <=)
# - Logical (and, or, not)
# ==========================================================

print(a + b) #addition
print(a - b) #subtraction
print(a * b) #multiplication
print(a / b) #division
print(a // b) #Integer division
print(a ** b) #exponentiation
print(7 % 2) #Modulus (Remainder of the division)








# ==========================================================
# 4. STRING OPERATIONS
# ----------------------------------------------------------
# - Concatenation
# - f-strings
# - Common methods (.upper(), .lower(), .strip(), etc.)
# ==========================================================

first_name = "steven"
last_name = "benni"

print(first_name + last_name)
print(first_name + " " + last_name)
print(first_name,last_name)

print(f"My name is {first_name.upper()} {last_name.title()}.") #F indicates that {first_name} {last_name} are variables.
print(f"My name is {first_name} {last_name}.")
print("2" + "3")
print("***Welcome to Software Dev***".strip("*"))#Strip takes of what youd like to remove


# ==========================================================
# 5. LISTS
# ----------------------------------------------------------
# - Creating lists
# - Indexing and slicing
# - Adding/removing elements
# - Useful methods (.append(), .remove(), .sort(), etc.)
# ==========================================================

professors =["greg","richard","Steve","Ben","Noah","aaron","Casey"]
print(type(professors))
print(professors[0])
print(professors[-1]) #takes out the last one removes Casey, 2 would remove aaron
print(professors[2:5]) # acessing 2, 3, and 4
print(professors[:5]) # acessing from index 0 to 4
print(professors[3:]) # acessing indices from 3 to the end
print(professors[:])  #

professors.append("todd")#adds to the end, append adds 1 by 1
print(professors)
professors.extend(["Micheal", "mustafa", "naomi"])#extend adds all rather than once
print(professors)
professors.insert(2,"vyoma")
print(professors)
professors.remove("greg")
x = professors.pop(2)
print(professors,x)
professors.reverse()
print(professors)

professors.sort()
print(professors)
professors.sort(reverse=True)
print(professors)


# ==========================================================
# 6. TUPLES AND SETS
# ----------------------------------------------------------
# - Tuples: immutable sequences
# - Sets: unique collections
# ==========================================================

grades = (88.3, 78.6, 99.5)
print(type(grades))
#grades[0] = 91.3

members = {"greg","richard","greg"}
print(members)# this is going to be the answer pf a future assigment :))

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



