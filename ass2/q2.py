#!/usr/bin/python3
def main():
	# TESTING
	print(q1())

def q1():
	import math

	def f(x):
		return 4 + (12*x) + (25*pow(x, 2)) + (24*pow(x, 3)) + (16*pow(x,4))


	def q(x):
		return 1 + 2*x + 3*pow(x, 2)

	return [f(i) for i in range(-2,3)], [q(i) for i in range(-2,3)]


if __name__ == '__main__':
	main()