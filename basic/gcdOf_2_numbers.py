a=int(input())
b=int(input())
def gcd_of_two(a,b):
    if(a==0):
        #return b
        print(b)
    elif(b==0):
        #return a
        print(a)
    elif(a==b):
        #return a
        print(a)
    elif(a>b):
        return gcd_of_two(a-b,b)     
    else:
        return gcd_of_two(a,b-a)           
gcd_of_two(a,b)        