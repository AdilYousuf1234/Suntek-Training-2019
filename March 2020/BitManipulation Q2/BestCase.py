
#2. Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
#Input: a = 2, b = 6, c = 5
#Output: 3
def solution(a, b, c):
    count=0
    while(a>0 or b>0 or c>0):
        aa=a&1
        bb=b&1
        cc=c&1
        #print(aa,bb,cc,a,b,c)
        a=a>>1
        b=b>>1
        c=c>>1
        if(cc==0):
            if(aa==bb and aa==0):
                pass
            elif(aa==bb and aa!=0):
                count+=2
            elif(aa!=bb):
                count+=1
        else:
            if(aa==bb and aa==0):
                count+=1
            elif(aa==bb and aa==1):
                pass
            elif(aa!=bb):
                pass
    return count
a=int(input())
b=int(input())
c=int(input())
print(solution(a,b,c))
