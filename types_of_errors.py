# Types of Errors

# 1.SyntaxError: This error occurs when the code contains 
# incorrect syntax.

# Missing colon in the  condition 
if age>18
    print("Hello, World!")

# Output: SyntaxError: invalid syntax

----------------------------------------------------------------------------------------------

# 2. IndentationError: This error occurs when there is an 

# Incorrect indentation
if n==3:
print('hello..')
print("Hello, World!")

# Output: IndentationError: expected an indented block 
# [if you not follow code structure]

----------------------------------------------------------------------------------------------

# 3.NameError: This error occurs when a variable or 
    
# Using an undefined variable
print(x)

# Output: NameError: name 'x' is not defined

----------------------------------------------------------------------------------------------

# 4. TypeError: This error occurs when an operation or function 
# is applied to an object of inappropriate type.

# Adding a string to an integer
result = 'Hello' + 5

# Output: TypeError: can only concatenate str (not "int") to str

----------------------------------------------------------------------------------------------

# 5. ValueError: This error occurs when a function receives 
# an argument of the right type but inappropriate value.

# Converting an invalid literal to int
number = int('hello')

# Output: ValueError: invalid literal for int() with base 10: 'abc'

----------------------------------------------------------------------------------------------

# 6. IndexError: This error occurs when trying to access an 
# element from a 
# list using an index which is out of range.

# Accessing an index that does not exist
my_list = [1,2,3,4,5] 
print(my_list[6])

# Output: IndexError: list index out of range

----------------------------------------------------------------------------------------------

# 7. KeyError: This error occurs when trying to access a 
# dictionary with a key that does not exist.

# Accessing a non-existent key in a dictionary
my_dict = {'name': 'Parul',}
print(my_dict['age'])

# Output: KeyError: 'age'

----------------------------------------------------------------------------------------------

# 8. AttributeError: This error occurs when an 
# invalid attribute is referenced.

# Accessing a non-existent attribute
my_list = [1, 2, 3]
my_list.append(4) # no error
my_list.push(5) # function not avalible

# Output: AttributeError: 'list' object has no attribute 'push'

----------------------------------------------------------------------------------------------

# 9. ImportError: This error occurs when an import statement 
# fails to find the module definition or when a from ... 
# import fails to find a name that is to be imported.  
# // module not found

# Importing a non-existent module
import non_existent_module

# Output: ImportError: No module named 'non_existent_module'

----------------------------------------------------------------------------------------------

# 10.ZeroDivisionError: This error occurs 
# when division or modulo by zero is performed.

# Dividing by zero
result = 10 / 0

# Output: ZeroDivisionError: division by zero

