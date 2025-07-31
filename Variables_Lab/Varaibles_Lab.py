# In these lab we will see how to use variables in python.

# Some variable rules that needs to be considered.
# 1) Cannot start with numbers
# 2) After the initial character variable names can contain letters (A-Z, a-z) numbers(0-9) and underand underscores (_). No other special characters (like !, @, #, $, %, spaces, hyphens) are allowed
# 3) Python variable names are case-sensitive. age, Age, and AGE are considered three distinct variables.
# 4) You cannot use Python's reserved keywords (e.g., if, for, while, class, True, False, None) as variable names, as these have special meanings in the language

# In the below example message word is the key and the value is give after = sign and it's a string. Also = sign in python is called assignment operator 
message = "Welcome to the variables lab"
print(message)

# In the below example we will be seeing how to print the below message characters all in upper case by using print method. the upper is an inbuilt method in python
training = "welcome to the ccna devnet course"
print(training.upper())

# We can also print all the characters in lower case by using lower method. This is also an inbuilt method.
name = "NETWORK-NINJA"
print(name.lower())

# By using the capitalize method we can print the intial character first alaphabet in upper case.
string = "hello world"
print(string.capitalize())

# If we want to permanantely change the upper case into lower we need to define into the vriable itself the lower method.
name = name.lower() # Refer NETWORK-NINJA example for this.

# In the below exmample we will see how to print the first alphabet of each character by using the title method.
variable = "this is a variable lab for python"
print(variable.title())

# The below print function will give the output for all the vriables that have been created.
print(globals())

# In the below function we are going to replace opsf with ospf by using replace method.
commands = """router opfs"""
print(commands.replace("opfs", "ospf"))