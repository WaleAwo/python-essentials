# dictionaries are used to store data values in key:value pairs.
# dictionary items are ordered, changeable, and does not allow duplicates (cannot have two items with the same key)

# create a dictionary
stuff = {
    "food": 15,
    "energy": 100,
    "enemies": 3
}

new_items = {
    "rocks": 4,
    "arrows": 18
}

# dictionary methods
stuff.update(new_items)  # combines dictionaries
print(stuff["food"])  # get item from key value
print(stuff.get("energy"))  # get item from key value
print(stuff.items())  # view all item keys and values
print(stuff.keys())  # get a list of keys
print(stuff.values())  # get a list of values
print(stuff.pop("food"))  # removes the key and value
print(stuff.popitem())  # remove the last item
print(stuff.update(food=522))  # updates a value
print(stuff.setdefault("energy"))  # see the default value of a key
print(stuff.setdefault("car", 12))  # adds a key/value pair
print(len(stuff))  # count items in the dictionaries

# check if a key exist in a dictionary
if "food" in stuff:
    print("Yes, 'food' is one of the keys in the 'stuff' dictionary")

# loop through the keys in a dictionary
# option 1
for item in stuff:
    print(item)

# option 2
for item in stuff.keys():
    print(item)

# loop through the values in a dictionary
# option 1
for item in stuff:
    print(stuff[item])

# option 2
for item in stuff.values():
    print(item)

# loop through keys and values in a dictionary
for key, value in stuff.items():
    print(key, value)
