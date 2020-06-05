#!/usr/bin/python3
def main():
	# TESTING
	grid = [[1,2,3,4,5,6,7,8] for i in range(8)]
	print(q4(grid))



def q4(grid, squareSize=None):
	# process the grid first where sums[i][j] = sum of all trees from square between grid[0][0] and grid[i][j]
	# this is done in (4n)^2 time
	size = len(grid)
	sums = [[0 for i in range(size)] for j in range(size)]
	sums[0][0] = grid[0][0]

	for i in range(size):
		for j in range(size):
			if i == 0 and j == 0:
				continue

			if i == 0: # first row
				sums[i][j] = sums[i][j - 1] + grid[i][j]
				continue

			if j == 0:
				sums[i][j] = sums[i - 1][j] + grid[i][j]
				continue

			# otherwise we are in the middle
			sums[i][j] = sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1] + grid[i][j]

	# Using sums[][] arr, we can loop through grid again in (4n)^2 time and calculate the sum of each square in constant time
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

			# we double minus the top corner square off so we need to add it back on
			if i - squareSize >= 0 and j - squareSize >= 0:
				total += sums[i - squareSize][j - squareSize]

			res[i][j] = total
			maxTrees = max(maxTrees, total)

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