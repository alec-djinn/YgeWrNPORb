from random import *
from math import *
import time
import signal
import threading






MATH = ['ceil(x)','copysign(x, y)','fabs(x)','factorial(x)',
		'floor(x)','fmod(x, y)','modf(x)','trunc(x)',
		'exp(x)','expm1(x)','log(x)','log(x,y)','log1p(x)',
		'log2(x)','log10(x)','pow(x, y)','sqrt(x)',
		'acos(x)','asin(x)','atan(x)','atan2(x, y)','cos(x)',
		'hypot(x, y)','sin(x)','tan(x)','degrees(x)',
		'radians(x)','acosh(x)','asinh(x)','atanh(x)',
		'cosh(x)','sinh(x)','tanh(x)','gamma(x)','lgamma(x)']

OP = ['+','-','/','//','*','**','%']

def gen_formula(lenght):
	'''Generate a valid math formula of selected lenght.'''
	formula = ''
	while lenght > 0:
		formula += sample(MATH,1)[0]
		if lenght > 1:
			formula += sample(OP,1)[0]
		lenght -= 1
	return formula
#formula = gen_formula(8)

def nest_formula(formula):
	'''Replace randomly an (x) or (x,y) argument with a function.
	nest_formula(sin(x)) -> sin(tan(x))'''
	# determine where (x) and (x,y) are.
	x_idx = []
	xy_idx = []
	for idx in range(len(formula)):
		if formula[idx:idx+3] == '(x)':
			x_idx.append(idx)
		elif formula[idx:idx+5] == '(x,y)':
			xy_idx.append(idx)
	# determine what can be nested
	if len(x_idx) > 0 and len(xy_idx) > 0:
		choice = sample(['(x)','(x,y)'],1)[0]
	elif len(x_idx) > 0:
		choice = '(x)'
	elif len(xy_idx) > 0:
		choice = '(x,y)'
	# nest a function by converting an argument to a function
	if choice == '(x)':
		idx = int(sample(x_idx,1)[0]) # pick a random position to nest
		nested_formula = formula[:idx]+'('+sample(MATH,1)[0]+')'+formula[idx+3:]
	else:
		idx = int(sample(xy_idx,1)[0]) # pick a random position to nest
		nested_formula = formula[:idx]+'('+sample(MATH,1)[0]+','+sample(MATH,1)[0]+')'+formula[idx+5:]
	print(nested_formula)
#b = nest_formula(formula)

class Timeout():
    """Timeout class using ALARM signal."""
    class Timeout(Exception):
        pass
 
    def __init__(self, sec):
        self.sec = sec
 
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)
 
    def __exit__(self, *args):
        signal.alarm(0)    # disable alarm
 
    def raise_timeout(self, *args):
        raise Timeout.Timeout()

def multi_thread_fusion_genes_annotation(folder_path, extension):
	''' Executes annotate_fusion_genes() for each dataset file in a folder.
	Each execution run on a different thread.'''
	dataset_files = list_of_files(folder_path, extension)
	threads = 0
	for file_ in dataset_files:
		threads += 1
		print('thread', threads, ':')
		threading.Thread(target=annotate_fusion_genes, args=(file_,)).start() # with multithreading
#multi_thread_fusion_genes_annotation('/home/amarcozz/Documents/Projects/Fusion Genes/Scripts/test_datasets', 'txt')

start = time.time()
prime1 = 13
prime2 = 87
error = 2
x = prime1*prime2
formulas = []
n = 0
while n < 100:
	result = False
	y = uniform(0.0, 10.0)
	a = gen_formula(5)
	with Timeout(1): # time execution limit
		try:
			exec('result='+a, globals())
			if abs(abs(result)-prime1) < error or abs(abs(result)-prime2) < error:
				print(a,'.'*(70-len(a)),result,'\t','y:',y)
				formulas.append(a)
				n += 1
		#except Timeout.Timeout:
		#	print("Timeout")		
		except:
			pass	

print('Found',len(formulas),'good formulas')
print('Execution time:', time.time()-start)