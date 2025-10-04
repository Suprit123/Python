# The try block lets you test a block of code of errors.

# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:

try:
    print(x)
except:
    print("An exception occured")

# Inside try, we do 10/0 - but dividing by zero is not allowed in match or python. Python raises a ZeroDivisionError.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero! ")


# Handling Invalid input by ValueError:
try:
    num = int(input("Enter a number: "))
    print(f"You entered {num}")
except ValueError:
    print("That's not a valid number.")

# Handling file not found with FilenotFoundError:
try:
    with open("non_existent_file.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found!")

# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

# Print one message if the try block raises a NameError and another for other errors:
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong.")
