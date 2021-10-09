n=int(input())
def primeNum(n):
    count=0
    for i in range(1,100):
        if(n%i==0):
            count+=1
    if(count>2):
        print("composite number")
    else:
        print("prime number")
primeNum(n)        

