# The remove() method removes the specified item.
# If there are duplicates values the remove() menthod removes the first occurance.
fruits = ["apples", "banana", "cherry", "mangoes"]
fruits.remove("cherry")
print(fruits)

# The pop() method removes the specified index.
# If you do not specify the index, the pop() method removes the last item.
car_brands = ["kia", "hyundai", "toyota", "bmw", "audi", "ford"]
car_brands.pop(4)
print(car_brands)

# The del keyword also removes the specified index:
certifications = ["ccna", "ccnp", "ccie", "sysadmin", "aws networking"]
del certifications[-2]
print(certifications)

# The del keywork can also delete the list completely.
colors = ["red", "blue", "green"]
del colors

# The clear menthod empties the list.
alphabets = ["a", "b", "c"]
alphabets.clear()
print(alphabets)
