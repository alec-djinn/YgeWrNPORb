## Simple 2D matrix class
## Python 2.7
## by alec_djinn - 2014


class Matrix2D:
	def __init__(self):
		self.matrix = [] # each item is a row in the matrix
		self.rows = 0
		self.columns = 0
		self.name = 'Unnamed'
		
	def __str__(self):
		return self.matrix
		
	def generate(self, rows, columns, verbose=False):
		'''
		Returns a list of lists containing the indices of the matrix (row, col)
		and prints it by row.
		int, int -> [[(int, int), ...], ...]
		'''
		self.rows = rows
		self.columns = columns
		self.matrix = [[(row, col) for col in range(columns)] for row in range(rows)]
		if verbose ==  True:
			print('Generated a %d row/s by %d colmn/s matrix') % (rows, columns)
			print('--------' * columns)
			self.printme()
			print('--------' * columns)
		return self.matrix
		
	def printme(self, verbose=False):
		'''
		Prints the matrix by row.
		'''
		if verbose == True:
			print('I am a %d row/s by %d colmn/s matrix') % (self.rows, self.columns)
		for row in self.matrix:
			print(row)
	
	def get_cell(self, row, col, verbose=False):
		'''
		Returns a specific cell of the matrix.
		'''
		if verbose ==  True:
			print('cell[row=%d, col=%d ]...') % (row, col)
			print(self.matrix[row][col])
		return self.matrix[row][col]
			
	def get_row(self, n, verbose=False):
		'''
		Returns the row n of the matrix.
		'''
		if verbose ==  True:
			print('matrix[row=%d]...') % n
			print(self.matrix[n])
		return self.matrix[n]
	
	def get_col(self, n, verbose=False):
		'''
		Returns the column n of the matrix.
		'''
		column_items = []
		i = 0
		while i < self.rows:
			column_items.append(self.matrix[i][n])
			i += 1
		if verbose ==  True:
			print('matrix[col=%d]...') % n
			for item in column_items:
				print(item)
		return column_items
			
	def write_cell(self, row, col, data, verbose=False):
		'''
		Write some data into a specific cell of the matrix.
		'''
		self.matrix[row][col] = data
		if verbose ==  True:
			print('Data wrote into cell[row=%d, col=%d ]...') % (row, col)
			print(self.matrix[row][col])							
		return self.matrix[row][col]
		
	def write_row(self, row, data, verbose=False):
		'''
		Write some data into a row, cell by cell.
		'''
		
		for col in range(self.columns):
			try:
				self.write_cell(row, col, data[col])
			except IndexError:
				# add 'Na' if len(data) is shorter then len(row)
				self.write_cell(row, col, 'Na')
			
		if verbose ==  True:
			print('Data wrote into matrix[row=%d]...') % row
			self.get_row(row,True)
		return self.get_row(row,True)

	def write_col(self, col, data, verbose=False):
		'''
		Write some data into a column, cell by cell.
		'''
		
		for row in range(self.rows):
			try:
				self.write_cell(row, col, data[row])
			except IndexError:
				# add 'Na' if len(data) is shorter then len(row)
				self.write_cell(row, col, 'Na')
			
		if verbose ==  True:
			print('Data wrote into matrix[col=%d]...') % col
			self.get_col(col,True)
		return self.get_col(col,True)	
				
				
#test
print('#########')
m = Matrix2D()
m.generate(4,5,True)
m.printme()
m.get_row(1,True)
m.get_col(1,True)
m.get_cell(3,2,True)
m.write_cell(3,2, (9,9,9),True)
m.write_row(3,[3,3])
m.printme()
for n in range(4):
	m.write_row(n,[0,0,0,0,0])
m.printme()
m.write_col(0,[1,1,1,1])
m.printme()
