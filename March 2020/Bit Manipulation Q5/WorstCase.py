#5.Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
#Example 1:
#Input: 2
#Output: [0,1,1]
n=int(input())
def Solution(n):
	ans=[]
	for i in range(n+1):
		s=bin(i)[2:]
		ans.append(s.count('1'))
	return ans
print(Solution(n))