ham = {'age':8, 'species':'cat', 'name':'Zophie'}
egs = {'name':'Zophie','species':'cat','age':8}

print(ham==egs)

print('name' in egs)
print('name' not in egs)

print(list(egs.keys()))
print(list(egs.values()))
print(list(egs.items()))

for k in egs.keys():
	print(k,egs[k])

print('vishnu' in ham)

print(egs.get('color','yellow'))
print(egs.get('age',0))

print(egs.setdefault('color','yellow'))
print(egs.setdefault('age',0))

print(list(egs.items()))
