import re
dates="""
24-06-2003
24-07-2003
24-08-2003
24-09-2003


21/08/2005
21/09/2005
21/10/2005
21/11/2005

2002/07/29
2002/08/29
2002/03/29


23.04.2004

"""
pattern=re.compile(r'\d{2}[-/]0[6789][-/]\d{4}')
matches=pattern.finditer(dates)
for match in matches:
    print(match)
