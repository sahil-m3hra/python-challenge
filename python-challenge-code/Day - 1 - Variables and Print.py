# ******************************** Variables *******************************
# Named memory locations in computer memory is known as a variable. Which holds value during the run time.
# Example: name, age, address, is_present etc.

# Rules for creating variable names:
# 1. Variable name should only starts with a letter or _.
# 2. There should be no space in between a variable name. We can use _ at the place of spaces.
# 3. No special characters allowed in a variable name.
# 4. A variable name can contains numbers in between or at the end of a variable name.
# 5. We cannot use keywords as a variable name.

# Examples of Valid variable name
# employee_id, is_present, first_name, age, _name etc.

# ********************************* print function *********************************
# When ever we want to display a message or output anything in python we can use print( )
# We can write the printing content inside the ( ) of print function.
# We can print multiple values using python print( ).
# example : print("Hello World!"), print(123)

# We can use different separators in print( ) like , (comma separator) is used when we want to display multiple and different datatype values in single print( ).
# We can use \t (tab separator) in between multiple values or in a string if we want 1 tab of spaces in between.
# We can use \n (new line separator) in between multiple values or in a string if we want them to print in on a next line.
# Example:
# print("Hello","Akhil",123)
# print("Hello\t123") or print("Hello\t", 123)
# print("Hello\n123") or print("Hello\n",123) 

# **********************************Code******************************

name = "Akhil"
age = 45
is_present = True

print("Hello", name)
print("Your age is: ", age)
print("Are you present today?: ", is_present)

# Printing using separators new line separator and tab space separator
print("******************** new line separator: ******************************")
print("Hello\n",name)
print("Your age is:\n ",age)
print("Are you present today?:\n",is_present)

print("********************* Tab space separator: **************************")
print("Hello\t",name)
print("Your age is:\t ",age)
print("Are you present today?:\t",is_present)

# ********************************* Data Types *********************************
# Datatypes define the type of data being stored inside a variable. Like in real world we deal with numbers, text, yes/no etc.
# Following are the basic datatypes available in Python.
# 1. int - these are the integer numbers like 10, -25, 100 etc. Like numbers without decimal point.
# 2. float - these are the numbers with decimal point like 25.6, -10.5 etc.
# 3. string - anything inside " " is treated as a string in python. like "Hello", "123" etc.
# 4. boolean - True and False without quotation marks.
# Syntax:
name = "John Doe" #string data type
age = 23 # integer data type
weight = 64.6 #float data type
is_present = True #boolean data type
address = "123, abc street, London 123456" #string data type

# We can use type() function to check the data type of any variable, value. type() return the datatype class
# E.g: 
print(type(name)) #<class 'str'>
print(type(age)) #<class 'int'>
print(type(weight)) #<class 'float'>
print(type(is_present)) #<class 'bool'>
print(type(address)) #<class 'str'>


# ********************************* Input function *********************************
# input() is used to accept values from user.
# Syntax:
# name = input("Enter your name: ")
# By default input() accepts every value in String data type.
# so we need to convert these values if we want to accept numbers and boolean values from user. This process of conversion is known as Type casting.
# we can write input() inside int() if we want to convert the input value (if it is a integer number but in string datatype e.g: "123")
# example:
age = int(input("Enter your age: "))
print(f"DataType of age value is {type(age)}")
# Similarly
# we can write input() inside float() if we want to convert the input value (if it is a floating number but in string datatype e.g: "123.56")
# example:
height = float(input("Enter your height: "))
print(f"DataType of height value is {type(height)}")
# we can write input() inside bool() if we want to convert the input value (if it is a True/False)
# example:
is_present = bool(input("Are you absent today? True/False "))
print(f"DataType of is_present value is {type(is_present)}")
# we can write input() inside str() if we want to convert the input value (if it is a number or bool type value)
# example:
address = str(input("Enter your address: "))
print(f"DataType of address value is {type(address)}")

