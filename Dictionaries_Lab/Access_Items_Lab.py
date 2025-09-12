my_car = {
    "brand": "kia",
    "model": "Seltos 1.5",
    "Fuel": "Petrol",
    "purchased_year": "2023",
    "color": "matt finish grey",
    "seller": "Crystal Kia",
}

# We can access the items of a dictionary be refering to it's key name, inside the squre bracket
brand = my_car["brand"]
print(brand)

# There is also a method called get() which will give the same result.
brand = my_car.get("brand")
print(brand)

# The keys() method will return a list of all the keys in the dictionary.
keys = my_car.keys()
print(keys)

# The values() method will return a list of all the values in the dictionary.
values = my_car.values()
print(values)

# The items() method will return each item in a dictionary, as tuples in a list.
items = my_car.items()
print(items)

# To determine if a specified key is present in a dictionary use the in keyword:
if "model" in my_car:
    print("Yes, 'model' is one of the key in the my_car dictionary")

for key, value in my_car.items():
    print(f" key: {key}: {value}")
