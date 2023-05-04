# a tuple is a collection which is ordered and unchangeable.
# tuple items are ordered, unchangeable, and allow duplicate values.

my_tuple = ("apple", "banana", "cherry")
another_tuple = ("Tesla", "BMW", "Nissan")

#  tuple methods
print(len(my_tuple))  # count items in the tuple
print(my_tuple[1])  # get item by index position
print(my_tuple[-1])  # get last item
print("apple" in my_tuple)
print(my_tuple.count("apple"))
tuple_new = my_tuple + another_tuple

# loops through tuple
for item in my_tuple:
    print(item)
