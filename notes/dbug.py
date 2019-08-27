import traceback

try:
	def box(sympol,width,height):
		if(len(sympol) != 1):
			raise Exception('length of character should be 1')

		if(height < 2 or width < 2):
			raise Exception('height and width should be gretar than 2')
		
		print(sympol*width)

		for i in range(height-2):
			print(sympol + (' ' * (width-2)) + sympol)

		print(sympol*width)

	box('$', 30, 1)
except Exception as e:
	errorfile = open('ErrorLog.log','a')
	errorfile.write(traceback.format_exc())
	errorfile.close()
	print('traceback info was logged')


try:
	market_2nd = {'ns':'green','ew':'red'}
	

except Exception as e:

