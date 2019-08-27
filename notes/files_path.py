import os
print(os.path.join('vishnu','sankar','meera'))

print(os.getcwd() + '\\files_path.py')
os.chdir('c:\\')

print(os.getcwd() + '\\files_path.py')

# absoulte file path start with the root folder
# relative file path starts with . or ..
'''
current working directory .\
one above ..\
'''
print(os.path.abspath('spam.png'))
os.chdir('c:\\users\\vsankar\\desktop\\PY')
print(os.path.abspath('spam.png'))
#os.path.isabs() returns true for absolute path
#os.path.relpath() gives relative file path
#os.path.basename and os.path.dirname

print(os.path.exists('c:\\windows\\system32\calc.exe'))
print(os.path.isfile('c:\\windows\\system32\calc.exe'))
print(os.path.isdir('c:\\windows\\system32\calc.exe'))
print(os.path.getsize('c:\\windows\\system32\calc.exe'))
#print(os.listdir('c:\\users\\vsankar\\desktop\\PY'))

totalsize = 0
for file in os.listdir('c:\\users\\vsankar\\desktop\\PY'):
	if not os.path.isfile(os.path.join('c:\\users\\vsankar\\desktop\\PY',file)):
		continue
	totalsize+=os.path.getsize(os.path.join('c:\\users\\vsankar\\desktop\\PY',file))

print(totalsize)
#os.makedirs()