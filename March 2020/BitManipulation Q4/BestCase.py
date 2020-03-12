#4.Given a positive integer n and you can do operations as follow:
#1.	If n is even, replace n with n/2.
#2.	If n is odd, you can replace n with either n + 1 or n - 1.
#What is the minimum number of replacements needed for n to become 1?

def Solution(n):
    c=0
    while(n>1):
        if(n&1==0):
            n>>=1
            c+=1
            print("Even",n)
        elif(n>>1 & 1==0 or n==3):
            n-=1
            c+=1
            print("if",n)
        else:
            n+=1
            c+=1
            print("else",n)
    return c
n=int(input())
print(Solution(n))