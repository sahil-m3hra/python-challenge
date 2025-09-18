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
    print("Sorry! You are underage now. Try next year.") #this will print only if the condition returns False.

# ******************************* Nested if-else *****************************
# when we use condition statement inside conditional statements.
# Syntax:
# if (condition1):
#     # Do something
#     if (condition2):
#         # Do something
#     else:
#         # Do Something
# else:
#     if (condition3):
#         # Do something
#     else:
#         # Do something

# example: Checking if a entered year is a leap year or not.
year = int(input('Please enter a year: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, 'is a leap year.')
        else:
            print(year, 'is not a leap year.')
    else:
        print(year, 'is a leap year.')
else:
    print(year, 'is not a leap year.')

# ******************************* if-elif-else *****************************
# If there are multiple conditions to check then we can use if-elif-else.
# Syntax:
# if(condition1):
#     # Do something
# elif (condition2):
#     # Do something
# elif (condition3):
#     # Do soemthing
# elif (condition4):
#     # Do something
# else:
#     # Do something

# example: Age checker for liquor eligibility program
age = 25
if age < 18:
    print("You are not old enough to vote.")
elif age < 21:
    print("You can vote but cannot drink alcohol.")
else:
    print("You can vote and drink alcohol.")