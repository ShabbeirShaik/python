array_range=int(input()) #range of the array
search_element=int(input()) #element that needs to be searched
array=[int(input()) for x in range(array_range)]
def linear_search(array,search_element,array_range):
    for i in range(0,array_range):
        if(array[i]==search_element):
            return i   
    return -1
result=linear_search(array,search_element,array_range)                  
if(result==-1):
    print("given number is not present in the array")  
else:
    print("Element found at index:",result)    