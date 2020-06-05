#!/usr/bin/python3
def main():
	# TESTING

	# 1 + 64 = 16 + 49
	arr = [1,8,4,7]
	print(q1(arr))

	# 0 .. 7 has no such pairs
	arr = [i + 1 for i in range(7)]
	print(q1(arr))

def q1(arr):
	seen = {} # store square sums found so far

	# n^2 loop through array
	for i, num1 in enumerate(arr):
		for j, num2 in enumerate(arr[i + 1:]):
			total = num1*num1 + num2*num2
			
			if total in seen: # if we have previously made the sum, we have satisfied condition
				return True	

			seen[total] = (num1, num2)			
	
	return False

if __name__ == '__main__':
	main()