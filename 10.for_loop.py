# Topic Loops
# for Loop 

languages = ['Flutter', 'Python', 'Java', 'JavaScript']

# run a loop for each item of the list
for i in languages:
    print(i) 


 # for loop using String Static
value="Hello welcome"
for x in value:
   print(x)

for y in 'your name':
   print(y)

 # for loop using String dyanmic
name=input('Enter Your Name:')
 
for val in name:
    print('Your Name Character: '+val) 

# for loop using range() MIMP 
# use of range() to define a range of values
#values = range(5) # static Value
values = range(int(input('Enter Value:'))) # dyamic Value

for i in values:
    print("Range Function Value:",i)    
    
    
    

# for loop using with else statement
value = [0, 1, 5]

for i in value:
    print(i)
else:
    print("No items left.")