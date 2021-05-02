'''
Problem statement: An integer number and an array of postive numbers is given.
We need to find out if the integer number can be formed by adding any combination of the given
numbers in the array.

The numbers can be used any number of times.
'''

'''
Dynamic Programming or Memoized approach

We maintain a dictionary with key as any of the different m values and store True/False in it so that
it can be reused.
'''

#Recursive approach

def canSum(m,arr, memo={}):

	if m in memo.keys():
		# print("Found %s" % (memo[m]))
		return memo[m]
	#base case
	if m==0:
		memo[m] = True
		return True
	if m<0:
		# print("Returning False after breaching 0")
		memo[m] = False
		return False
	#recursive case
	for num in arr:
		remainder = m - num
		#return true if we find at least one combination of numbers that adds up
		if canSum(remainder, arr, memo):
			memo[m] = True
			return True

	#false case
	memo[m] = False
	# print("Returning False")
	return False #Return False if no combination of numbers could return True



print(canSum(7, [5, 3, 4, 7], memo={}))
print(canSum(7, [2, 4], memo={}))
print(canSum(7, [2, 3], memo={}))
print(canSum(8, [2, 3, 5], memo={}))
print(canSum(300, [7, 14], memo={}))

'''
Time Complexity

1. Each root node will branch out to n nodes. 
2. Each of these n nodes will further brach out to n nodes.
3. The height of the tree wll be m, which is the number or target sum.
4. Total number of recursive calls if n*n*...m times = n^m.
Time complexity: O(n^m)

Space complexity:
Height of tree is m and hence there will be m recursive call stack items evertime.
Space complexity = O(m)
'''