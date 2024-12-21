#list
list1=[0.9,0,3,9]

print(list1)

list1.append(4)
print(list1)
print(list1[3])
list1.remove(0.9)
print(list1)

#tuple

t1=(1,3,3,4,7,99,999)
print(t1)
t2=("hello",)
t3=t1+t2
print(t3)

print(tuple(list1))
print(list(t1))

#set

set1={8,4,3,10,8,4,3,10}
print(set1)

#dictionary

dic1={"name":"Tchiyna","grade":7}
print(dic1)

print("my grade is ",dic1["grade"])
dic1["age"]=13
print(dic1)