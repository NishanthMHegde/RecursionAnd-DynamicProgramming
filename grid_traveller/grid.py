'''
Problem Statement: You are given a grid of size m*n. A man is placed on the top left corner cell.
What are the total number of ways in which the man can reach the bottom right cell of the grid?
'''

'''
Visualization and Recursive approach

1. The man can either move right or down at a time.
2. If he moves down, then we have a (m-1)*n sized grid to cover.
3. If he moves right, then we have a (m)*(n-1) sized grid to cover.
4. If he is in the last row or last column of the grid, then he can move in only one way.
5. If m is 0 or n is 0, then he cannot move at all.

'''


#Recursive approach

def grid_traveller(m, n):
	#base case
	if m==0 or n==0:
		return 0
	if m==1 or n==1:
		return 1

	#recursive case
	#move down and move right
	return grid_traveller(m-1, n) + grid_traveller(m, n-1)


print(grid_traveller(1, 0))
print(grid_traveller(0, 1))
print(grid_traveller(1, 1))
print(grid_traveller(1, 2))
print(grid_traveller(2, 1))
print(grid_traveller(3, 3))
print(grid_traveller(4, 4))
print(grid_traveller(10, 10))


'''
Space and time complexity

1. Root node is (m,n).
2. Left child will be (m-1, n) and right child will be (m, n-1)
3. The maximum height of the tree is (m+n) which is the longest route the tree can have.
4. The tree is once again binary.
5. The total number of function calls is 2*2*2... (n+m) = 2^(n+m).

Time complexity: O(2^(m+n)).


Space complexity: O(n+m)
'''