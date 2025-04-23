# Create Function - Syntax 

# A function is a block of code that runs 
# whenever we call it.

# creating and defining the function using def keyword

def demoFunction():
    print("Hello Welcome to Function")

# Calling Function
demoFunction()   


# types of Functions [arguments]

# 1. Defualt Argument

def defualt_function(v1, v2 = 10):    
    print("Value v1 is: ", v1)    
    print("Value v2 is: ", v2)    
         
# Calling the function and passing only one argument    
print("Passing only one argument")    
defualt_function(20) 
   
# Now giving two arguments to the function    
print("Passing two arguments")    
defualt_function(40,50)     

# 2.Keyword Argument 
def keyword_function(n1,n2,n3):    
    print("Value n1 is: ", n1)    
    print("Value n2 is: ", n2)    
    print("Value n3 is: ", n3)    
       
print( "Without using keyword" )    
keyword_function(10,20,30)       
        
print( "With using keyword" )    
keyword_function(n1=100,n3=200,n2=500)    


# 3. Required Argument function

def requiredFunction(n1, n2,n3):    
    print("n1 is Id: ", n1)    
    print("n2 is Name: ", n2) 
    print("n3 is Age: ", n3)    
    
requiredFunction(1,'yourname',25)       
       


# 4. Variable Length Argument [MIMP for 2 & 3 marks]

# If you do not know how many arguments that will be 
# passed into your function, 
# add a * before the parameter name in the function definition.

# type -1 using single * sign
def variableLengthFunction(*args_list):    
    # create empty list
    ans = []    
    
    for i in args_list:    
        ans.append(i)    
    return ans    
  
# Passing args arguments    
object1 = variableLengthFunction('Python', 'Functions', 'tutorial',1,2,3,4,5,6)    
print('Varibale length function call 1 :',object1)    
    
object2 = variableLengthFunction(1,2,3,4,5)    
print('Varibale length function call 2:',object2)    

object3 = variableLengthFunction('parul')    
print('Varibale length function call 3:',object3)

    
# defining a ** function   

# If you do not know how many keyword arguments that will be passed into 
# your function,
# add two asterisk: ** before the parameter name in the function definition.
# item() is pre define method for store key value pair data

def function(**kargs_list):    
    ans = []    
    for key, value in kargs_list.items():    
        ans.append([key, value])    
    return ans    
  
# Paasing kwargs arguments    
object = function(Firsts = "Python", Seconds = 2, Third = 24.5,abc=10)    
print('Keyword Argurment function 1 :',object)     

object = function(Firsts = 1, Seconds = 'Parul')    
print('Keyword Argurment function 2 :',object)     



# Return Function Value
def return_function(x):
  return 5 * x #10


def return_fun(a,b):
    ans = a+b
    return ans

print('Return Type Function 1:',return_function(2))
print('Return Type Function 2:',return_fun(5,5)) 

# multiple returns

def multiple_return_fun():
    first = 'today temp : ',40
    second = 'yesterday temp : ',35
    third = 'tomorrow temp : ',35
    print(first,second,third)
    return first,second,third

multiple_return_fun()

# globle variable 
a1=10

def demo1(a1):
    print('inside function A Value :',a1)

demo1(a1)
print('outside function A Value :',a1)

# local variable
def demo2():
    a2=20
    print('inside demo2 :',a2)
    
demo2()
#print('outside ',a2); # a2 is local varibale   



# dynamic Function

def fetch_user_info():
    
    # user id
    user_id = int(input("Enter your ID: "))
   
    # user name
    name = input("Enter your name: ")

    # user age
    age = int(input("Enter your age: "))
    
    print("user id ",type(user_id))
    
    # Print information
    print("Name:",name)
    print("ID:",user_id)
    print("Age:",age)

# call functioin
fetch_user_info()


# user define function

def demo(name):
    print("name : ",name)
    
demo("parul")

# built in function

'''
len()
max()
min()
input()
range()
type()
print()
'''

