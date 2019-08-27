import os
#hellofile = open(os.path.join(os.getcwd()+'\\file.txt'))
hellofile = open(os.path.join(os.getcwd()+'\\file2.txt'),'a') # w for write only mode
#content = hellofile.read()
#content = hellofile.readlines()
hellofile.write('which is always equal to the length of the string')
hellofile.write('which is always equal to the length of the string')
hellofile.write('which is always equal to the length of the string')
hellofile.write('which is always equal to the length of the string')
hellofile.close()
#print(content)

import shelve

tickets = shelve .open('importantTickets')
tickets.close()