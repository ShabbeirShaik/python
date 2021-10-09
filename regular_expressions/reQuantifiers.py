import re
s="iam shabbeir and my roll is 18481 _1234 _gdhsgdj_"
pattern=re.compile(r"\d{4,5}")       # * + {4} {4,5} ?
matches=pattern.finditer(s)
for match in matches:
    print(match)