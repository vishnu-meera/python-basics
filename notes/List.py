li = ['cat','bat','mat','rate']
print(li[len(li)-1])
print(li[1:3])

spam= [10,20,30]
print(spam)
spam[1]="Hello"
print(spam)

print(spam[1:])
print(spam[:2])
print(len("heloo"))

del li[2]
print(li)

print(list("hel          lo"))

print(10 in spam)
print(20 not in spam)

print(list(range(10)))

supplies  = ['pens','pencil','books','pins']
for i in range(len(supplies)):
	print (supplies[i])

cat = ['fat','orange',5]
size,color,weight = cat
print(size,color,weight)

try:
	wish = ['hello','hi','howdy','heyas']
	print(wish.index('vishnu'))
except Exception as e:
	print(e)
	wish.append('vishnu')

print(wish)

#never do spand = spand.append()

#insert and append are list methods , never do it on other types
wish.remove('vishnu')
#remove will oly remove first value
#list.sort() will be sort
#list.sort(reverse=True) will sort in reverse
#list.sort different types
#list.sort(key=str.lower)
print(wish)