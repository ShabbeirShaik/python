#n1=int(input())
n=list(map(int,input().split(" ")))
k=[]
for i in n:
    if i not in k:
        k.append(i)
print(k)        
