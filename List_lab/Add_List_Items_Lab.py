# To add item to the end of the list, use the append() method:
fruits = ["apple", "bnana", "mangoes"]
fruits.append("strawberry")
print(fruits)

# To insert a list item at a specified index, use the insert() method.
car_brands = ['kia', 'hyundai', 'ford', "toyota"]
car_brands.insert(3, "bmw")
print(car_brands)

#to append elements from another list to the current list, use the extend() method.
courses = ["networking", "cloud"]
certifications = ["devnet", "azure", "aws"]
courses.extend(certifications)
print(courses)