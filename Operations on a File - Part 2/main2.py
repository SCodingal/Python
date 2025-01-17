new_file = open('d.txt','x')
new_file.close

import os
print("Checking if my_file exists or not......")
if os.path.exists("d.txt"):
    print("file found")

else:
    print("The file does not exist")

os.remove("g1.txt")

os.rmdir('sample')