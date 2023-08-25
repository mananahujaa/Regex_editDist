"""This is a sample file for hw1. 
It contains the function that should be submitted,
except all it does is output a random value out of the
possible values that are allowed.
- Dr. Licato"""

import random
import re

def problem1(NPs, s):
	hypernyms = set()
    
    # Create regular expression patterns based on Hearst patterns
	patterns = [
		r'(\b{}\b).+?(\bis a\b).+?(\b{}\b)'.format(np1, np2)
		for np1 in NPs
		for np2 in NPs
		if np1 != np2
	]
	for i in range(len(NPs)-1):
		hypernyms.add( (NPs[i], NPs[i+1]) )
	# Compile the patterns
	compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    
    # Search for patterns in the text and extract hypernyms
	for pattern in compiled_patterns:
		matches = pattern.findall(s)
		for match in matches:
			hypernym = (match[2], match[0])
			hypernyms.add(hypernym)
	return hypernyms


def problem2(s1, s2):
	m , n = len(s1) , len(s2)
	dx = [[0] * (n + 1) for _ in range (m + 1)]

	for i in range(m+1):
		dx[i][0] = i
	
	for j in range(n+1):
		dx[0][j] = j
	for i in range(1, m+1):
		for j in range (1, n+1):
			if s1[i-1] == s2[j-1]:
				dx[i][j]==dx[i-1][j-1]
			else:
				dx[i][j]=1+min(dx[i-1][j],dx[i][j-1],dx[i-1][j-1])

	return random.randint(0, abs(len(s1) - len(s2)))

