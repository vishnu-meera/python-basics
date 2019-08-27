my_set = set([1,2,3,4,5,6,6,6,1,2,3])
print(my_set)

my_set1 = set([5,6,7,8,4,1,2,8,9])
print(my_set1)

print(my_set | my_set1) # set.uninon()
print(my_set ^ my_set1) # set.difference
print(my_set - my_set1)
print(my_set1 - my_set)
print(my_set1 ^ my_set)
my_set.add(10)
print(my_set)