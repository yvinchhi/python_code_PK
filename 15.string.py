# ch.8 Introduction of String Syntax , declaration

# String Declaration with syntax [ 2 mark IMP ]

#string is collection of characters

# using Single Quotos
str1 = 'hello students' 
print(str1) 

# using double quotos
str2 = "string example using double quotes"  
print('String Value : ' , str2)  

# using triple quotos 
str3 = '''A multiline 
string example'''  
print(str3)   

#Strings indexing and splitting
str4 = "HELLO" 
print(str4[0])  
print(str4[1])  
print(str4[2])  
print(str4[3])  
print(str4[4])  
# It returns the IndexError because 6th index doesn't exist  
#print(str4[6])  


# Given String exxxample for range slice operator [2 mark IMP]
str5 = "Welcome"
  
# Start Oth index to end  
print(str5[0:]) #output: welcome   

# Starts 1th index to 4th index  
print(str5[1:5])  # output : elcom

# Starts 0th to 2nd index  
print(str5[:3])  #output : wel
 

# Delete the String

# As we know that strings are immutable.
# We cannot delete or remove the characters from the string.  
# But we can delete the entire string using the del keyword.

str6 = "Hello Welcome"  

#del str6[1] # not delete the particular charcter index

del str6  # delete entire String

#print(str6) # output  : str6 not found becuse str6 is deleted
 

# String Operations - operators [ 3 Marks MIMP]

str7 = "Hello"     
str8 = "world" 

# Repetation Operator (*)   
print('Repetation Operator :',str7*3)     
    
# concate operator (+)
print('Contacte Operator :',str7+str8)

# slice operator ( [] )     
print('Slice Operator :',str7[4]) # return the particular index character

# range slice operator ( [:] )                
print(str7[2:4]); # prints ll

# memebership Operator                    
print('w' in str8) # print false as w is not present in str8  if present then true  
print('wo' not in str8) # prints false as wo is present in str8.     
 

# format() method [ 2 Marks IMP]

# Using Curly braces  
print("{} and {} both are the best friend".format("X","Y"))  
  
#Positional Argument  
print("{0} and {1} best players ".format("A","B"))  
  
#Keyword Argument  
print("{a},{b},{c}".format(a = 10, c = 20, b = 30))  

                    