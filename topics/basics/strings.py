# string formatting
name = "Janelle Jones"
school = "Elementary High School"
print("{} works at {}".format(name, school))

# string methods
print(len(name))  # length on string
print(name.upper())  # uppercase
print(name.lower())  # lowercase
print(name.strip())  # remove white space before/after text
print(name.split(" "))  # splits text into a list
print(name.replace(" ", ","))  # replace a character with another character
print(name[2])  # print character at index position

# check if character/word in string
if "Jones" in name:
    print("Yes, 'Jones' is present")

# check if character/word not in string
if "Mark" not in name:
    print("Yes, 'Mark' is not present")

# loop through string
for letter in name:
    print(letter)
