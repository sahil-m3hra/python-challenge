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


