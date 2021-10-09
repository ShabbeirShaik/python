n=int(input())
l1=[int(input()) for x in range(n)]
class solution():
    def insertion_sort(self,l1):
        for i in range(len(l1)):
            key=l1[i]
            j=i-1
            while j>=0 and key<l1[j]:
                l1[j+1]=l1[j]
                j-=1
            l1[j+1]=key
        print(l1)
s1=solution()
s1.insertion_sort(l1)                
