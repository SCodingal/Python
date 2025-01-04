#open the file in read mode
file_read = open('Codingal.txt','r')
print("File in Read mode")
print(file_read.read())
print(file_read.readlines())
file_read.close()

#oppening the file in write mode
file_write = open('Codingal.txt','w')
print("File in Write mode")
file_write.write("I like to eat many different kinds of food/snacks that are really good, because who does not like foood?")
file_write.close()

#oppening the file in append mode
file_append = open('Codingal.txt','a')
print("File in append mode")
file_append.write("My teacher's favourite color is blue")
file_append.close()