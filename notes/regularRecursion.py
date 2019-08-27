def factorial(n):
	#print(factorial)
	print(n)
	if(n==1):
		return 1
	else:
		return n * factorial(n-1);

def tail_factorial(n, accumalator=1):
	if(n==1):
		return accumalator
	else:
		return tail_factorial(n-1,accumalator*n)

print(factorial(5))

#print(tail_factorial(5))

#f = lambda x,y : x+y

#print(f(2,3));

#f = lambda a: lambda b : lambda c : a* b* c

#print(f(5)(3)(2))
