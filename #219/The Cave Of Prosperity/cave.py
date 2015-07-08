#------------------------------------------------------------
# Challenge #219: "The Cave Of Prosperity"
# Difficulty: Hard
# June 19, 2015
# Brandon Newbright
#------------------------------------------------------------

from decimal import Decimal

def knapsack(filename):
	# Reads every number from the input file
	data = [n for n in open(filename).read().split()]

	# The first two numbers are the knapsack capacity 'W' and the number of gold nuggets 'n'
	W, n = data[0], data[1]

	# The remaining values represent the weights 'w' of the nuggets
	w = data[2:]

	s = [0]

	for i in range(W):
		x = w[i]
		t = []
		for j in range(len(s)):
			y = s[j]
			t.append(x + y)
			u = sorted(union(s,t))


	# Loop until we are out of logs to place
	while logs > 0:
		# Rather than scan through the entire array for every log placed, we cast the array to a dictionary and loop through that
		for index, pile in enumerate(piles):
			# If the number of logs in the pile matches the smallest pile's height...
			if pile == smallest:
				# ...We add one log to it...
				piles[index] += 1
				# ...And remove that log from our input pile.
				logs -= 1
				# We stop looping through the dictionary when we are out of logs to place
				if logs == 0:
					break
		# If we've scanned through the entire dictionary and still have logs to place, we've added to every pile that had the smallest height, so we set the new smallest height
		smallest += 1


	# Finally, we print the piles array neatly
	print("The sorted piles look like this:\n")
	for k in range(0, n*n, n):
		print(*piles[k:k+n])
	print("\nThe smallest pile is now {}.\n".format(min(piles)))
