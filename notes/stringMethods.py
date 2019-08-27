spam = "vishnu Sankar!!!"

print(spam.upper())
print(spam.lower())

spam = spam.upper()
print(spam)

spam = 'Vishnu Sankar'
print(spam.islower())
print(spam.upper().isupper())

print(spam.isalnum())
print(spam.isalpha())

print('12345'.isdecimal())

print(' '.isspace())
print(spam.isspace())
print(spam.istitle())

print('vishnu sankar'.startswith('vish'))
print('vishnu sankar'.endswith('kar'))

animals = ['cat','dog','monkey','elephant']

print(''.join(animals))
print(','.join(animals))
print('\n'.join(animals))

m = "My mother might make monday melodious"

print(m.split(' '))
print(m.split('m'))
#rjust, ljust,center
spam = 'Vishnu'.rjust(40)
print(spam)
print(spam.strip().strip('V').replace('u','xyz'))




