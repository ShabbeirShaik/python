from lcmOf2numbers import lcm   #import the lcm function from lcmOf2numbers file 
#n=int(input())
num1=int(input())
den1=int(input())
num2=int(input())
den2=int(input())
def addFraction(num1,den1,num2,den2):
    result=int((num1*(lcm(den1,den2)/den1))+int((num2*(lcm(den1,den2)/den2))))
    return result/lcm(den1,den2)
addFraction(num1,den1,num2,den2)

