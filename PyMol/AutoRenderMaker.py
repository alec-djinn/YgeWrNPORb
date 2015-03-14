# AutoRenderMaker
# Note: The tiles are tilted and so not overlapping well
area = 57358.473
counter = 0

def round_up_area(area):
	tmp = int(area)
	n = 1
	while tmp > n**2:
		n += 1
	return n**2

scene_size = round_up_area(area)

resolution = '800, 800'
zoom = 10
grid_size = 6
file_name = 'Virus_'

limit = scene_size**(1.0/2.0)
delta = ((limit) / (grid_size)) / grid_size


def initiate(zoom):
	moves = []
	moves.append('zoom center, '+ str(zoom))
	moves.append('translate ' + str([delta, -delta, 0]))
	return moves


def render(resolution, file_name):
	global counter
	moves = []
	moves.append('ray ' + resolution)
	moves.append('png tile_' + file_name + str(counter) + '.png')
	counter += 1
	return moves


def move_next_col(delta):
	moves = []
	moves.append('translate ' + str([-delta,0,0]))
	return moves


def move_next_row(delta):
	moves = []
	moves.append('translate ' + str([0,delta,0]))
	return moves

def move_col0(delta, grid_size):
	moves = []
	col0 = delta * grid_size
	moves.append('translate ' + str([col0,0,0]))
	return moves



# SOLVE
all_moves = []
all_moves.append(initiate(zoom))
all_moves.append(render(resolution, file_name))
for i in range(grid_size):
	for j in range(grid_size):
		all_moves.append(move_next_col(delta))
		all_moves.append(render(resolution, file_name))
	all_moves.append(move_col0(delta, grid_size))
	all_moves.append(move_next_row(delta))
	all_moves.append(render(resolution, file_name))

with open("AutoRender.txt", 'w') as out_file:
	out_file.write('# AutoRender beta'+ "\n")
with open("AutoRender_Virus.txt", 'a') as out_file:
	for move_set in all_moves:
		for move in move_set:
			print move
			out_file.write(move + "\n")


