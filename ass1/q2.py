#!/usr/bin/python3
import random

def main():
	# TESTING

	nuts, bolts = q2(1000)
	for nut, bolt in zip(nuts, bolts):
		assert(nut.size == bolt.size)
		print(nut.size, bolt.size)

def q2(n):
	# our bolts and nuts with hidden sizes
	class Bolt:
		def __init__(self, size):
			self.size = size

	class Nut:
		def __init__(self, size):
			self.size = size

	# returns if a bolt fits a nut
	# We can only compare a nut and a bolt.
	def compare(nut, bolt):
		return nut.size - bolt.size

	# our quicksort algorithm
	def quickSort(nuts, bolts, left, right):
		if left >= right: # keep going until the subarray is empty
			return

		# since everything is shuffled, just take our pivot to be first in array
		target = bolts[left]

		# find the bolt and nut that matches at pivot and sort the rest
		pivot = move(nuts, left, right, target)
		pivot = move(bolts, left, right, target)

		# sort remaining subarrays
		quickSort(nuts, bolts, left, pivot - 1)
		quickSort(nuts, bolts, pivot + 1, right)


	# this will partition our array. 
	# Everything smaller than target goes to the left
	# Everything larger than target goes to right
	# Returns the index of where our match is so we can set our new left and right
	def move(arr, left, right, target):
		idx = left
		smaller = []
		larger = []

		for num in arr[left:right + 1]:
			if compare(num, target) < 0:
				smaller.append(num)

			if compare(num, target) > 0:
				larger.append(num)

		for num in smaller:
			arr[idx] = num
			idx += 1

		pivot = idx
		arr[idx] = target
		idx += 1

		for num in larger:
			arr[idx] = num
			idx += 1

		return pivot

	####################################################
	# initialise and randomise
	nuts = [Bolt(i + 1) for i in range(n)]
	bolts = [Nut(i + 1) for i in range(n)]
	random.shuffle(nuts)	
	random.shuffle(bolts)


	quickSort(nuts, bolts, 0, n - 1)
	return nuts, bolts

if __name__ == '__main__':
	main()