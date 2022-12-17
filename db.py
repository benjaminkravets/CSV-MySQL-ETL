# import OS module
"""List directory items"""

import os
import string
# Get the list of all files and directories
path = "C://Users//bakra//Desktop"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files

#print(type(dir_list))
for x in dir_list:
    print(x + " " + str(hash(x)))