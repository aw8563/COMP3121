#!/usr/bin/python3
import random

def main():
	# TESTING

	grid = [[1,2,3,4,5,6,7,8] for i in range(8)]
	print("MAX TREES =", q4(grid))

	for row in grid:
		random.shuffle(row)
	print("MAX TREES =", q4(grid))

def q4(grid, squareSize=None):
	# process the entire grid first where sums[i][j] = sum of all trees from square between grid[0][0] and grid[i][j]
	# this is done in (4n)^2 time
	size = len(grid)
	sums = [[0 for i in range(size)] for j in range(size)]

	for i in range(size):
		for j in range(size):
			sums[i][j] = grid[i][j]

			if i > 0: # not first row, we add the upper rectangle
				sums[i][j] += sums[i - 1][j]

			if j > 0: # not first col, we add left rectangle
				sums[i][j] += sums[i][j - 1]


			# minus the middle overlap if there is one
			if i > 0 and j > 0:
				sums[i][j] -= sums[i - 1][j - 1]

	# Using sums[][] arr, we can loop through grid again in (4n)^2 time 
	# we can calculate the sum of each n//4 sized square in constant time
	# total runtime is n^2
	if not squareSize: 
		squareSize = size//4
	
	maxTrees = 0
	res = [[0 for i in range(size)] for j in range(size)] # debugging

	for i in range(squareSize - 1, size):
		for j in range(squareSize - 1, size):			
			total = sums[i][j]

			# trim off excess
			if i - squareSize >= 0: 
				total -= sums[i - squareSize][j]

			if j - squareSize >= 0:
				total -= sums[i][j - squareSize]

			# if we double minus the top corner square off, we need to add it back on
			if i - squareSize >= 0 and j - squareSize >= 0:
				total += sums[i - squareSize][j - squareSize]

			res[i][j] = total
			maxTrees = max(maxTrees, total)

	print('-------------')
	print("grid")
	for row in grid:
		for col in row:
			print(col, end = " ")
		print()

	print('-------------')
	print("result")
	for row in res:
		for col in row:
			print(col, end = " ")
		print()

	return maxTrees

if __name__ == '__main__':
	main()