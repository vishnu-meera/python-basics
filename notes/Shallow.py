dic = {x : x**4  for x in range(10)}

dic1 = dic

print(dic1)
print(dic)

dic[10] = 10**4

print(dic1)
print(dic)

