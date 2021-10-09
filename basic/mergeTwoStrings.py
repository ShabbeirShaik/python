n=input()
n1=input()
res=""
i=0
while (i<len(n)) or (i<len(n1)):
    if(i<len(n)):
        res+=n[i]
    if(i<len(n)):
        res+=n1[i]
    i+=1        

print(res)    