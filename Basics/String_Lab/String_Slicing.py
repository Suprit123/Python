# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Hello, world!!"
print(b[2:5])

# By leaving out the start index, the range will start at the first character.
b = "Hello, world!"
print(b[:5])

# By leaving out the end index, the range will go to the end.
b = "Hello, world!"
print(b[2:])
