#Basic Star Patter
print("Star pattern /n")
for i in range(1,6):
  for j in range(i):
    print("*", end=" ")
  print()

print("Star pattern /n")
for i in range(6,0,-1):#for row
  for j in range(i):
    print("*", end=" ")
  print()

print("Number /n")
for i in range(1,6):#for row
  for j in range(i):
    print(i, end=" ")
  print()
  
  

