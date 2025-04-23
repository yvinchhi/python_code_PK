# dictionary is collection of Key Value Pair
# every key-value pair store in to {} braces
# each key-value pair seprated by , comma 
# and every key and Value seprated by : colon
# key must be unique and always in String Formate

# Create Dictionary

# Syntax
dict = {"name": "name",
        "Age": 25,
        "city":"Rajkot"}

print("First Dictionary Print ",dict);

dict["city"]="abccdd"   

print("second Dictionary Print ",dict);

dict["city"]="abc"
print("First Dictionary Print after update ",dict);

# Creating an empty Dictionary       
dict1 = {}       
print("Empty Dictionary: ",dict1)              
      
# Accessing Dictionary Value
Employee = {"Name": "yourname", 
            "Age": 25, 
            "Designation":'Flutter Developer', 
            "Company":"company name"}      

print("print the Data type :",type(Employee))      

print("Printing Employee Data")
print("---------------------------")      
print("Name : " ,Employee["Name"])      
print("Age :" ,Employee["Age"])      
print("Designation :" ,Employee["Designation"])      
print("Company : " ,Employee["Company"])

# Creating an empty Dictionary       
Dict = {}       
print("Empty Dictionary: ",Dict)       

# Adding elements to dictionary one at a time       
Dict[0] = 'A'      
Dict[1] = 'B'
Dict[2] = "name"  # Last one element print always     
Dict[2] = 'C'      
print("\n Dictionary after adding 3 elements: ")       
print(Dict)       

# Adding set of values with a single Key       
# The Emp_ages doesn't exist to dictionary      

Dict['Emp_ages'] = 24, 23.5, 'P'

# u have pass multiple value to single key      
Dict['City']="Rajkot"
print("\nDictionary after adding 3 elements: ")       
print(Dict)       

# Updating existing Key's Value       
Dict['City'] = 'Junagadh'      
print("\n Updated key value: ")       
print(Dict)  
       