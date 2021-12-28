import random


class Room:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.dir = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
		random.shuffle(self.dir)
	
	def get_cur_pos(self):
		return self.x, self.y

	def get_next_pos(self):
		return self.dir.pop()


def make_maze(size):
	rooms = [[Room(x,y) for x in range(size)] for y in range(size)]
	maze = [['■' for _ in range(size*2+1)] for _ in range(size*2+1)]

	visited = []

	def make(cur_room):
		cx, cy = cur_room.get_cur_pos()
		visited.append((cx, cy))
		maze[cy*2+1][cx*2+1] = '□'
		while cur_room.dir:
			nx, ny = cur_room.get_next_pos()
			if 0 <= nx < size and 0 <= ny < size:
				if (nx, ny) not in visited:
					maze[cy + ny + 1][cx + nx + 1] = '□'
					make(rooms[ny][nx])

	make(rooms[0][0])

	return maze


def save_maze(maze, filename):
	with open(filename, 'w') as file:
		for y in range(len(maze)):
			for x in range(len(maze)):
				file.write(maze[y][x])
			file.write('\n')


maze = make_maze(15)
save_maze(maze, 'assets\maze.txt')