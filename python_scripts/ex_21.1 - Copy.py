import os
import time

maze1 = [
		['#','#',' ','#',' ','S'],
		[' ',' ',' ',' ','#',' '],
		[' ',' ','#',' ',' ',' '],
		[' ',' ',' ','#',' ',' '],
		[' ','#',' ','#','#','#'],
		['E','#',' ',' ',' ',' ']
		]

maze2 = [
		['S','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' '],
		[' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#','#'],
		[' ','#',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' '],
		[' ','#',' ','#',' ','#',' ','#',' ','#','#','#','#','#','#','#',' '],
		[' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ',' ',' ',' ',' '],
		[' ','#','#','#',' ','#',' ','#',' ','#',' ',' ',' ','#','#','#',' '],
		[' ',' ',' ',' ',' ','#',' ','#',' ','#',' ','#',' ',' ',' ','#',' '],
		['#','#',' ','#',' ','#',' ','#',' ','#',' ','#','#','#','#','#',' '],
		[' ',' ',' ','#',' ','#',' ','#',' ','#',' ',' ',' ','#',' ','#',' '],
		['#','#','#','#','#','#','#','#',' ','#','#','#','#','#',' ','#','#'],
		[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		['#','#','#','#','#','#',' ','#','#','#','#','#','#','#','#','#','#'],
		[' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' '],
		['#','#',' ',' ',' ','#',' ','#','#',' ','#','#','#','#',' ','#',' '],
		[' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#','#'],
		['E','#',' ','#',' ','#','#','#','#','#','#','#',' ','#',' ',' ',' ']
		]

maze3 = [
		['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','S','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
		['#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#'],
		['#',' ','#',' ','#',' ','#','#','#','#','#',' ','#',' ','#','#','#',' ','#',' ','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#'],
		['#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#'],
		['#',' ','#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#','#','#','#','#',' ','#',' ','#','#','#','#','#',' ','#',' ','#',' ','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' ','#','#','#',' ','#','#','#',' ','#'],
		['#',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#'],
		['#',' ','#','#','#',' ','#','#','#','#','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#','#','#',' ','#'],
		['#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#'],
		['#',' ','#',' ','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#','#','#','#','#','#','#','#','#',' ','#','#','#','#','#',' ','#',' ','#',' ','#',' ','#',' ','#','#','#','#','#','#','#',' ','#',' ','#','#','#'],
		['#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#'],
		['#','#','#',' ','#','#','#','#','#','#','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#',' ','#'],
		['#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#'],
		['#',' ','#','#','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#','#','#',' ','#'],
		['#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#'],
		['#','#','#',' ','#','#','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#','#','#',' ','#',' ','#','#','#',' ','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#',' ','#','#','#','#','#'],
		['#',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ','#'],
		['#',' ','#','#','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#','#','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#','#','#','#','#',' ','#',' ','#'],
		['#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#'],
		['#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#'],
		['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#'],
		['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','E','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
		]

def print_maze(maze):
	num_rows = len(maze)
	num_cols = len(maze[0])
	os.system('clear')
	for row in range(num_rows):
		for col in range(num_cols):
			print(maze[row][col], end = ' ')
		print()
	time.sleep(0.2)

# [North East South West]
neighbours=[[-1,0], [0,1], [1,0], [0,-1]]

def solve_maze(m, r, c):

	# 1. Base case #1: cell outside maze boundaries -> return False
	if r not in range(len(m)) or c not in range(len(m[0])):
		return False

	# 2. Base case #2: cell already visited OR wall -> return False
	if m[r][c] == "#" or m[r][c] == ".":
		return False

	# 3. Base case #3: found exit (E) -> return True
	if m[r][c] == "E":
		return True

	# 4. Move on and leave breadcrumb to avoid ping pong effect
	m[r][c] = "."
	print_maze(m)

	# 5. Call function recursively for all neighbors
	for n in neighbours:
		if solve_maze(m, r+n[0], c+n[1]) == True:
			return True

	# 6. If none of the neighbors lead anywhere, reset cell
	m[r][c] = " "
	print_maze(m)
	return False

solve_maze(maze3, 0, maze3[0].index("S"))












