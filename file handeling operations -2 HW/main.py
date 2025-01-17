new_file = open('l.txt','x')
new_file.close

import os
print("Checking if my_file exists or not......")
if os.path.exists("l.txt"):
    print("file found")

else:
    print("The file does not exist")

os.remove("l.txt")

