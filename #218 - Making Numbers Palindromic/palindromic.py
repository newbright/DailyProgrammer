#------------------------------------------------------------
# Challenge #218: "Making Numbers Palindromic"
# Difficulty: Easy
# June 8, 2015
# Brandon Newbright
#------------------------------------------------------------

from collections import defaultdict

def is_palindrome(n):
	return str(n) == str(n)[::-1]

def palindrome(n, on = 0, s = 0):
	if not on:
		on = n
	if is_palindrome(n):
		print("{} becomes palindromic after {} steps: {}".format(on, s, n))
	else:
		n += int(str(n)[::-1])
		palindrome(n, on, s+1)

def bonus_palindrome(n, d, on = 0, s = 0):
	if not on:
		on = n
	if is_palindrome(n):
		d[n].append(on)
	else:
		if s < 993:
			n += int(str(n)[::-1])
			bonus_palindrome(n, d, on, s+1)
		else:
			print("{} does not converge.".format(on))
			d["Lychel"].append(on)

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