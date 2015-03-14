# -*- coding: utf-8 -*-
'''
A most frequent k-mer with up to d mismatches in Text is simply a string Pattern maximizing Countd(Text, Pattern) among all k-mers. Note that Pattern does not need to actually appear as a substring of Text; for example, as we saw above, AAAAA is the most frequent 5-mer with 1 mismatch in AACAAGCTGATAAACATTTAAAGAG, even though it does not appear exactly in this string. Keep this in mind while solving the following problem:

Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
     Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
     Output: All most frequent k-mers with up to d mismatches in Text.

CODE CHALLENGE: Solve the Frequent Words with Mismatches Problem.

Sample Input:
     ACGTTGCATGTCGCATGATGCATGAGAGCT 4 1
Sample Output:
     GATG ATGC ATGT
'''

#define kmers long 4
s = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
motif_len = 4
motif_dict = {}
mismatch = 1

print('Sequence = ' + s)

#find unique k-mers in the sequence
for i in range(len(s)-motif_len):
	motif = s[i:i+motif_len]
	if motif not in motif_dict:
		motif_dict[motif] = 1
	else:
		motif_dict[motif] += 1

#1: generate a list of motif
motif_list = []
for k in motif_dict:
	motif_list.append(k)
#print('Motifs found : '),

#2: check where the motifs are [wrongly commented]
dict = {}
input = s
ylist = []
for item in motif_list:
	motif = item
	results = []
	y = 0
	for n in range(len(input)-len(motif)+1):
		counter = 0
		sample = input[n:n+len(motif)]
		for i in range(len(sample)):
			if sample[i] == motif[i]:
				pass
			else:
				counter += 1
		if counter <= mismatch:
			results.append(n)
	
	dict[item] = []
	for value in results:
		dict[item].append(value)
		y += 1
	ylist.append(y)
	
print('\nProgram Output:'),
final_list = []
for item in dict:
	if len(dict[item]) == max(ylist):
		print(item),
		final_list.append([item, dict[item]])
#print('')
#print(final_list)

n=0
for n in range(len(final_list)):
	for m in range(max(ylist)):
		f = final_list[n][1][m]
		final_list[n][1][m] = s[f:f+motif_len]
#for item in final_list:
	#for n in range(len(item[1])):
		#print(item[1][n])
		#define the consensus sequence -> to do but not necessary for this case
		#for k in range(len(dict[item])): final_list[item].append(dict[item])
#list founded k-mers
print('\nSample  Output: GATG ATGC ATGT') 	#same values, different order. It doesn't matter
											
