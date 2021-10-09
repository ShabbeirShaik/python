n=int(input())
temp=n
#remainder=int(input())
def factorial(remainder):
    fact=1
    for i in range(remainder,1,-1):
        fact=fact*(i)
        #remainder=remainder-1
        #print(i)
    return fact 
#factorial(remainder)    
def strong(n):
    result=0 
    while(n!=0):
        remainder=n%10
        #remainder=remainder+1
        result+=factorial(remainder)  
        n=n//10 
    print(result)
    if(result==temp):
        print("strong")  
    else:
        print("not strong")  
strong(n) 


