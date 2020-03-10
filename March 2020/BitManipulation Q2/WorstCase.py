#2. Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
#Input: a = 2, b = 6, c = 5
#Output: 3

def solution(a, b, c):
    a=bin(a)[2:]
    b=bin(b)[2:]
    c=bin(c)[2:]
    m=max(len(a),len(b),len(c))
    a=a.zfill(m)
    b=b.zfill(m)
    c=c.zfill(m)
    print(a,b,c)
    i=0
    count=0
    while(i<m):
        if(c[i]=='0'):
            if(a[i]==b[i] and a[i]=='0'):
                pass
            elif(a[i]==b[i] and a[i]!='0'):
                count+=2
            elif(a[i]!=b[i]):
                count+=1
        else:
            if(a[i]==b[i] and a[i]=='0'):
                count+=1
            elif(a[i]==b[i] and a[i]=='1'):
                pass
            elif(a[i]!=b[i]):
                pass
        i+=1
    return count
a=int(input())
b=int(input())
c=int(input())
print(solution(a,b,c))