# To change the item value of a specific item, refer to the index number:
fruits = ["apple", "banana", "blackcurrant"]
fruits[2] = "mangoes"
print(fruits)

# Change a range of item values:
certifications = ["ccna", "ccnp", "dba", "sysadmin"]
certifications[2:4] = ["ccie", "aws networking"]
print(certifications)

# If you insert more items then you replace, the new items will be inserted where you specified , and the remaining items will be move accordingly:
car_brands = ["kia", "hyundai", "toyota"]
car_brands[1:2] = ["bmw", "audi"]
print(car_brands)

# Change the list range value by replacing it with one value:
colors = ["black", "red", "green", "orange", "yellow"]
colors[2:4] = ["brown"]
print(colors)