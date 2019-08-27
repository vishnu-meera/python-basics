def paliandrome(string):
	newtstring = []
	for i in range(len(string)-1,-1,-1):
		newtstring.append(string[i])
	if ''.join(newtstring)==string:
		print(string + ' is paliandrome')
	else:
		print(string + ' is not paliandrome')

#paliandrome('malayalam')
#paliandrome('vishnu')
#paliandrome('meera')

def newpaliandrome(string):
	for i in range(0,len(string)-1):
		if (string[i].lower() != string[len(string)-1-i].lower()) :
			print(string + ' is not paliandrome')
			return
	print(string + ' is paliandrome')

#newpaliandrome('vishnu')
#newpaliandrome('Saippuakivikauppias')
#newpaliandrome('tattarrattat')

def palianRecur(string,start,end):
	print(palianRecur)
	if(end==-1):
		print(string + ' is paliandrome')
		return
	else:
		if(string[start].lower() != string[end].lower()):
			print(string + ' is not paliandrome')
			return
		else:
			palianRecur(string, start+1, end-1)

palianRecur('malayalam', 0, len('malayalam')-1)
#palianRecur('vishnu', 0, len('vishnu')-1)