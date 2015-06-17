#------------------------------------------------------------
# Challenge #217: "Lumberjack Pile Problem"
# Difficulty: Easy
# June 1, 2015
# Brandon Newbright
#------------------------------------------------------------

# Loop to read from each input file, excluding the challenge input ("input5.txt")
for i in range(1, 5):
	# Reads every number from the input file
	data = [int(n) for n in open("input" + str(i) + ".txt").read().split()]

	# The first two numbers are the side length 'n' of the square array of piles and the number of logs to be placed 'logs'
	n, logs = data[0], data[1]

	# The remaining values represent the piles' heights in the pile array
	piles = data[2:]
	
	# We neatly print the input values
	print("----INPUT " + str(i) + "----")
	print("We have {} logs to stack in this {} x {} array:\n".format(logs, n, n))
	for j in range(0, n*n, n):
		print(*piles[j:j+n])
	print("")

	# We find the smallest pile in the array to start
	smallest = min(piles)

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


