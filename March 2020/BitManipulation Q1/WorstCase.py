#1.Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). Return an array containing the result for the given queries.
#Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
#Output: [2,7,14,8] 

def solution(a,q,n):
	ans=[]
	#print(n)
	i=0
	while(i<n):
		j=q[i][0]
		x=a[j]
		while(j<q[i][1]):
			x=x^a[j+1]
			j+=1
		ans.append(x)
		i+=1		 
	return ans	
		
print("ENTER ARRAY")
a=list(map(int,input().split()))
print("ENTER NO OF QUERIES")
n=int(input())
q=[]
for i in range(n):
	li=int(input())
	ri=int(input())
	q.append([li,ri])
ans=solution(a,q,n)
print(ans)
