my_car = {
    "brand": "kia",
    "model": "Seltos",
    "Fuel": "Petrol",
    "purchased_year": "2023",
    "seller": "Crystal Kia",
}

# The pop() method removes the item with the specified key name:
my_car.pop("model")
print(my_car)

# The popitem() method removes the last inserted item.
my_car.popitem()
print(my_car)

# The del keyword removes the item with the specified key name:
del my_car["Fuel"]
print(my_car)

# The del keyword can also delete the disctionary completely. You will get error here because "my_car" no longer exists.
del my_car
print(my_car)

# The clear() method empties the dictionary.
my_car.clear()
print(my_car)
