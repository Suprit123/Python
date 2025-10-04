# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.

# In Python a function is defined using the def keyword:


def my_function():
    print("Hello from a function")


my_function()

# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name


def my_function(surname):
    print(f"{surname} Chinchodikar")


my_function("Suprit")
my_function("Whiskey")

# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.


def my_car_function(model, brand):
    print(f"{model}, {brand}")


my_car_function("X-Line", "kia")


# The following example shows how to use a default parameter value.

# If we call the function without argument, it uses the default value:


def my_country(country="India"):
    print(f"I am from {country}")


my_country("Sweden")
my_country()
my_country("Singapore")

# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.


def my_fruits(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_fruits(fruits)
