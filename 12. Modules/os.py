# Getting the current working directory
import os

cwd = os.getcwd()

print(cwd)


# Changing the current working directory
import os

os.chdir("/path/to/new/directory")


# Creating a directory
import os

os.mkdir("new_directory")


# Removing a directory
import os

os.rmdir("new_directory")


# Checking if a file exists
import os

if os.path.exists("myfile.txt"):
    print("The file exists!")
else:
    print("The file does not exist.")


# Opening a file
import os

f = open("myfile.txt", "r")

contents = f.read() #read the contents of the file

f.close() #close the file


# Writing to a file
import os

f = open("myfile.txt", "w")

f.write("Hello, world!") #write to the file

f.close() #close the file


# Renaming a file
import os

os.rename("myfile.txt", "new_name.txt")


# Deleting a file
import os

os.remove("myfile.txt")


# Getting the size of a file
import os

size = os.path.getsize("myfile.txt")

print(size)


# Getting the modification time of a file
import os

mtime = os.path.getmtime("myfile.txt")

print(mtime)


# Listing the contents of a directory
import os

contents = os.listdir("/path/to/directory")

print(contents)
