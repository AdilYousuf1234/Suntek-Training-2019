#5.Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
#Example 1:
#Input: 2
#Output: [0,1,1]
n=int(input())
def Solution(n):
	ans=[]				#Array which contains the no of 1's in binary representation
	for i in range(n+1):		#Iterate from 0 to n
		s=bin(i)[2:]		#convert integer to binary representation
		ans.append(s.count('1'))#count 1's and add to the array
	return ans
print(Solution(n))
