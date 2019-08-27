x = [5,2,4,6,1,3]

for i in x:
	if(x[i] > x[i+1]):
		temp = x[i]
		x[i] = x[i+1]
		x[i+1] =temp
		
	print (x[i]) 
