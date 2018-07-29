def readFile():
    temp = open("sample.txt")
    numbers = temp.read()
    print(numbers)
    numbers = numbers.splitlines()
    temp.close()
    print("****************")
    print(numbers)
    number = int(input("Enter a number: "))
    if number in numbers:
        print("number found")
    else:
        print("number not found")
    
readFile()