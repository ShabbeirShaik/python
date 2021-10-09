n=int(input())
class solution():
    global sum=0
    def armstrong(self,n):
        while(n!=0):
            temp=n%10
            n=n//10
            sum+=temp**3
        print(sum)
        if(sum==n):
            print("armstrong")
        else:
            print("not an armstrong")    
i1=solution()
i1.armstrong(n)            
     
