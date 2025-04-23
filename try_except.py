# for 3 to 5 marks

# the try and except blocks are used 
# to handle exceptions (errors) 
# that may occur during the execution of a program. 
# This mechanism is known as "exception handling". 

# 1. try: The code that might raise an exception 
# is placed in the try block.
# 2. except: The code that executes 
# if an exception occurs is placed in the except block.
# 3. finally: (Optional) The code that always executes

try:
    # Code that may raise different exceptions
    num = int(input("Enter a number: "))
    result = 10 / num
    print("RESULT = ",result)
    
except ValueError:
    # Code that runs if a ValueError occurs
    print("Error: Invalid input. Please enter a number.")

except ZeroDivisionError:
    # Code that runs if a ZeroDivisionError occurs
    print("Error: Cannot divide by zero.")

finally:
    # Code that always runs
    print("This block always executes.")

print("Program continues...")

