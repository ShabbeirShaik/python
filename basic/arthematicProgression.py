a1=int(input())
a2=int(input())
n=int(input())
n1=int(input())
class solution:
    def mathTable(self,a1,a2,n,n1):
            l=[]
            l.append(a1)
            l.append(a2)
            for i in range(0,n1):
                diff=l[i+1]-l[i]
                k=l[i+1]+diff
                l.append(k)
            print(l)    
            print(l[n])    
b1=solution()
b1.mathTable(a1,a2,n,n1)
                