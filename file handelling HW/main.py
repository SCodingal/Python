
file_read = open('Angola.txt','r')
print("File in Read mode")
print(file_read.read())
print(file_read.readlines())
file_read.close()


file_write = open('Angola.txt','w')
print("File in Write mode")
file_write.write("Angola is a beautiful country located in southen west africa")
file_write.close()


file_append = open('Angola.txt','a')
print("File in append mode")
file_append.write("Angolas naional animal is the palanca negra")
file_append.close()