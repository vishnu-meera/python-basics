string = "String traversal!"
x=""
for i in range(len(string)-1,-1,-1):
	x = x + string[i]
print(x)

for i in range(2):
	for j in range(2):
		print(str(i) + " " + str(j))
