
def main():
	import argparse

	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	exclusive = parser.add_mutually_exclusive_group()


	parser.add_argument('-v','--verbose',
						help='displays lots of prints on the console',
						action='store_true')
	parser.add_argument('-o','--outputfile',
						help='writes the results to a text file',
						type=str)
	exclusive.add_argument('-f','--inputfile',
						help='reads data from a text file: file.txt',
						type=str)
	exclusive.add_argument('-d','--inputdir',
						help='reads data from text files in a directory: /myDir/mySubdir',
						type=str)
	exclusive.add_argument('-s','--sequence',
						help="takes a sequence as input : 'aGtcAATGa'",
						type=str)
	exclusive.add_argument('-ss','--sequences',
						help="takes a list of sequences as insput: ['ATCG','GGGG',...]",
						type=list)
	parser.add_argument('-e','--experiment',
						help='takes the experiment you want to run as input: int'+\
							'\n*******************************************'+\
							'\nM13KE - p3 N-term display - NEB PhD-12  : 1'+\
							'\nM13KE - p3 N-term display - NEB PhD-7   : 2'+\
							'\nM13KE - p3 N-term display - NEB PhD-C7C : 3'+\
							'\nM13KE - p8 N-term display - custom      : 4'+\
							'\nDNA SELEX                               : 5'+\
							'\nRNA SELEX                               : 6'+\
							'\n*******************************************',
						type=int)


	args = parser.parse_args()
	
	if args.verbose:
		print '::::::::::::::::'
		print '::verbose mode::'
		print '::::::::::::::::'
		print '\narguments:'
		for item in str(args).split(','):
			item = item.replace('Namespace(','')
			item = item.replace(')','')
			print '\t'+item.strip()


main()
