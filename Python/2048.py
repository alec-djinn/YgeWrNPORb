## 2048 game implementation

'''
2048 - by alec_djinn - Jun 2014
'''
import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    temp_line = []
    result_line = []
    # iterate over line's items
    for item in line:
        # look for non-zero entries
        if item != 0:
            # append to temp_line a list made by item and False.
            # False indicates the "merged status"
            temp_line.append(item)
    # sum consecutive tile with same number
    # append the result to result_line
    num = 0
    while num in range(len(temp_line)):
        try:
            if temp_line[num] == temp_line[num+1]:
                result_line.append(temp_line[num] + temp_line[num+1])
                num += 2
            else:
                result_line.append(temp_line[num])
                num += 1
        except IndexError:
            result_line.append(temp_line[num])
            num += 1
    # fill remaining tiles with zeros
    len_difference = len(line) - len(result_line)
    while len_difference > 0:
        result_line.append(0)
        len_difference = len(line) - len(result_line)

    return result_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        # store the number of rows and columns
        self.grid_width = grid_width
        self.grid_height = grid_height
        # set the grid
        self.cells = [ [0 for col in range(self.grid_width)] for row in range(self.grid_height)]
        # make a list of indices of the tiles
        self.indices = [[(row,col) for col in range(self.grid_width)] for row in range(self.grid_height)]        
        # define the direction tiles indices and store them in a dictionary
        self.up_row = self.get_row(0, self.indices)
        self.down_row = self.get_row(-1, self.indices)
        self.left_col = self.get_col(0, self.indices)
        self.right_col = self.get_col(-1, self.indices)
        self.index_dict = {UP:self.up_row, DOWN:self.down_row, LEFT:self.left_col, RIGHT:self.right_col}
   
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        # set [value, status] for each cell in the grid
        #self.cells = [ [0 for col in range(self.grid_width)] for row in range(self.grid_height)]
        for col in range(self.grid_width):
            for row in range(self.grid_height):
                self.cells[row][col] = 0
        return self.cells
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """        
        self.show_grid(self.cells)
        
    def get_row(self, number, grid_name):
        """
        Reteurn the value of a specific row.
        """
        row = []
        for item in grid_name[number]:
            row.append(item)        
        return row

    def get_col(self, number, grid_name):
        """
        Reteurn the value of a specific column.
        """
        col = []
        for item in range(len(grid_name)):
            col.append(grid_name[item][number])
        return col

    def show_grid(self, grid_name):
        """
        Print the grid.
        """
        for number in range(len(grid_name)):
            print self.get_row(number, grid_name)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        
        #if direction == 1: dir_, rev_ = 'UP', False
        #if direction == 2: dir_, rev_ = 'DOWN', True    
        #if direction == 3: dir_, rev_ = 'LEFT', True
        #if direction == 4: dir_, rev_ = 'RIGHT', False
        
        
        # set the for loop iteration limit
        limit = range(self.grid_height) if direction == UP or direction == DOWN else range(self.grid_width)
        value_list = [] # values to merge()   
        temp_list = [] # indices of value to merge()
        line = self.index_dict[direction]
        offset = OFFSETS[direction]
        # generate a list of indices
        for item in line:
            index = item
            value_list = [] # values to merge()   
            temp_list = [] # indices of value to merge()
            for num in limit:
                    temp_list.append(index)
                    next_index = tuple(map(sum,zip(index,offset)))
                    index = next_index
                    print(num)
            # print temp_list
            # get values from indices
            for index in temp_list:
                value_list.append(self.get_tile(index[0],index[1]))
            # print value_list
            # merge the list and copy the results back to the grid
            
            merged_list = merge(value_list)
            counter = 0
            for index in temp_list:
                self.set_tile(index[0],index[1],merged_list[counter])
                counter += 1
        self.new_tile()
        print "----------"
            
    def new_tile(self): # add a check for zeros in self.cells to solve crashes at the end of the game 
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # check if there is space left in the grid
        # i.e. if there is at least one cell with zero
        zeros_list = []
        for col in range(self.grid_width):
            for row in range(self.grid_height):
                if self.cells[row][col] == 0:
                    zeros_list.append(0)
        if 0 in zeros_list:
            zero_check = True
        else:
            zero_check = False
            print("Game Over!")
                
        # make a new tile in a random position
        flag = False
        while flag == False and zero_check == True:            
            row = random.randrange(self.grid_height)
            col = random.randrange(self.grid_width)
            if self.get_tile(row,col) == 0:
                value = 4 if random.randrange(10) < 1 else 2
                self.set_tile(row,col,value)
                print "New tile!"
                flag = True
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self.cells[row][col]

    
poc_2048_gui.run_gui(TwentyFortyEight(5, 4))