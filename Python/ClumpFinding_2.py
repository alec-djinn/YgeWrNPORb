import time
 
f = open("E-coli.txt",'r') #input from a large file, 4.2MB
genome =  f.read()

start_time = time.time()
L = 500 # genome substring length
k = 9 # length of the motif
t = 3 # minimum repetition of the motif
n = 0
motif_len = k
list = []
n += 1
motif_dict = {}
 
 
for i in range(len(genome)-motif_len):
	motif = genome[i:i+motif_len]
	if motif not in motif_dict:
	# Here is the trick to make it iterate only once inside the genome.
	# The value of the dictionary is the list motif[].
	# motif[0] is an accumulator and take trace of how many times the motif is repeated
	# from motif[1] it traces the index of founded motif
		motif_dict[motif] = [1,i] 
	else:
		motif_dict[motif][0] += 1 # accumulate the count
		motif_dict[motif].append(i) # append() to the list the index of all founded motif
for motif in motif_dict:
	# look for motif repeated t times with an index distance of L
	if motif_dict[motif][0] >= t and motif not in list:
		for n in range(len(motif_dict[motif])-t):
			if motif_dict[motif][n+t-1] - motif_dict[motif][n] <= L:
				if motif not in list:
					list.append(motif)

for motif in list:
	print(motif),
 
f.close() 
print('\nexecution time'),
print(str(time.time() - start_time) + ' seconds\n')