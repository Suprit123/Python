# Dictionaries are used to store data values in key:value pairs.
my_car = {
    "brand": "kia",
    "model": "Seltos 1.5",
    "Fuel": "Petrol",
    "purchased_year": "2023",
    "color": "matt finish grey",
}
print(my_car)

# Since dictionary items are presented in key:value pairs, it can be refered using the key name.
print(my_car["brand"])

# We can also check the dictionary type by using type() method.
print(type(my_car))

# We can used the dict() method as well to create a dictionaary.
my_car = dict(brand="Kia", Model="Seltos 1.5", Fuel="Petrol")
print(my_car)
