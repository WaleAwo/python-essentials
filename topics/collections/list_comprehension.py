# create a new list based on the values of an existing list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [fruit for fruit in fruits if "a" in fruit]  # return fruits containing the letter 'a'

print(new_list)
