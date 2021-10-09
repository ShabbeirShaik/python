#ascii dotall ignorecase locale multiline verbose 
import re
s="hello World"
pattern=re.compile(r"world",re.I)
matches=pattern.finditer(s)
for match in matches:
    print(match)