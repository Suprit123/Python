try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# try: Python tries to execute the code that might raise an error.
try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    result = num1 / num2
# except: If an error occurs, it jumps to the matching except block
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter valid number.")
# else: If no exception occurs, the code inside else runs.
else:
    print(f"The result is: {result}")
