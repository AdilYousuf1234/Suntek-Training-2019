#1.Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). Return an array containing the result for the given queries.
#Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
#Output: [2,7,14,8] 

def solution(a,q,n):
	xor=[a[0]]
	for i in range(1,len(a)):
		xor.append(xor[i-1]^a[i])
	#print(xor)
	ans=[]
	for i in range(n):
		end=q[i][1]
		start=q[i][0]
		if(start!=0):
			ans.append(xor[end]^xor[start-1])
		else:
			ans.append(xor[end])
	#print(an)
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