# ********************************* Operators in Python *********************************
# Before understanding operators lets understand what an expression is: a+b-2=0
# a+b-2=0 this is a random expression for example: here a,b,2 are known as operands and +,-,= are known as operators.

# Operators are the symbols used to perform some specific task or calculation.
# There are two types of operators
# 1. Unary operators -> works with only single operand like +10, -b etc
# 2. Binary operators -> works with multiple operands like a + b = c
# There are 4 types of Binary operators:
    # 1. Arithmetic Operators - used to perform mathematical calculations.
    # 2. Relational Operators - used to compare 2 or more than 2 values and form a condition and the final answer will be in True/False.
    # 3. Logical Operators - used to compare two or more than 2 relational conditions
    # 4. Assignment operators - used to assign values to a variables.

# 1. Arithmetic Operators
# There are several operators in this category like:
# + (Addition)
# - (Subtraction)
# * (Multiplications)
# / (Division) -> return the quotient after division in floating data type
# // (Floor division) -> return the quotient after division in integer type. Basically it will exclude everything after the decimal point.
# % (Modulus) -> return the remainder value
# ** (Exponential) -> helps to find the power

# Example:
num1 = int(input("Enter first number: ")) #lets say 10
num2 = int(input("Enter first number: ")) #lets say 5
sum = num1 + num2 # 15
diff = num1 - num2 # 5
mul = num1 * num2 # 50
div = num1 / num2 # 2.0
floor_div = num1 // num2 # 2 
remainder = num1 % num2 # 0
exponent = num1 ** num2  # 100000

# In an expression, if multiple arithmetic operators are there the the execution will be done one the basis of PEMDAS and this order of priority of operators during execution is known as Precedence.
#                        _
# P - Parenthesis ( )    |   High
# E - exponential **     |   
# M - Multiplication *   |    to 
# D - Division / // %    |
# A - Addition +         |
# S - Subtraction -      V   low

                         

# 2. Relational Operators
# There are six relational operators in Python and returns final result in True/False.
# < - less than
# > - Greater than
# <= - less than equal to 
# >= - greater than equal to 
# == - equal to (checks equality)
# != - not equal to

# example:
a = 10
b = 5

print(a<b) # False
print(a>b) # True
print(a<=b) # False because neither 10 is less than nor equal to 5
print(a>=b) # True because 10 is greater than 5 so it will not check for the equality here.
print(a==b) # False
print(a!=b) # True

# 3. Logical Operators
# There are 3 logical operators in python i.e && (and) , || (or) , not(). They are used to compare 2 or more than 2 relational conditions.
# Example:
# and -> and will return True as a final answer if all the relational conditions will return True otherwise it will return False.
# or -> or will return True as a final answer if any of the relational condition will return True other will it will return False.
# not(relational conditions) -> It reverse the answer. If the relational conditions answer is True then it will reverse it to False and Vice-versa.
num1 = 10
num2 = 5
num3 = 12
# print((num1 > num2) and (num2 < num3)) -> It will return True as final answer because both relational conditions will return true here.
# print((num1 > num2) or (num2 > num3)) -> It will return True as final answer because first relational conditions will return true and second relational condition will return false so final answer will be True.
# print(not(num1 > num2 and num2 < num3)) -> It will return True first but not() will reverse it so final answer will be False.


# ********************************* Assignment operators in Python *********************************
# = -> Assignment Operator used to assign values to a variable.
# a = 10
# name = "Akhil"

# += -> used to add right side value to left side variable. e.g :
# age = 25
# instead of age = age + 5 we can do the following
# age += 5
# print(age) -> 30

# -= -> used to subtract right side value to left side variable. e.g :
# age = 25
# instead of age = age - 5 we can do the following
# age -= 5
# print(age) -> 20

# *= -> used to multiply right side value to left side variable. e.g :
# age = 5
# instead of age = age * 5 we can do the following
# age *= 5
# print(age) -> 25

# /= -> used to divide right side value to left side variable. e.g :
# age = 25
# instead of age = age / 5 we can do the following
# age /= 5
# print(age) -> 5

