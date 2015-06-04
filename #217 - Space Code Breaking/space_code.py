#------------------------------------------------------------
# Challenge #217: "Space Code Breaking"
# Difficulty: Intermediate
# June 3, 2014
# Brandon Newbright
#------------------------------------------------------------

def decode_Omicron(message):
	result = ""
	# Convert each line into a list and scan through its integer values 
	char_list = message.strip('"').split()
	for c in char_list:
		# Convert each character to its integer form, and invert the fifth bit using an XOR operator
		converted = int(c) ^ 0b10000
		# Append the ASCII representation of the converted byte to the result string
		result += chr(converted)
	return result

def decode_Hoth(message):
	result = ""
	# Convert each line into a list and scan through its integer values 
	char_list = message.strip('"').split()
	for c in char_list:
		# Convert each character to its integer form, and add 10 to its value
		converted = int(c) - 10
		# Append the ASCII representation of the converted integer to the result string
		result += chr(converted)
	return result

def decode_Ryza(message):
	result = ""
	# Convert each line into a list and scan through its integer values 
	char_list = message.strip('"').split()
	for c in char_list:
		# Convert each character to its integer form, and subtract 1 from its value
		converted = int(c) + 1
		# Append the ASCII representation of the converted integer to the result string
		result += chr(converted)
	return result

def decode_Htrae(message):
	result = ""
	# Convert each line into a list and scan through its integer values 
	char_list = message.strip('"').split()
	for c in reversed(char_list):
		# Append the ASCII representation of the integer to the result string
		result += chr(int(c))
	return result

def score_line(message):
	points = 0
	for c in message:
		# Award a "point" to a line if it contains alphanumeric characters
		if c.isalpha() or c.isdigit():
			points += 1
		# Award more "points" for spaces
		elif c.isspace():
			points += 2
	# Return the average point value for each character.
	return points

def main():

	planets = ["Omicron V", "Hoth", "Ryza IV", "Htrae"]

	code_lines = open("input/input.txt").read().splitlines()

	for line in code_lines:

		print "INPUT - " + line
		print ""
		# Create dictionaries to store each score and decoded line with its respective planet
		scores_dict, decoded_dict = dict.fromkeys(planets), dict.fromkeys(planets)

		# Decode and score the line with each language
		decoded_dict["Omicron V"] = decode_Omicron(line)
		scores_dict["Omicron V"] = score_line(decoded_dict["Omicron V"])

		decoded_dict["Hoth"] = decode_Hoth(line)
		scores_dict["Hoth"] = score_line(decoded_dict["Hoth"])

		decoded_dict["Ryza IV"] = decode_Ryza(line)
		scores_dict["Ryza IV"] = score_line(decoded_dict["Ryza IV"])

		decoded_dict["Htrae"] = decode_Htrae(line)
		scores_dict["Htrae"] = score_line(decoded_dict["Htrae"])

		# Print the corresponding decoded output and that output's score for each language
		print "{}: {} (score: {})".format(planets[0], decoded_dict[planets[0]], scores_dict[planets[0]])
		print "{}: {} (score: {})".format(planets[1], decoded_dict[planets[1]], scores_dict[planets[1]])
		print "{}: {} (score: {})".format(planets[2], decoded_dict[planets[2]], scores_dict[planets[2]])
		print "{}: {} (score: {})".format(planets[3], decoded_dict[planets[3]], scores_dict[planets[3]])
		print ""

		# Print the decoded line with the highest score
		max_planet = max(scores_dict, key=scores_dict.get)
		print "--BEST CHOICE--"
		print "{}: {} (score: {})".format(max_planet, decoded_dict[max_planet], scores_dict[max_planet])
		print ""
		print ""

if __name__ == "__main__":
	main()