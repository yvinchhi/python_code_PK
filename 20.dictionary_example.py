# dict methods

'''
# methods of Dictionary
1. keys()
2. values()
3. update()
4. pop()
5. clear()
del keyword
'''

#1. Get All Key 
student = {
            "id": 1,
            "name": "yourname",
            "class": 'BTECH'
          }

# get All Keys
x = student.keys() # return all key name

print("Print All KEy : ",x)

# Get Single KEy value
x = student["name"]
print('Single Key Fetch : ' , x)

# Get Values
x = student.values()
print('Fetch All Values : ' ,x)

# Make a change in the original dictionary, 
# and see that the values list gets updated

# first way to update key values
x = student.values()
print('Before the change : ' ,x) 

student["class"] = 'BCA'
print('After the change : ', x)

#Add a new item to the original dictionary, 
# and see that the values list gets updated
x = student.values()
print('Before the change : ',x) 
student["year"] = 1999
print('After the change : ',x)

# second way to update dict.
# Update() method
stud = {
  "id": 1,
  "name": "yourname",
   "year": 2023 }

print('Update() Method Before : ',stud)
stud.update({"year": 1999})
print('Update() Method After : ',stud)

# Remove Items using pop() method
# The pop() method removes the item with 
# the specified key name:
dict = {
  "id": 1,
  "name": "yourname",
  "gender": 'Gender'
}

print('pop() Method Before: ',dict)
dict.pop("gender")
print('pop() Method After: ',dict)

#The del keyword removes the item with the 
# specified key name
del stud["id"]
print('use del Keyword : ',stud)

#The clear() method empties the dictionary
stud.clear()
print('use clear() method : ',stud)

# for LOOP using Dictionary
dict1 = {
  "id": 1,
  "name": "yourname",
  "gender": 'Gender'
}

# Print all key names in the dictionary, one by one
for x in dict1:
  print("print dict data using Loop KEY",x)
  
#Print all values in the dictionary, one by one
for x in dict1:
  print("print dict data using Loop Values", dict1[x])  

#You can also use the values() method to 
# return values of a dictionary
for x in dict1.values():
  print(x)
  
#You can use the keys() method to return 
# the keys of a dictionary
for x in dict1.keys():
  print(x)
     
# set multiple type value to dictionary
dict2 = {
    1: 'Hello',
   'two': True,
   '3': [1,2,3],
   'Four':{'id':1},
    1.1:2.2
}
print(dict2)

"""
# add value by user in to Dictionary 
# [dynamic dictionary]
# Allow the user to add name and age dynamically
while True:
    name = input("Enter a name (or 'exit' to stop): ")
    if name.lower() == 'exit':
          break

    try:
      age = int(input(f"Enter the age for '{name}': "))
    except ValueError:
        print("Please enter a valid age.")
        continue
 
    print(f"Name: {name}, Age: {age}")
    print("Name : {} Age : {}".format(name,age)) 
    print("Name :",name)
    print("Age:",age)
   """
# in Python, the f before a string in a 
# print statement indicates the use of a
# formatted string. 
# It's called an f-string or formatted 
# string literal. 
# F-strings provide a convenient way to 
# embed expressions and variables 
# inside a string for easier formatting.


# Initialize an empty dictionary usinf while loop
"""user_dict = {}

while True:
    key = input("Enter key  (or type 'exit' to stop): ")
    
    if key.lower() == 'exit':
        break
    
    value = input("Enter value: ")
    
    # Store key-value pair in dictionary
    user_dict[key] = value

print("\nFinal Dictionary:", user_dict)

"""
# Initialize an empty dictionary using for loop

user_dict = {}

# Ask user how many key-value pairs they want to enter
num_entries = int(input("How many key-value pairs do you want to enter? "))

# Use a for loop to get user input
for _ in range(num_entries):
    
    key = input("Enter key: ")
    value = input("Enter value: ")
    
    user_dict[key] = value  # Store key-value pair

print("\nFinal Dictionary:", user_dict)



