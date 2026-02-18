# List items are indexed and you can access them by referring to the index number.
fruits = ["apple", "banana", "mangoe"]
print(fruits[1])

# Negavtive Indexing which starts from right to left and the first value is -1.
certifications = [
    "CCNA",
    "CCNP",
    "CCIE",
    "AWS Networking",
]
print(certifications[-1])

# Accessing the range of values from the list. When specifying a range, the return value wull be a new list with specified items.
car_brands = ["Kia", "Hyundai", "BMW", "Audi", "Mercedez", "Ford", "Toyota"]
print(car_brands[2:6])

# Accessing the range of values using negative index numbers.
colors = ["red", "back", "orange", "yellow", "pink", "white"]
print(colors[-3:-1])

# Check if any item is present in list.
alphabets = ["a", "b", "c", "d", "e", "f"]
if "a" in alphabets:
    print("Yes, 'a' is in the alphabets list")

# To check the position of the specific value from the list.
elements = ["water", "fire", "air"]
find = elements.index("fire")
print(find)
