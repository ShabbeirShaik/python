n=int(input())
def fiband(n):
    if(n==2):
        return 1
    elif(n==1):
        return 0
    else:
        return fiband(n-1)+fiband(n-2)        
print(fiband(n))