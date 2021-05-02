'''
Problem Statement: You are given a grid of size m*n. A man is placed on the top left corner cell.
What are the total number of ways in which the man can reach the bottom right cell of the grid?
'''

'''
Memoization:

1. Create a dictionary datastructure with a key in the form of m,n which holds the number of steps.
2. Re-use the values in dictionary to reduce time complexity of recursive calls.

'''


#Recursive approach

def grid_traveller(m, n, memo={}):
	key = str(m) +"," + str(n)

	#memo case
	if key in memo.keys():
		return memo[key]
	#base case
	if m==0 or n==0:
		memo[key] = 0
		return memo[key]
	if m==1 or n==1:
		memo[key] =1
		return memo[key]

	#recursive case
	#move down and move right
	memo[key] = grid_traveller(m-1, n, memo) + grid_traveller(m, n-1, memo)
	return memo[key]

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
3. All the left and right child sub-nodes will not be recomputed as they are stored in the memoized object.
4. The tree is not binary and the total number of nodes we traverse is (m+n).

Time complexity: O(m+n).


Space complexity: O(n+m)
'''