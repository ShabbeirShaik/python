def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)
def lcm(a,b):
    print((a/(gcd(a,b))*b))
lcm(65,15)