def function1():
	print("my first function")

function1()

def returnFunction():
	return "i am result"

result = returnFunction()
print(result)

def multi(a=9,b=2):
	return a+b,a-b,a/b,a//b,a*b,a%b

result2 = multi(10)
print(result2)
print(type(result2))