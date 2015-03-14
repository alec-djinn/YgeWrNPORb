## Useful little functions.
'''
fun_lab.py
alec_djinn - Jan 2015
'''

def base10to4(number):
    '''(int) -> string'''
    tmp = []
    result = '0'
    while(number > 0):
            tmp.append(number % 4)
            number = int(number // 4)
    while tmp:
        result += str(tmp.pop())
    return result

def check_for_infection(file_name, motif):
	'''
	Look for the mark (motif) in a file.
	'''
	with open(file_name, 'r') as infile:
		for line in infile:
			if motif in line:
				return True
	return False

def check_var(var):
    '''var_name -> bool #prints some output
    Print out stuff about a variable.
    
    >var_name = 'whatever!'
    >check_var(var_name)
    >>> 
    __variable check__
    name  : var_name
    value : whatever!
    type  : <class 'str'>
    lenght: 9

    '''
    def get_varname(var):
        import itertools
        '''var_name -> string(var_name)
        Return a [string] of a variable's name.
        
        > my_var = 99
        > get_varname(my_var)
        >>> 'my_var'
        '''
        return [tpl[0] for tpl in itertools.filterfalse(lambda x: var is not x[1], globals().items())]
    try:
        print('\n__variable check__')
        print('name  :',get_varname(var)[0],)
        print('value :',var)
        print('type  :',type(var))
        print('lenght:',len(var))
        return True
    except Exception as e:
        print(e)
        return False

def combine_files(list_of_file_names): # to finish
	'''
	Check for instructions hidded in various files.
	Combine the instructions into one single executable file.
	'''
	lines = []
	for each_file in list_of_file_names:
		with open(each_file, 'r') as infile:
			for line in infile:
				lines.append(line)

def count_mismatches(motif, sequence, max_mismatches):
	'''(str, str, int) -> (int, str)
	Counts the mismatches between two string (motif, sequence).
	Returns the number of mismatches and a a modified motif (x_motif) where all the mismatched position are replaced with '-'. If mismatche > max_mixmatches ignore it.
	count_mismatches('12345', '12045') -> (1, '12-45')
	count_mismatches('12345', '12040') -> (2, '12-4-')
	Precondition: motif and sequence must have the same lenght
	'''
	i = 0
	mismatches = 0
	x_motif = ''
	while i < len(motif) and len(motif) == len(sequence):
		if motif[i] == sequence[i]:
			x_motif += motif[i]
			i += 1
		else:
			mismatches += 1
			x_motif += '-'
			i += 1
	if mismatches <= max_mismatches:	
		return mismatches, x_motif
	
def count_mismatches_in_long_sequence(motif, long_sequence, max_mismatches):
	'''(str, str, int) -> (int, str)
	Counts the mismatches between two string (motif, sequence).
	Uses count_mismatches() iterating through a sequence of any lenght.
	'''
	i = 0
	small_sequence = long_sequence[i:i+len(motif)]
	while i < (len(long_sequence)-len(motif)):
		
		if count_mismatches(motif, small_sequence, max_mismatches) != None:
			print(count_mismatches(motif, small_sequence, max_mismatches))
			#print(small_sequence)
		i += 1
		small_sequence = long_sequence[i:i+len(motif)]
		#print(small_sequence)

def fib(n):
    '''int -> [int, int, ...]
    Return a Fibonacci series up to n'''
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def fib4(n):
    '''int -> ['int', 'int', ...]
    Return a Fibonacci series up to n.
    
    > b = fib(1000)
    > check_var(b)
    >>> __variable check__
        name  : b
        value : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
        type  : <class 'list'>
        lenght: 17

    > a = fib4(1000)
    > check_var(a)
     >>> __variable check__
         name  : a
         value : ['0', '1', '1', '2', '3', '11', '20', '31', '111', '202', '313', '1121', '2100', '3221', '11321', '21202', '33123']
         type  : <class 'list'>
         lenght: 17
    '''
    result = []
    a, b = 0, 1
    while a < n:
        result.append(base10to4(a))
        a, b = b, a+b
    result[0] = '0' # replace the empty string in ['', '1', ...]
    return result

def fib_to_DNA(min_length=20, max_length=64, verbose=False):
    '''(int, int, bool) -> [(_fibDNA,_type,item), (), ...]
    Generates DNA sequences from Fibonacci's numbers of a specific digits size.
    converts each Fibonacci in a base4 number and replace the 4digits with all the permutations of 'ACTG'.
    Returns a list of tuples containing
    [0] -> a DNA sequence rapresenting the Fibonacci number in base4
    [1] -> the specific permutation used to obtain [0]
    '''
    if min_length > max_length:
        return 'Error in function call arguments: min_length > max_length, it must be <='

    _type = ('Fibonacci','min_length='+str(min_length)+', '+'max_length='+str(max_length))
    fibDNAs = []
    _fib4s = []
    _fibs = fib(10**64)
    _ATCG_permutations = permutate("ACTG",4)

    if verbose:
        check_var(_fibs)

    for item in _fibs:
        _fib4 = base10to4(item)
        _fib4s.append(_fib4)

    for _fib4 in _fib4s:
        if len(_fib4) >= min_length and len(_fib4) <= max_length:
            for perm in _ATCG_permutations:
                _fibDNA = _fib4.replace('0',perm[0]).replace('1',perm[1]).replace('2',perm[2]).replace('3',perm[3])
                fibDNAs.append((_fibDNA,_type,_fib4,perm))
                if verbose:
                    print('===============================')
                    print(item)
                    check_var(_piDNA)
        if verbose:
            check_var(fibDNAs)
    return fibDNAs

def get_varname(var):
    '''var_name -> string(var_name)
    Return a [string] of a variable's name.
    
    > my_var = 99
    > get_varname(my_var)
    >>> 'my_var'
    '''
    import itertools
    return [tpl[0] for tpl in itertools.filterfalse(lambda x: var is not x[1], globals().items())]

def execute_file(file_name):
	'''
	Executes line-by-line the python code found in infile_name.
	'''
	with open(file_name, 'r') as infile:
		for line in infile:
			exec(line)

def mark_file(file_name, motif):
	'''
	Write a line with motif at the end of the file.
	'''
	with open(file_name, 'a') as infile:
		outfile.write(motif)

def permutate(string,length):
    '''(string,int) -> list(string, string, ...)
    Returns the a list of permutation of a string.
    >permutate("ACTG",4)
    >>> ['ACTG', 'ACGT', 'ATCG', 'ATGC',
        'AGCT', 'AGTC', 'CATG', 'CAGT',
        'CTAG', 'CTGA', 'CGAT', 'CGTA',
        'TACG', 'TAGC', 'TCAG', 'TCGA',
        'TGAC', 'TGCA', 'GACT', 'GATC',
        'GCAT', 'GCTA', 'GTAC', 'GTCA']

    '''
    import itertools
    result = []
    for item in itertools.permutations(string, length):
        result.append("".join(str(i) for i in item))
    
    return result

def pi_to_DNA(pi_file='pi.ale', length=64, verbose=False):
    '''(string, int, bool) -> [(_piDNA,_type,item), (), ...]
    Generates DNA sequences from pi.
    Takes the first 'length' digits from pi from a file,
    converts pi in a base4 number and replace the 4digits with all the permutations of 'ACTG'.
    Returns a list of tuples containing
    [0] -> a DNA sequence rapresenting pi in base4
    [1] -> the specific permutation used to obtain [0]
    '''
    _type = ('pi','pi_file='+str(pi_file)+', '+'length='+str(length))
    piDNAs = []
    ATCG_permutations = permutate("ACTG",4)
    
    with open(pi_file,'r') as f:
        content = [line for line in f.readlines() if line[0] != '#']
    _pi = content[0][:length+1] # +1 considering the '.'
    
    digits = str(_pi.replace('.',''))
    number = int(digits)
    _pi4 = base10to4(number)

    if verbose:
        check_var(ATCG_permutations)
        check_var(_pi)
        check_var(digits)
        check_var(number)
        check_var(_pi4)

    for item in ATCG_permutations:
        _piDNA = _pi4.replace('0',item[0]).replace('1',item[1]).replace('2',item[2]).replace('3',item[3])
        piDNAs.append((_piDNA,_type,item))
        if verbose:
            print('===============================')
            print(item)
            check_var(_piDNA)
    if verbose:
        check_var(piDNAs)
    return piDNAs

def python_check():
	version_check = int((sys.version)[0]) # check Python version
	if version_check == 2:
		# execute code for Python 2
		print('Detected Python 2')
		#find_motifs(out_file_1, motif_len, repetition, out_file_2)
	elif version_check == 3:
		#execute code for Python 3
		print('Detected Python 3')
	else:
		sys.exit('Python version error, please execute this orogram using Python version 2.7.x or newer')

def reverse_complement(dna_sequence='TTTTAAAACCCCGGGG',verbose=False):
	''' string -> string
	Returns the reverse complement of a DNA sequence.
	Input: A DNA string pattern.
	Output: The reverse complement of Pattern.
	'''
	reverse_complement = ''
	n = len(dna_sequence)-1
	while n >= 0:
		if dna_sequence[n] == 'A':
			reverse_complement += 'T'
			n = n-1
		elif dna_sequence[n] == 'T':
			reverse_complement += 'A'
			n = n-1
		elif dna_sequence[n] == 'C':
			reverse_complement += 'G'
			n = n-1
		else:
			reverse_complement += 'C'
			n = n-1
	if verbose:
		print('input   : ' + input_sequence)
		print('output  : ' + reverse_complement)
	return reverse_complement

def shuffle_file(file_name):
	'''
	Shuffles the lines of an input file.
	'''
	import random
	lines = []
	with open(file_name, 'r') as infile:
		for line in infile:
			lines.append(line)
	print(lines)
	random.shuffle(lines)
	print(lines)
	with open(file_name, 'w') as outfile:
		for line in lines:
			outfile.write(line)

def update_file(file_name, lines):
	'''
	Write lines at the end of an existing file.
	'''
	with open(file_name, 'a') as outfile:
		for line in lines:
			outfile.write(line)

def write_lines_to_file(lines, file_name):
	'''
	Takes a list of string as input (lines).
	Writes each string as separate line in outfile_name
	'''
	with open(file_name, 'w') as outfile:
		for line in lines:
			outfile.write(line+'\n')

def zeta(s,iterations):
	''' 'Naive' Riemann Zeta function'''
	result = 0
	while iterations > 0:
		result += 1/(iterations**s)
		iterations -= 1
	return result
#import time
#import math
# start = time.time()
# for s in [-1,1,complex(1)]:
#  	for n in range(1000):
#   		print(s,n,zeta(s,n))
# print('execution time :',time.time()-start)
# print('pi**2 /6 :',(math.pi**2)/6)
# print(-1/12)



