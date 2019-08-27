myList = [x*2 for x in range(100)]
multiply_by_10 = [(x+1) * 10 for x in range(10)]
print(multiply_by_10)

print([n for n in range(101) if n%3 == 0])

persons = ["Vishnu ", " AYaaN" , "MEERA", " Prasanna"];
print([person.strip().lower() for person in persons])