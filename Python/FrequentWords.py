'''
Frequent Words Problem: Find the most frequent k-mers in a string.
	Input: A string Text and an integer k.
	Output: All most frequent k-mers in Text.

Sample Input:
	ACGTTGCATGTCGCATGATGCATGAGAGCT
	4

Sample Output:
	CATG GCAT
'''

s = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
motif_len = 4
motif_dict = {}
for i in range(len(s)-motif_len):
	motif = s[i:i+motif_len]
	if motif not in motif_dict:
		motif_dict[motif] = 0
	else:
		motif_dict[motif] += 1
for k in motif_dict:
	if motif_dict[k] == max(motif_dict.values()): # the most frequent entry in the dictionary
		print(k),
