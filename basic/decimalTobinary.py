n=int(input())
def decimal_binary(n):
    print(bin(n).replace("0b",""))
    """if(n>1):
        decimal_binary(n//2)
    print(n%2,end=" ")    """
decimal_binary(n)    
