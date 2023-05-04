# for loop

fruits = ["apple", "orange", "pear"]
for fruit in fruits:
    print("Would you like an {}.".format(fruit))

# while loop

temp = 37
while temp > 32:
    print("{}: The water is not frozen".format(temp))
    temp -= 1
print("Water becomes ice at 32 degrees Fahrenheit")

# Loop controls
# Break - end the loop and go to the next statement in the program (outside the loop)
# Continue - skips current part of the loop and moves to the next part of the loop
# Pass - skips any part of the loop where "pass" appears. best used for testing

sweets = 15
while sweets > 10:
    print("{}: You have too many sweets".format(sweets))
    sweets -= 1
    if sweets == 13:
        break

for number in range(1, 11):
    if number == 7:
        print("Skipping number 7.")  # execute specific command
        continue
    print("This is number {}.".format(number))

for number in range(1, 11):
    if number == 3:
        pass  # skips
    else:
        print("The number is {}.".format(number))
