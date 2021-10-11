array_range=int(input())
search_element=int(input())
array=[int(input()) for i in range(array_range)]
low=0
high=len(array)
def binary_search(array,high,low,search_element):
    if high>=low:
        mid=(low+high)//2
        if array[mid]==search_element:
            return mid
        elif array[mid]>search_element:
            return binary_search(array,mid-1,low,search_element)
        elif array[mid]<search_element:
            return binary_search(array,high,mid+1,search_element)
    else:
        return -1
result = binary_search(array,high,low,search_element)
if(result==-1):
    print("Element not found in the array")
else:
    print("element found in the array at:",result)                                