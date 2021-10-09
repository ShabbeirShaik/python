#group start end span
import re
s="123abc63763abc76473ABC"
pattern=re.compile(r'abc')
matches=pattern.finditer(s)
for match in matches:
    print(match.span())
    print(match.start())
    print(match.end())
    print(match.group())