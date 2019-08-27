class Student(object):
	"""Student"""
	num_of_students = 0

	def __init__(self,name,index):
		self.name=name
		self.index=index
		Student.num_of_students +=1

	def __del__(self):
		Student.num_of_students -=1
try:
	s = Student('vishnu',1)
	y = Student('meera',2)

	print(Student)
	print(s)
	print(y)
	print(Student.num_of_students)
	del s

	print(Student)
	print(y)
	print(Student.num_of_students)
	print(s)

except Exception as e:
	print(e)