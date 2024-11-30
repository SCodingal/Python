lst = [1,3,5,7]

print("lenght of list:",len(lst))
print("firts element:", lst[0])
print("last element:", lst[-1])

lst.append(1)
print("updated list:", lst)

lst.remove(7)
print("updated list:", lst)

lst.sort()
print("updated list:", lst)

lst.reverse()
print("updated list:", lst)

print(lst[1:3])

