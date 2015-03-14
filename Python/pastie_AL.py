## WARNING: Horribly messy code below - use caution
## Artificial life program written in python and pygame
import pygame, random, colorsys, math

resolution = 100
blockSize = 6
mutationRate = 0.00022

environment = 100

pygame.init()
screen = pygame.display.set_mode([resolution * blockSize, resolution * blockSize])
pygame.display.set_caption("Artificial Life")

class BlankCell:
	def __init__(self, x, y):
		self.formula = ""
		self.answer = 0
		self.color = [0, 0, random.randint(14, 15) / 100.0]
		self.x = x
		self.y = y

	def fight(self):
		pass

class Cell:
	def __init__(self, parent, x, y):
		self.x = x
		self.y = y
		self.answer = parent.answer + 0
		self.color = parent.color[:]
		self.formula = parent.formula + ""

		if random.random() < mutationRate:
			bit = random.randint(0, 2)
			rand = random.randint(10, 30)
			self.color[bit] += random.choice([rand, -rand]) / 100.0
			if self.color[bit] > 1:
				self.color[bit] = 1
			elif self.color[bit] < 0.2:
				self.color[bit] = 0.2

			if random.random() < 0.5:	
				operation = random.randint(0, 3)
				if operation == 0: 
					operation = '+2'
				elif operation == 1: 
					operation = '-2'
				elif operation == 2:
					operation = '*2'
				elif operation == 3:
					operation = '/2'
				
				place = random.randint(0, len(self.formula) / 2) * 2
				self.formula = self.formula[:place] + operation + self.formula[place:]

			else:
				if len(self.formula) != 0:
					place = random.randint(0, len(self.formula) / 2) * 2
					self.formula = self.formula[:place] + self.formula[place:]

			if random.random() < 0.1:
				self.formula = ""
			self.answer = eval("2" + self.formula)

	def fight(self):
		enemy = 0

		while type(enemy) == int:
			enemy = random.randint(0, 3)

			if enemy == 0 and self.x < resolution - 1:
				enemy = cellGrid[self.x + 1][self.y]
			elif enemy == 1 and self.x > 0:
				enemy = cellGrid[self.x - 1][self.y]
			elif enemy == 2 and self.y < resolution - 1:
				enemy = cellGrid[self.x][self.y + 1]
			elif enemy == 3 and self.y > 0:
				enemy = cellGrid[self.x][self.y - 1]
				
		global environment
		if math.fabs(self.answer - environment) < 5:
			environment = random.randint(-600, 600)

		if math.fabs(self.answer - environment) + (len(enemy.formula) * 2) < math.fabs(enemy.answer - environment) + (len(enemy.formula) * 2):
			cellGrid[enemy.x][enemy.y] = Cell(self, enemy.x, enemy.y)
		else:
			cellGrid[self.x][self.y] = Cell(enemy, self.x, self.y)

#Generates a grid. Nested list comprehensions FTW!
cellGrid = [[BlankCell(i, j) for j in range(resolution)] for i in range(resolution)]


#Kickstart!
cellGrid[3][3] = Cell(BlankCell(3, 3), 3, 3)
cellGrid[3][3].color = [0.3, 0.6, 0.7]
cellGrid[3][3].formula = ""
cellGrid[3][3].answer = 2

cellGrid[17][17] = Cell(BlankCell(17, 17), 17, 17)
cellGrid[17][17].color = [0.6, 0.1, 0.5]
cellGrid[17][17].formula = ""
cellGrid[17][17].answer = 2

cellGrid[35][35] = Cell(BlankCell(35, 35), 35, 35)
cellGrid[35][35].color = [0.877, 0.52, 0.58]
cellGrid[35][35].formula = ""
cellGrid[35][35].answer = 2

alive = True
clock = pygame.time.Clock()
deathsPerIteration = 1000

while alive:

	screen.fill([255, 255, 255])
	for t in range(deathsPerIteration):
		cellGrid[random.randint(0, resolution - 1)][random.randint(0, resolution - 1)].fight()

	for x in range(resolution):
		for y in range(resolution):
			color = colorsys.hsv_to_rgb(cellGrid[x][y].color[0], cellGrid[x][y].color[1], cellGrid[x][y].color[2])
			color = [i * 255 for i in color]
			if blockSize > 1:
				pygame.draw.rect(screen, color, [x * blockSize, y * blockSize, blockSize, blockSize])
			else:
				screen.set_at((x, y), color)

	if pygame.mouse.get_pressed()[0] == True:
		pos = pygame.mouse.get_pos()
		pos = [i / blockSize for i in pos]
		print('2' + cellGrid[pos[0]][pos[1]].formula, cellGrid[pos[0]][pos[1]].answer, environment)
	
	if pygame.mouse.get_pressed()[2] == True:
		environment = random.randint(-600, 600)

	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			alive = False
	pygame.display.flip()

pygame.quit()