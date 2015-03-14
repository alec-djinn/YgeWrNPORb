## Numbers to DNA converter library

import itertools

def base10to4(number):
    '''(int) -> string'''
    tmp = []
    result = ''
    while(number > 0):
            tmp.append(number % 4)
            number = int(number // 4)
    while tmp:
        result += str(tmp.pop())
    return result

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
    # def get_varname(var):
    #     '''var_name -> string(var_name)
    #     Return a [string] of a variable's name.
        
    #     > my_var = 99
    #     > get_varname(my_var)
    #     >>> 'my_var'
    #     '''
    #     return [tpl[0] for tpl in itertools.filterfalse(lambda x: var is not x[1], globals().items())]
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

def fib(n):
    '''int -> [int, int, ...]
    Return a Fibonacci series up to n'''
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
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
    _fibs4 = []
    _fibs = fib(10**64)
    ATCG_permutations = permutate("ACTG",4)

    if verbose:
        check_var(_fibs)

    for item in _fibs:
        _fib4 = base10to4(item)
        _fibs4.append(_fib4)

    for _fib4 in _fibs4:
        if len(_fib4) >= min_length and len(_fib4) <= max_length:
            for item in ATCG_permutations:
                _fibDNA = _fib4.replace('0',item[0]).replace('1',item[1]).replace('2',item[2]).replace('3',item[3])
                fibDNAs.append((_fibDNA,_type,item))
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
    return [tpl[0] for tpl in itertools.filterfalse(lambda x: var is not x[1], globals().items())]

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
    result = []
    for item in itertools.permutations(string, length):
        result.append("".join(str(i) for i in item))
    
    return result


## generate DNA sequences from Nepero

## generate DNA sequences from Primes

## generate DNA sequences from Golden Ratio

## Divide the DNA in smaller seuqnce and blast them!

#from conventer import *