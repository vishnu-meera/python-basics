import re

string = 'Batwoman is a superheroine appearing in American comic books published by DC Comics. In all incarnations, the character is a wealthy heiress who becomes inspired by the superhero Batman and chooses, like him, to put her wealth and resources towards a war on crime as a masked vigilante in her home of Gotham City. The identity of Batwoman is shared by two heroines in mainstream DC publications; both women are named Katherine Kane, with the original Batwoman commonly referred to by her nickname Kathy and the modern incarnation going by the name Kate.'
batreg = re.compile(r'Bat(wo)?man') # 0 or 1 (wo)

mo = batreg.search(string)

#print(mo.group())
#print(batreg.findall(string))
phnreg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phnreg)

print(phnreg.findall('222-333-4444 444-444-4444 111-111-1111'))

#phoneReg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')


phoneReg = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

mo = phoneReg.search('My phone umber is 415-555-1234.Call me tomorrow.')
#print(mo.group())

mo=phoneReg.search('My phone number is 555-1234 without area code is 222')
#print(mo.group())

batreg = re.compile(r'Bat(wo)*man') # 0 or any 'wo' group with man
# escape * using /*

batreg = re.compile(r'Bat(wo)+man') # 1 or any 'wo' group with man
# so Batman wont match

regex = re.compile(r'\+\*\?')
#print(regex.search('i learned about +*? regex syntax'))
regex = re.compile(r'(\+\*\?)+')

#print(regex.search('i learned about +*?+*?+*?+*?+*?+*? regex syntax'))

# ? zero or one, * zero or more , + one or more
#{x} excat number of times

haRegex = re.compile(r'(Ha){3}')
#print(haRegex.search('he said HaHaHa'))

#{3,5} means 3 to 5
#{3,} means 3 to any number

digitRegex = re.compile(r'(\d{3,5})') # greedy
digitRegex = re.compile(r'(\d{3,5})') # nongreedy

#print(digitRegex.search('333444 555 888 12345 2222 666666'))
#print(digitRegex.findall('333 444 555 888 12345 2222 666666'))

'''
Character classes
\d -> any numeric digit 0 to 9
\D -> any character other than 0 to 9
\w -> lettter, number or _
\W -> not(lettter, number or _)
\s -> space or tab or newline
\S -> not (space or tab or newline)

'''
song  = '''On the first day of Christmas
my true love sent to me:
A Partridge in a Pear Tree

On the second day of Christmas
my true love sent to me:
2 Turtle Doves
and a Partridge in a Pear Tree

On the third day of Christmas
my true love sent to me:
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the fourth day of Christmas
my true love sent to me:
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the fifth day of Christmas
my true love sent to me:
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the sixth day of Christmas
my true love sent to me:
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the seventh day of Christmas
my true love sent to me:
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the eighth day of Christmas
my true love sent to me:
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the ninth day of Christmas
my true love sent to me:
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the tenth day of Christmas
my true love sent to me:
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the eleventh day of Christmas
my true love sent to me:
11 Pipers Piping
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the twelfth day of Christmas
my true love sent to me:
12 Drummers Drumming
11 Pipers Piping
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree'''

#xmas = re.compile(r'\d+\s\w+')
xmas = re.compile(r'\d+\s\w+\s\w+')
vowerl = re.compile(r'[^aeiouAEIOU]{3}') # a|e|i|o|u [a-zA-Z]
print(xmas.findall(song))

print(vowerl.findall(song))