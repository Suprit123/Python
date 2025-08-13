# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# With the break statement we can stop the loop before it has looped through all the items:
car_brands = ["kia", "hyundai", "ford", "toyota"]
for brands in car_brands:
    print(brands)
    if brands == "ford":
        break
# In the below exampple we have prited the statement after the break. While in above example we have printed it before the break
car_brands = ["kia", "hyundai", "ford", "toyota"]
for brands in car_brands:
    if brands == "hyundai":
        break
    print(brands)

# The continue statement can stop the current iteration of the loop, and continue with the next
certifications = ["ccna", "ccnp", "ccie", "dba", "aws _networking", "aws_security"]
for certs in certifications:
    if certs == "dba":
        continue
    print(certs)

# We have added the print statement before continue if compared to above code where it's afterwards.
colors = ["red", "black", "orange", "purple", "pink"]
for dark in colors:
    print(dark)
    if dark == "black":
        continue

# To loop through a set of code a specified number of times, we can use the range() function
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(4):
    print(x)

# It is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 7):
    print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
for x in range(2, 30, 3):
    print(x)
