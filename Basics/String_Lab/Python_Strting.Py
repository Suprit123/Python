# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# You can display a string literal with the print() function:

print("Hello")
print("Hello")

# You can use quotes inside a string, as long as they don't match the quotes surronding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assigning a string to a variable is done with the varaible name followed by an equal sign and the string:
a = "Hello"
print(a)

# You can assign a multiline string to a variable by using three double quotes or three single quotes.
bgp = """Router bgp 
neighbor 1.1.1.1 remote-as 100
network 192.168.1.0 mask 255.255.255.0
"""
print(bgp)

# Square brackets can be used to access the elements of the string.
a = "Hellow World!"
print(a[1])

# Looping through a String
for x in "banana":
    print(x)

# To get the length of a string, use the len() function.
a = "Hello World"
print(len(a))

# Check if "free" is present in the following text: The output will be true or false.
txt = "The best things in life are free"
print("free" in txt)

# Print only if "free" is preset
txt = "The best things in life are free"
if "free" in txt:
    print("Yes", "free is present.")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in. The output will be true or false.
txt = "The best things in life are free"
print("expensive" not in txt)

# Loop
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No", "expensive is NOT present.")
