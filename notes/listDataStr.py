list1 = [1,'abc',(2,3,'abc')]
print(list1)
print(type(list1))

print(type(list1[2]))

print(list1 * 2)

print(2 in list1)

list2 = [1,'abc',(2,3)]
print(list1==list2)

print(list1[:2])
print(list1[1:])
list1.append(6)
print(list1)
list1[len(list1):]=[7]
print(list1)

print(list(map(lambda x: x*x + 3*x + 3,[1,2,3,4,5,6,7,8,9])))

l=[]
for i in range(101):
	l.append(i)
print(l)