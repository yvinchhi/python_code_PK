# function , contional statements ,loops , try-except ,dictionary
# user Info ADD UPDATE DELETE & DISPLAY using Dictionary

user_info = {}

# Add 
def add_user():
    name = input("Enter a name: ")
    try:
        age = int(input(f"Enter the age for '{name}': "))
        user_info[name] = age
        print(f"User '{name}' added successfully.")
    except ValueError:
        print("Please enter a valid age.")

# Update
def update_user():
    name = input("Enter the name to update: ")
    if name in user_info:
        try:
            new_age = int(input(f"Enter the new age for '{name}': "))
            user_info[name] = new_age
            print(f"Age for user '{name}' updated successfully.")
        except ValueError:
            print("Please enter a valid age.")
    else:
        print(f"User '{name}' not found.")


# Delete
def delete_user():
    name = input("Enter the name to delete: ")
    if name in user_info:
        del user_info[name]
        print(f"User '{name}' deleted successfully.")
    else:   
        print(f"User '{name}' not found.")


while True:
    print("\nOptions:")
    print("1. Add a user")
    print("2. Update a user's age")
    print("3. Delete a user")
    print("4. Display user information")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_user()
    elif choice == '2':
        update_user()
    elif choice == '3':
        delete_user()
    elif choice == '4':
        print("\nUser Information:")
        for name, age in user_info.items():
            #print(f"Name: {name}, Age: {age}")
            print("Name : ",name)
            print("Age : ",age)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")
