
'''
Problem statement: Given a target string and an array of sub-strings, find out if it is possible to construct 
the target string using any combinations of the given sub-strings any number of times.
'''
import re

def canConstruct(target, words, memo={}):
	#memoization case
	if target in memo.keys():
		return memo[target]
	#base case
	if target == '':
		memo[target] = True
		return True 

	#recursive case
	for word in words:
		if target.startswith(word):
			suffix = re.sub(word, '', target)
			if canConstruct(suffix, words):
				memo[target] = True
				return True

	memo[target] = False			
	return False


print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], memo={})) #true
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], memo={})) #false
print(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], memo={})) #true
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], memo={})) #false


'''
Time and Space complexity

Time complexity: Let length of target string be m
Let there be n words in the array
In the worst case, the height of m will be traversed and n words will be used only on one side of tree.
So the time complexity of the algorithm is O(n*m)

Space complexity: O(m^2)
'''