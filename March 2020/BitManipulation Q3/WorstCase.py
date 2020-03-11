#3.Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
#Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
#Could you do this in O(n) runtime?
#Example:
#Input: [3, 10, 5, 25, 2, 8]
#Output:28
def solution(a):
    m=0
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            x=a[i]^a[j]
            if(x>m):
                m=x
            
    return m
l=list(map(int,input().split()))
print(solution(l))