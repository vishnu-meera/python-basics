try:
	sum  = 0
	file = open('number.txt','r')
	for number in file:
		temp = int(number)
		if(temp != 0):
			sum = sum + 1/temp
			print (sum)

except ZeroDivisionError:
	print("One of the number in the file is zero")
except IOError:
	print('number.txt DNE')
except Exception as e:
	print(e)
finally:
	print(sum)