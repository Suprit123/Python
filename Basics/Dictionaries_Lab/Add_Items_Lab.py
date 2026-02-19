my_car = {
    "brand": "kia",
    "model": "Seltos",
    "Fuel": "Petrol",
    "purchased_year": "2023",
    "seller": "Crystal Kia",
}

# Adding and item to the dictionary is done by using a new index key and assigning a value to it.
my_car["engine"] = 1.5
print(my_car)

# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
my_car.update({"engine": 1.5, "color": "matt grey", "seating_capacity": 4})
print(my_car)
