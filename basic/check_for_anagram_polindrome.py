n=input()
result=sorted(n)
if(sorted(n)==result):
    if(n==n[::-1]):
        print("Anagram polindrome detected")
    else:
        print("It is a anagram but not a polindrome ")    
else:
    print("It is neither polindrome nor a anagram")        