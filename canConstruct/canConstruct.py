
'''
Problem statement: Given a target string and an array of sub-strings, find out if it is possible to construct 
the target string using any combinations of the given sub-strings any number of times.
'''
import re

def canConstruct(target, words):
	#base case
	if target == '':
		return True 

	#recursive case
	for word in words:
		if target.startswith(word):
			suffix = re.sub(word, '', target)
			if canConstruct(suffix, words):
				return True


	return False


print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) #true
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) #false
print(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) #true
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) #false


'''
Time and Space complexity

Time complexity: Let length of target string be m
Let there be n words in the array
In the worst case, the height of m will be traversed and n words will be used.
So the time complexity of the algorithm is O(n^m)

Space complexity: O(m^2) (m for height of tree/call stack and another m for each call to hold new suffix)
'''