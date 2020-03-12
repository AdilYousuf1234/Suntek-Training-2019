#4.Given a positive integer n and you can do operations as follow:
#1.	If n is even, replace n with n/2.
#2.	If n is odd, you can replace n with either n + 1 or n - 1.
#What is the minimum number of replacements needed for n to become 1?

def Solution(n):
    count=0
    while(n>1):
        if(n&1==0):                     #If n is even then n=n/2
            n>>=1
            c+=1
            #print("Even",n)
        elif(n>>1 & 1==0 or n==3):      #If half of n is even or half of n is 1(i.e. n==3)
            n-=1
            c+=1
            #print("if",n)
        else:                           #If n is neither even nor half of n is even
            n+=1
            c+=1
            #print("else",n)
    return c
n=int(input())
print(Solution(n))
