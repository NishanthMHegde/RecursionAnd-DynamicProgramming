
#Fibonacci sequence: 1,1,2,3,5,8,13,21,34,55,... 

#Recursive implementation

def fib(n):
	#base case
	if n==1:
		return 1;
	if n==2:
		return 1;
	return fib(n-1) + fib(n-2);


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

#Time complexity

'''
Visualize the Fibonacci problem as a tree. 
1. Root node is the initial number n.
2. It has one left child whih is (n-1) and one right child that is (n-2).
3. Each of the left and right child similarly have their own left and right children till we reach base case.
4. Length of the tree (length of longest path) is n.
5. There are 2 children for each of the node in the tree. 
6. The number of nodes on each level i of the tree is 2^1. (for ex: level 2 has 2^2 =4 nodes).
7. Hence the total number of nodes in the tree is 1*2*2*2*2...n. We have 2^n number of nodes and 2^n number of recursive calls.

Time complexity: O(2^n) which is exponential.


At any point in the program, either the left tree is executed and once it is done, right tree is executed recursively. 
So at any point, n memory units are occupied. 

Space complexity: O(n)
'''



