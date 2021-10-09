import string  
n=int(input())  
l= [x for x in range(1,26)]
k=[]
for i in string.ascii_lowercase:
    k.append(i)
Alpha_dict=dict(zip(l,k))     
k=str(n)
final_str=""
while(n!=0):
    rem=n%10
    final_str+=Alpha_dict[rem]
    n=n//10
print(final_str[::-1]) 

