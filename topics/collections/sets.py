#  set items are unordered, unchangeable, and do not allow duplicate values.

fruits = {"apple", "banana", "cherry"}
another_set = {"blueberry", "tomato"}

#  set methods
fruits.add("pear")  # add item to set
fruits.update(another_set)  # add items from another set
fruits.remove("banana")  # remove item from set
fruits.discard("banana")  # remove item from set
fruits.clear()  # clears all items from a set
print(len(fruits))  # count items in the list
print("banana" in fruits)  # check if an item exists

# loops through set
for fruit in fruits:
    print(fruit)

del fruits  # deletes a set
