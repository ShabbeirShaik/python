import re
s="iam shabbeir 1234 AHAM"
pattern=re.compile(r"[A-Za-z0-9]")
matches=pattern.finditer(s)
for match in matches:
    print(match)