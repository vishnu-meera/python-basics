class Student:
    def __init__(self, *args):
        self.name = args[0]
        self.school = args[1]
        self.marks = []

    def avg_marks(self):
        return sum(self.marks)/len(self.marks)

    @classmethod
    def friend(cls,origin,firend_name,*args):
        return cls(firend_name,origin.school,*args)


class WorkingStudent(Student):
    def __init__(self,*args):
        super().__init__(args[0],args[1])
        self.salary = args[2]

vishnu = WorkingStudent("Vishnu","IIT","$5000")
meera = WorkingStudent.friend(vishnu,"Meera","$7000")

# print(meera.name)
# print(meera.school)
# print(meera.salary)


# def asteric_args(*args):
#     print(sum(args))
#     print(args[0])

# asteric_args(1,2,3,4,5,6,7)

# *args
# **kwargs

my_list = [12,45,67,1023,12]
print(list(filter(lambda x:( x != 67 and x != 12), my_list)))
print((lambda x: x*3)(10))