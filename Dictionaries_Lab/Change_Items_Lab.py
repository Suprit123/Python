my_car = {
    "brand": "kia",
    "model": "Seltos 1.5",
    "Fuel": "Petrol",
    "purchased_year": "1990",
    "color": "matt finish grey",
    "seller": "Crystal Kia",
}

# You can change the value of a specific item by referring to it's key name.
my_car["purchased_year"] = 2023
print(my_car)
# The update() method will update the dictionary with the items from the given argument.
# Please note that the argument must be a dictionary.
my_car.update(({"purchased_year": 2024}))
print(my_car)
