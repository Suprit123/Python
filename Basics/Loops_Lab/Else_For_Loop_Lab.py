# The else keyword in a for loop specifies a block of code to be executed when the loop is finished

# When to use for-else:
# Use it when you're searching for something or waiting for a condition inside a loop and want to take an action if it was never met.
for r in range(6):
    print(r)
else:
    print("Finally finished!")

# The else block will NOT be executed if the loop is stopped by a break statement.
for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("loop completed without break")

# Searching the for a value
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    if num == 5:
        print("Found!")
        break
else:
    print("Not Found.")
