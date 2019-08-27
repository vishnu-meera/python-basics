
try:
	file = open("C:\\Users\\vsankar\\Desktop\\good.xml",'r')
	print(file.read(10))
	print(file.tell())
	file.seek(40)
	print(file.read(10))
	print(file.tell())
	for line in file:
		print(line)
	print(file.name)
	print(file.mode)
	print(str(file.closed))
	file.close()
except Exception as e:
	print(e)