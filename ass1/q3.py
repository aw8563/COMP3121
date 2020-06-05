#!/usr/bin/python3
import random

def main():
	# TESTING

	print(q3().weight) #  should be


def q3():
	# apples with their own weights which we do not know
	class Apple:
		def __init__(self, weight):
			self.weight = weight
			self.previousWeighs = []


	# our 'scale' which returns heavier/ligher apple
	class Scale:
		def __init__(self):
			self.nUsed = 0

		# returns the (heavier, lighter) apple
		def weigh(self, apple1, apple2):
			self.nUsed += 1
			return (apple1, apple2) if apple1.weight > apple2.weight else (apple2, apple1)

	scale = Scale()
	apples = [Apple(i + 1) for i in range(1024)]
	random.shuffle(apples)

	# merge sort and only consider the larger half each time until we have 2 apples left
	while len(apples) > 2:
		remaining = []

		for i in range(1, len(apples), 2):
			# compare each pair
			apple1 = apples[i]
			apple2 = apples[i - 1]
			heavier, lighter = scale.weigh(apple1, apple2)

			# need to keep track of all comparisons in case we weigh heaviest with second heaviest	
			# we will check this at the end		
			remaining.append(heavier)
			heavier.previousWeighs.append(lighter)

		apples = remaining

	# most of the time this will be heaviest and second heaviest 
	heaviest, second = scale.weigh(apples[0], apples[1])

	# however, sometimes we get unlucky and compare heaviest and second heaviest
	# we need to go through all the comparisons with the heavier apple to make sure we didn't discard second heaviest
	for apple in heaviest.previousWeighs:
		second, _ = scale.weigh(second, apple)

	# make sure we use scale 1032 times
	assert(scale.nUsed <= 1032)

	# and we found the correct one
	assert(second.weight == 1023)

	return second

if __name__ == '__main__':
	main()