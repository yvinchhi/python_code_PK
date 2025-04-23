# Ch. 9 String Method [MIMP 3 to 5 Mark ]

''' 
 1. capitalize()
 2. count()
 3. endswith()
 4. startwith() 
 5. isalpha()
 6. isdigit()
 7. islower()
 8. isupper()
 9. lower()
 10. upper()
'''

# upper & lower and isUpper() & isLower()
text1 = "Hello, World!"
print(text1.upper())  # Output: 'HELLO, WORLD!'
print(text1.lower())  # Output: 'hello, world!'

print(text1.islower())  # return type is boolean 
print(text1.isupper())  


# Strip() : Remove leading and trailing whitespace from a string. [1 mark mcq]
text2 = "   Python is fun!   "
print(text2)
print(text2.strip())  # Output: 'Python is fun!'


# split() : Split a string into a list of substrings based on a delimiter.[2 mark]
text3 = "Python,java,JavaScript,android,flutter"
languages = text3.split(",")
print(languages)  # Output: ['Python', 'Java', 'JavaScript']


# join() : Join a list of strings into a single string using a delimiter.
languages = ['Python', 'Java', 'JavaScript']
text4 = ",".join(languages)  # u have to pass any delimiter like [, - .]
print(text4)  # Output: 'Python, Java, JavaScript'


# startswith() & endswith() : return type Boolean
# Check if a string starts or ends with a specific substring. 
text5 = "Hello, World! Welcome" 
# u have to pass both single character and Word 
print(text5.startswith("Hello")) #outut : True
print(text5.endswith("e"))   # Output: True


# replace() : 
text6 = "Hello, World!"
new_text = text6.replace("World", "Student") 
# u have pass both Character and entire word
print(new_text) 


# find() & index() : Find the first occurrence of a substring in a string.
text7 = "Hello, World! Student"
print("Find Method:",text7.find("Student"))  #  return type indext [int value]
print("Index MEthod :",text7.index("World"))  

# count() : 
text8 = "How much good food? i like good healthy food"
print(text8.count("good"))  # Output: 2
print(text8.count("o"))

# isalpha() & isDigit() return type boolean
text9 = "Hello" 
text10 = "12345"
print(text9.isalpha())  # Output: True
print(text10.isdigit())  # Output: True

# capitalize() 
text11 = "hello, world!,student" # entire string first charcter Capitalize
print(text11.capitalize())  # Output: 'Hello, world!, student'


    





    







