import re

def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False

	if text[3] != '-':
		return False

	for i in range(4,7):
		if not text[i].isdecimal():
			return False

	if text[7] != '-':
		return False

	for i in range(8,12):
		if not text[i].isdecimal():
			return False

	return True

def findPhoneNumbers(message):
	pattern 		= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
	#mo	= re.search(pattern, message)
	#mo.group()
	return re.findall(pattern, message)

#print(isPhoneNumber('917432886'))

print(findPhoneNumbers('call me at 412-333-4444 or this number like 333-222-1111'))

batReg = re.compile(r'Bat(ma|mobile|copter|bat)')
mo = batReg.search('Batmobile lost a wheel')

print(mo.group())

mo = batReg.search('BatVishnu lost a wheel')

try:
	print(mo.group())
except Exception as e:
	print(e) #'NoneType' object has no attribute 'group'
'''
groups are created in the regex using parantheses
use \(and \) to literal parentheses in the regex string
the pipe | can match one of many possible groups
'''


