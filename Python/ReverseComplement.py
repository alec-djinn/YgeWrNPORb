'''
Reverse Complement Problem: Reverse complement a nucleotide pattern.
	Input: A DNA string Pattern.
	Output: Pattern, the reverse complement of Pattern.

CODE CHALLENGE: Solve the Reverse Complement Problem.

Sample Input:
	AAAACCCGGT

Sample Output:
	ACCGGGTTTT
'''

input_sequence = 'AAAACCCGGT'
reverse_complement = ''
n = len(input_sequence)-1
while n >= 0:
	if input_sequence[n] == 'A':
		reverse_complement += 'T'
		n = n-1
	elif input_sequence[n] == 'T':
		reverse_complement += 'A'
		n = n-1
	elif input_sequence[n] == 'C':
		reverse_complement += 'G'
		n = n-1
	else:
		reverse_complement += 'C'
		n = n-1
		
print('input   : ' + input_sequence)
print('output  : ' + reverse_complement)
		


