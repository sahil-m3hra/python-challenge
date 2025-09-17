# Day - 3 - Control Flow and Logical Operators

# Control flow statements helps us to change the flow of the program based on a condition(either True or False).
# Syntax:
# if(condition):
#     Do Task1
# else:
#     Do Task2

# Example:
# if(is_it_raining_outside):
#     print("Carry Umbrella")
# else:
#     print("We dont need umbrella.")
# In the above example out of 2 print functions only one will execute depending upon the output of the condition passed inside the if().

# Real Example:
print("Welcome to Driving license Eligibility checker program")
age = int(input("Enter your age: "))
if(age >= 18): #Here i am using relational operator to check whether the age is equal or greater than 18. this condition will return True or False.
    print("You are eligible for Driver License.") #this will print only if the condition returns True
else:
    print("Sorry! You are underage now. Try next year.") #this will print only if the condition returns False