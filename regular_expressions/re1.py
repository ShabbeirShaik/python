import re
s="abc123abc4567abc123ABC"
pattern=re.compile(r'abc')

matches=pattern.finditer(s)
#matches=re.finditer(r'abc',s)  ----->another method
#match=re.match(pattern,s)------------>only match object which searches its pattern at the starting of the string
for i in matches:
    print(i)
"""    
searchs=re.search(pattern,s)    
for i in searchs:   
    print(i)"""
