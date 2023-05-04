# the key function for working with files in Python is the open() function.
# the open() function takes two parameters; filename, and mode.
# there are four different methods (modes) for opening a file:
import os

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# open file
f = open("../../demofile.txt")
print(f.read())  # read all file contents
print(f.readline())  # read one line
f.close()  # close file

# write to file
# to write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

f = open("../../demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open("../../demofile2.txt")
print(f.read())

# create a new file
# to create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

f = open("myfile.txt", "w")

# delete a file
os.remove("demofile.txt")

# delete a folder - folder has to be empty
os.rmdir("myfolder")

# check if file exist before deleting
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
