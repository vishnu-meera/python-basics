try:
	file = open('file.txt','w+')
	file.seek(0)
	for i in range(0,1000000,1):
		file.write("Son nom est meera " + str(i) + "\n")
	file.seek(0)
	print(file.read())
	file.close()
except Exception as e:
	print(e)