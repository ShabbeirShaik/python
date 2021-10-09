"""def polindrome(sum):
    temp=str(sum)
    if(temp==temp[::-1]):
        print("1")
    else:
        print("0")    """
n=int(input())
sum=0
for i in str(n):
    sum=sum+int(i)
print(sum)
#polindrome(sum)
sum=str(sum)
if(sum==sum[::-1]):
    print("1")
else:
    print("0")    