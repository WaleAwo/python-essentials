# store multiple items in a single variable
# items are ordered, changeable, and allow duplicate values

# create a list
fruits = ["banana", "pear", "cherry", "apple"]
years = [3, "1988", 2.5, 987, "1993"]

# list methods
fruits.append("peaches")  # add item
fruits.insert(1, "oranges")  # add item by index
fruits.extend(years)  # add another list
fruits[1] = "blackcurrant"  # change item
fruits.remove("pear")  # remove item by name
fruits.pop(0)  # remove item by index
fruits.pop(-1)  # remove last item
fruits.clear()  # empty list
fruits.sort()  # sorts items
fruits.sort(reverse=True)  # reverse sort
fruits.reverse()  # reverse the order
print(len(fruits))  # count items in the list
print(fruits[1])  # get item by index position
print(fruits[-1])  # get last item
print("apple" in fruits)  # check if an item exists
print(fruits.count("apple"))  # count the number of an item in a list
print(fruits.index("apple"))  # show index position of item in a list

# loops through list
# option 1
for fruit in fruits:
    print(fruit)

# option 2 - list comprehension
[print(fruit) for fruit in fruits]

fruits.clear()  # clear a list
del fruits[1]  # remove item
del fruits  # delete a list
