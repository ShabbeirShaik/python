n=int(input())
l1=[int(input()) for x in range(n)]
def selection_sort(l1):
    for i in range(len(l1)):
        min_number=min(l1[i:])
        min_number_index=l1.index(min_number,i)
        if(l1[i] != l1[min_number_index]):
            l1[i],l1[min_number_index] = l1[min_number_index],l1[i]
    print(l1)
selection_sort(l1)
            
