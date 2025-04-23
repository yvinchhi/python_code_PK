# Arithmetic Opration using Functtion

# 1. Addition
# 2. Multiplication
# 3. Substraction
# 4. Division

# use if elif for operaion selection
# operation selection , num1 , num2 
# fetch from user then perfome operation


def perform_arithmetic_operation():
    print("Select the arithmetic operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation_choice = int(input("Enter the operation number (1-4): "))

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if operation_choice == 1:
        ans = num1 + num2
   
    elif operation_choice == 2:
        ans = num1 - num2
  
    elif operation_choice == 3:
        ans = num1 * num2
 
    elif operation_choice == 4:
        ans = num1 / num2

    else:
        print("Invalid operation choice.")
        return

    print("Answer = " , ans)

perform_arithmetic_operation()
