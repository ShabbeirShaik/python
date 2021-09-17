book={}
book['patel']={'name':"patel",
'phone': "7654363883",
'address':"near bhavani puram vijayawada"}
book['sajid']={'name':"sajid",
'phone': "8762888292",
'address':"near labbipet,vijayawada"}
book['sai kumar']={'name':"sai kumar",
'phone': "846252562",
'address':"near sai baba temple machilipatnam"}
import json
s=json.dumps(book)
with open("c://data//book.txt","w") as f:
    f.write(s)
print(s)