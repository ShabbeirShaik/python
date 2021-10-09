a=input()
class solution():
    def goodOrbad(self,a):
        l=['a','e','i','o','u']
        c,v=0
        for i in range(len(a)):
            if(a[i] in l):
                c=0
                v+=1
                if(v>=5):
                    print("0")
                elif(a[i]=='?'):
                    c+=1
                    v+=1
                    if(c>3):
                        print("0")
                    if(v>5):
                        print("0")
                else:
                    v=0
                    c+=1
                    if c>3:
                        print("0")
        print("1")                               
