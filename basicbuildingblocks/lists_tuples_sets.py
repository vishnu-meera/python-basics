list_one = [80,90,89,89,90]
list_tuple = (80,90,89,89,90)
list_set = {80,90,89,89,90}
sum = 0
for grade in list_one:
    sum+=grade

avgGrade = sum/len(list_one)

print(sum, avgGrade)
print(list_one)
print(list_tuple)
print(list_set)

list_one.append(100)

print(list_one)

#some more advanced 
# set methods
#intersection == intersection of set
#union == union of set
#difference == diff of set