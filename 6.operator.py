#Type of Operators in Python

''' 
1. Arithmetic  [ + , - , * , / , //]
2. Comparison  [ == , != , < , > , <= , >= ,   ]
3. Assignment  [ += , -= , *= , /= ]
4. Logical     [ and , or , not ]
5. Membership  [ in , not in ]
6. Identity    [ is , is not ]

'''


# 1. Arithmetic OP
a = int(input("Enter the Value A:"))
b = int(input("Enter the Value of B:"))


print("Airthmetic Operations")
print("===============================")

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# floor division
print ('Floor Division: ', a // b)

print('--------------------------------------')
 
# 2. Comparision OP

print('Comparision Operatos')
print("==================================")

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)

print('--------------------------------------')
 
# 3. Assignment OP

print('Assignment Operatos')
print("==================================")

# assign the sum of a and b to a
a=10
b=20

a += b 
print('Addition = ', a) 

a *= b 
print('Multiplication = ', a) 

a -= b
print('Substraction = ', a) 

a /= b     
print('Division = ', a) 


print('--------------------------------------')

# 4. Logical OP
ab=5

print("Logical Operator")
print("==================================")

# logical AND    return true both cond are true otherwise false
print("AND Operator : ",ab>5 and ab<10)   

# logical OR return true any one cond. will be true otherwise
print("OR Operator : ",ab>5 or ab<10)     

# logical NOT
# Using 'not' operator
print('NOT Operator:',not (ab > 4)) 
           
print('--------------------------------------')           

# 5. Membership OP
x = 'Hello world'

print("Membership Operator")
print("==================================")

# check if 'H' is present in x string
print('H' in x)  # prints True

# check if 'hello' is present not in x string
print('Hello' not in x)  # prints False

print('--------------------------------------') 

# 6. Identity OP

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello' 

print("Identity Operator")
print("==================================")

print(x1 is not y1)  
print(x2 is y2)  
  
 
 
 
 
 
 
 
 