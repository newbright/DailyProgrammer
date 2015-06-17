#------------------------------------------------------------
# Challenge #218: "Making Numbers Palindromic"
# Difficulty: Easy
# June 8, 2015
# Brandon Newbright
#------------------------------------------------------------

from collections import defaultdict

# Simply checks whether the input 'n' (a string or integer) is palindromic
def is_palindrome(n):
	return str(n) == str(n)[::-1]

# Recursively checks if a number 'n' is palindromic, where 'on' passes the original number and 's' is the number of the step being performed.
def palindrome(n, on = 0, s = 0):
	if not on:
		on = n
	if is_palindrome(n):
		print("{} becomes palindromic after {} steps: {}".format(on, s, n))
	else:
		n += int(str(n)[::-1])
		palindrome(n, on, s+1)

# Similar to the above, but adds palindromes as keys to a dictionary whose values are the numbers used to obtain them.
# Also finds numbers whose palindromes do not converge after ~1000 steps (known as "Lychel Numbers").
def bonus_palindrome(n, d, on = 0, s = 0):
	if not on:
		on = n
	if is_palindrome(n):
		d[n].append(on)
	else:
		# Although the prompt calls for 1000 steps, Python does not allow recursion to that depth, so I've used 990.
		if s < 990:
			n += int(str(n)[::-1])
			bonus_palindrome(n, d, on, s+1)
		else:
			print("{} does not converge.".format(on))
			d["Lychel"].append(on)

# Simple function to print palindromes which can be obtained from multiple values.
def bonus():
	palindrome_dict = defaultdict(list)

	for n in range(1, 1001):
		bonus_palindrome(n, palindrome_dict)
	for key, values in palindrome_dict.items():
		if len(values) > 1:
			print("{} yielded by {} items: {}".format(key, len(values), ', '.join(map(str, values))))

palindrome(123)
palindrome(286)
palindrome(196196871)

bonus()