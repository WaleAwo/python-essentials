# the 'try' block lets you test a block of code for errors.
# the 'except' block lets you handle the error.
# the 'else' block lets you execute code when there is no error.
# the 'finally' block lets you execute code, regardless of the result of the try- and except blocks.

# simple try
try:
    print(x)
except:
    print("An exception occurred")

# try...else
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# try...finally
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# raise an exception
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")
