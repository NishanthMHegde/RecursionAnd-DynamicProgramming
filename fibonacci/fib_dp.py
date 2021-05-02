
#Fibonacci sequence: 1,1,2,3,5,8,13,21,34,55,... 

#Dynamic Programming implementation

def fib(n, memo={}):
	#memo case
	if n in memo.keys():
		return memo[n]
	#base case
	if n==1:
		memo[n] = 1
		return memo[n]
	if n==2:
		memo[n] = 1
		return memo[n]
	memo[n] = fib(n-1, memo) + fib(n-2, memo);
	return memo[n]

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(15))
print(fib(18))
print(fib(30))
print(fib(40))
#Time complexity

'''
Visualize the Fibonacci problem as a tree. 
1. Root node is the initial number n.
2. It has one left child whih is (n-1) and one right child that is (n-2).
3. Each of the left child will have a left and right child as fib(n-1) is called first.
4. The right children will not again have a left and right child as the value from the leftmost recursion call will be re-used.
4. Length of the tree (length of longest path) is n.
5. 

Time complexity: O(n) which is linear.


At any point in the program, either the left tree is executed and once it is done, right tree is executed recursively. 
So at any point, n memory units are occupied. 

Space complexity: O(n)
'''



