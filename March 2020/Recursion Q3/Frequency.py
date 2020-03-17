#3.	Given an integer array and an integer K.  Write a method return the frequency of K
#Arr : -1 5 5 4 3 -1 -1 
#K: -1
#o/p: 3
def Solution(a,k):
    if(len(a)==0):
        return
    if(a[0]==k):    #if first element is key increment count
       global count
       count+=1
    Solution(a,k)   #Use recursion to search the remaining elements
count=0    
l=list(map(int,input().split()))
k=int(input())
Solution(l,k)
print(count)
