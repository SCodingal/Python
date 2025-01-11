file1=open("School.txt","r")
#print(file1.read()) # reads all the lines line
print(file1.read(5)) #  takes the letters of the first word in your file with the number you've put in
print(file1.readlines()) # reads all the lines in a list and separates them with commas
print(file1.readline()) #reads only one line
file1.close()

