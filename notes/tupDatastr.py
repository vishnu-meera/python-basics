tup = (1,'abc',2,'cde')
tup1 = 3, 'efg', True
tup2 = 'A'

print(tup)
print(tup1[1])
print(tup2[0])
try:
	tup = tup[0:3] +  (5,)
except  Exception as e:
	print(e)

print(tup)
print(6 in tup)
print(tup * 3)
for x in tup:
	print (x)


def multi_result(a,b):
	return (a+b,a*b,a/b,a//b,a%b)

print(multi_result(4,2))
print(multi_result(6,3))

print(multi_result(4,2)[2:5]==multi_result(6,3)[2:5])

# tup functions
print('----------------------------------------------')
print(len(multi_result(4,2)))
print(max(multi_result(4,2)))
print(min(multi_result(4,2)))