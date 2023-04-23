

def create_grid():
	grid = []
	HEIGHT = 10
	WIDTH = 10
	for row in range(HEIGHT):
		row = []
		for cell in range(WIDTH):
			row.append(" ")
		grid.append(row)
	return grid

def display_grid(grid):

	for count , row in enumerate(grid):
		for count1, cell in enumerate(row):
			print(" ", end = "")
			if cell == "R":
				print("R", end = " |")
			elif cell == "B":
				print("B", end = " |")
			elif cell == " ":
				print(cell, end = " |")
				 #" ""cell"" ""|"
		print()
		print("-" * (4 * len(row)))

def current_player(turn):
	if turn % 2 == 0:
		return 0
	else:
		return 1

def placement(grid, column, piece):
	for i in range(len(grid)-1, -1, -1):
		if grid[i][column] == " ":
		 grid[i][column] = piece
		 return grid

def check_end(grid):
	free = 0
	for row in grid:
		for cell in row:
			if cell == " ":
				free += 1
	if free == 0:
		return True
	else:
		return False


def check_horizontal_connect(grid):
	horizontal = []
	for i, row in enumerate(grid):
		for j, cell in enumerate(row):
			if cell != " ": 
				if horizontal == []:
					horizontal.append(cell)
				else:
					if cell in horizontal:
						horizontal.append(cell)
					else:
						horizontal = []
						horizontal.append(cell)
			else:
				continue
			if len(horizontal) == 4:
				return True
		horizontal = []
	return False


def check_vertical_connect(grid):
	vertical = []
	count = 0
	for i, row in enumerate(grid):
		for j, cell in enumerate(row):
			if j == count and cell != " ":
				if vertical == []:
					vertical.append(cell)
				else:
					if cell in vertical:
						vertical.append(cell)
					else:
						vertical = []
						vertical.append(cell)
			else:
				continue
			if len(vertical) == 4:
				return True
		vertical = []
		#count += 1		
	return False


def check_vertical_connect1(grid):
	vertical = []
	count = 0
	for i in range(10):
		for j, row in enumerate(grid):
			cell = row[count]
			if j == count and cell != " ":
				if vertical == []:
					vertical.append(cell)
				else:
					if cell in vertical:
						vertical.append(cell)
					else:
						vertical = []
						vertical.append(cell)
			else:
				continue
			if len(vertical) == 4:
				return True
		vertical = []
		count += 1
	return False




play = True
turn = 0
pieces = ["R", "B"]
grid = create_grid()
display_grid(grid)

while play:
	x = current_player(turn)
	current_pieces = pieces[x]
	if x == 0:
		print("Red player turn")
	else:
		print("Blue player turn")

	move = int(input("Enter column number: "))
	if move not in range(0, 10):
		print("There is no column " + str(move))
		move = int(input("Enter column number: "))
	print("OK - placing in column " + str(move))
	grid = placement(grid, move, current_pieces)
	display_grid(grid)
	
	turn += 1
	game = check_vertical_connect1(grid)
	print("game result = " + str(game))
	end = check_end(grid)
	if end:
		print("it's a tie!!")
		break




