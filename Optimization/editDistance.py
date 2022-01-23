# Function to calculate the minimum number of character insertion, deletion and substitution to change s into t
def calculateEditDistance(s, t):
	cache = {} # To store solutions of the subproblems
	# At any given time recurr(m, n) will deal with the sub problem which looks at the first m characters of s and first n characters of t
	def recurse(m, n):
		if (m,n) in cache: # To avoid solving the sub problem twice
			return cache[(m,n)]
		if m == 0: # if s is empty, we need n insertions
			result = n
		elif n == 0: # if t is empty, we need m deletions
			result = m
		elif s[m-1] == t[n-1]: # if the last characters are the same, we go to the next character
			result = recurse(m-1, n-1)
		else: # if the last characters are not the same, then we find the minimum of substitute, delete and insert
			subCost = 1 + recurse(m-1, n-1)
			delCost = 1 + recurse(m-1, n)
			insCost = 1 + recurse(m, n-1)
			result = min(subCost, delCost, insCost)
		cache[(m, n)] = result
		return result
	return recurse(len(s), len(t))

print(calculateEditDistance('a cat!'*10, 'the cats!'*9))
