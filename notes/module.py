import primeModule as pr

#from primeModule import First_N_Prime
#print(dir(pr))

#print(pr.__file__)
#print(pr.__spec__)
#print(pr.__name__)
#print(pr.__loader__)
#rint(pr.__doc__)
#print(pr.__cached__)
#print(pr.__builtins__)

#builtInModule

import copy
import math
import cmath

my_dic = {x : x**3  for x in range(10)}
my_dic2 = copy.deepcopy(my_dic)

#print(my_dic)
#print(my_dic2)

my_dic[10] = 10**3

#print(my_dic)
#print(my_dic2)

#print(dir(copy))
#print(dir(math))
#print(cmath.sqrt(4))

#print(math.log(128))
import sys

print(dir(sys))
print(sys.version)