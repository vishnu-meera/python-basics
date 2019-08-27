def BinarySearch(seq,number):
	low=0
	high=len(seq)-1
	step=0

	while low<=high:
		mid=int((low+high)/2)
		guess = seq[mid]
		#print(low,high,mid,guess)
		step+=1
		if guess==number:
			return(guess,step)
		elif guess<number:
			low=mid+1
		else:
			high=mid-1

arr=[]
for i in range(100000):
	arr.append(i*2)

print(BinarySearch(arr,4112))


def BinarySearchRe(low,high,number,step):
	mid 	= int((low+high)/2)
	guess	= arr[mid]
	#print(low,high,mid,guess)
	if(guess == number):
		return(guess,step)
	else:
		if guess<number:
			low=mid+1
		else:
			high=mid-1
		step +=1
		return BinarySearchRe(low,high,number,step)

print(BinarySearchRe(0,len(arr),4112,0))