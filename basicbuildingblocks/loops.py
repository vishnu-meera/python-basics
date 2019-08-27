my_variable = "hello"
for x in my_variable: # iterables strings, lists, tuples,sets and few more
    print(x)

print("###########")

my_variable2 = [1,3,5,7,9]
count = 0
while count < len(my_variable2):
    print(my_variable2[count] ** 9999)
    count+=1


should_continue = True
if should_continue:
    print("Hello")

# in ==> if something in lists:
# not in ==> if something not in lists:
# pass ==> means do nothing