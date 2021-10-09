n=int(input())
l1=[int(input()) for x in range(n)]
def bubble_sort(l1):
    for i in range(0,len(l1)-1):
        for j in range(len(l1)-1):
            if(l1[j]>l1[j+1]):
                temp=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=temp
    print(l1)
bubble_sort(l1)    