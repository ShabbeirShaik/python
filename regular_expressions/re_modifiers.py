import re
#methods:-->split() sub()
 
"""                                                                                     
s="1234abc87673abc87686786ABCsdjhjabc"
pattern =re.compile(r"abc")
#splitted_list=pattern.split(s)
#print(splitted_list)
subb=pattern.sub("hello",s)
print(subb)
"""
urls="""
https://www.google.com
http://amazon.com
udp://flipkart.com
"""
pattern=re.compile(r"([a-zA-z0-9://]+)(www\.)?\.?([a-zA-z0-9]+)\.([a-zA-z0-9]+)")
matches=pattern.finditer(urls)
for match in matches:
    print(match) 