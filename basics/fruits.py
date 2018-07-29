def readAndPrintfile(filename):
    myfile = open(filename)
    content = myfile.readline()
    while content !='':
        #print(content.split()[0])
        print(content.rstrip('\n'))
        content = myfile.readline()
    myfile.close()
        
def readShortFile(filename):
    myfile = open(filename)
    content = myfile.read().splitlines()
    for fruit in content:
        #print(content.split()[0])
        print(fruit)
    myfile.close()

def readPrint(filename):
    myfile = open(filename,"r")
    content = myfile.read()
    print(content)   
    myfile.close()
    
def printLengthOfFruits(filename):
    myfile = open(filename)
    content = myfile.read().splitlines()
    myfile.close()
    for fruit in content:
        #print(content.split()[0])
        print(len((fruit)))

def printLengthOfFruitsOtherWay(filename):
    myfile = open(filename)
    content = myfile.readlines()
    content = [line.strip() for line in content]
    myfile.close()
    for fruit in content:
        #print(content.split()[0])
        print(len((fruit)))
        
printLengthOfFruitsOtherWay("fruits.txt")