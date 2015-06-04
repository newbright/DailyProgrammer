#------------------------------------------------------------
# Challenge #216: "Metaprogramming Madness!"
# Difficulty: Hard
# May 22, 2015
# Brandon Newbright
#------------------------------------------------------------

types_list = [1, 0, 1.0, 0.0, 'c', '', "Hello World!", "", [1, 2, 3], [], True, False]

for item in types_list:
	print str(item) + " : " + str(bool(item))