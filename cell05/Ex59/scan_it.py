import re

text = input('Put word here: ')
patt = input('Search: ')

pattern = rf'\b{re.escape(patt)}\b'
res = re.findall(pattern, text, re.IGNORECASE)

if len(res) > 0:
    print(len(res)) 
else:
    print('None') 
