'''
Pattern Matching Problem: Find all occurrences of a pattern in a string.
	Input: Two strings, Pattern and Genome.
	Output: All starting positions where Pattern appears as a substring of Genome.

Note: Throughout this chapter, we will use 0-based indexing in problem implementations, meaning that we count starting at 0 instead of 1. For example, the starting positions of ATA in CGATATATCCATAG are 2, 4, and 10 instead of 3, 5, and 11.

Sample Input:
	ATAT
	GATATATGCATATACTT

Sample Output:
	1 3 9
'''

pattern = 'ATAT'
genome = 'GATATATGCATATACTT'
print('pattern   : ' + pattern)
print('genome    : ' + genome)
n = 0
while n <= len(genome):
	if genome[n:(n+len(pattern))] == pattern:
		print(n),
		n += 1
	else:
		n += 1

