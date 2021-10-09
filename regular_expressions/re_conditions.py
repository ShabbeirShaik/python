import re
s="""
1234
iam shabbeir
mr. shabbeir
mrs. patel
mr saikumar
mr dp
ms. fathima
shabbeir654@gmail.com
saikumar345@yahoo.org
patel-321@bingo.mail
"""
#pattern=re.compile(r"(mr|mrs|ms)\.?\s\w+")
pattern=re.compile(r"([a-zA-z0-9-]+)@([a-zA-z]+)\.([a-zA-z]+)")

matches=pattern.finditer(s)
for match in matches:
    #print(match)
    #print(match.group())
    print(match.group(0))
    print("___________________")
    #print(match.group(2))
    print(match.group(1))