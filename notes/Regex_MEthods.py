import re

namesReg = re.compile(r'Agent \w+')
print(namesReg.findall('Agent Alice gave the secret documnets to Agent Bob.'))

print(namesReg.sub('***','Agent Alice gave the secret documnets to Agent Bob.'))

# re.IGNORECASE | re.DOTALL | re.VERBOSE
# re.sub() do the substitution

# re.VERBOSE les you add whitespace