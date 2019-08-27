
try:
	a = 5/0
	print("after")
except Exception as e:
	print(e)

try:
	n=int(input("enter a number\n"))
	n=n*10
	print(n)
except ValueError:
	print("Please enter integer")