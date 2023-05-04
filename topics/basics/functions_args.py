# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.


def user_info(name, age, city):  # positional
    print("{} is {} years old and lives in {}.".format(name, age, city))


def car_info(brand, model, year=2023):  # default value
    print("I have a {} model {}, with {} a plate.".format(brand, model, year))


def add(*args):  # unknown number of arguments
    print(sum(args))


def application(**kwargs):  # self-defined parameters
    print(**kwargs)


def multiply(x):
    return 5 * x


total = multiply(5)
print(total)
user_info("John", 12, "London")
car_info("Tesla", "S")
add(2, 5, 17)
application(colour="brown", number=23, item="train")
