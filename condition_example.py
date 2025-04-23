age  = int(input("Enter Your Age:"))

#If age is less than 18, the person cannot vote. 
if age < 18:
    print("the person cannot vote.") 

#If age is exactly 18, they are eligible for the first time. 
elif age==18:
    print("they are eligible for the first time.")

else:
    print("they are eligible to vote.")
#If age is greater than 18, they are eligible to vote. 




























age = int(input("Enter your age: "))

if age < 18:
    print("You are not eligible to vote.")
elif age == 18:
    print("You are eligible to vote for the first time!")
else:
    print("You are eligible to vote.")
