'''
Problem statement: An integer number and an array of postive numbers is given.
We need to find out if the integer number can be formed by adding any combination of the given
numbers in the array.

The numbers can be used any number of times.
'''

'''
Visualization and Recurisve approach

M :given number 
n: length of array of numbers
1. We first take the given number as root node.
2. We then subtract each of the given n numbers from the root node to obtain n child nodes.
3. We further subtract each of the given n numbers from the value in each of the previous nodes til we reach the base case.
4. If we obtain a 0 at any of the nodes, we return a 0. This means that we can obtain the number m from summing any of the n numbers.
. We return false as soon as we reach a negetive number from the node.
'''

#Recursive approach

def canSum(m,arr):

	#base case
	if m==0:
		return True
	if m<0:
		return False
	#recursive case
	for num in arr:
		remainder = m - num
		#return true if we find at least one combination of numbers that adds up
		if canSum(remainder, arr):
			return True

	#false case
	return False #Return False if no combination of numbers could return True



print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(7, [2, 3]))
print(canSum(8, [2, 3, 5]))
print(canSum(300, [7, 14]))

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