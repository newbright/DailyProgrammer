#------------------------------------------------------------
# Challenge #228: "Letters In Alphabetical Order"
# Difficulty: Easy
# August 17, 2015
# Brandon Newbright
#------------------------------------------------------------

def order(w):
  if w == "".join(sorted(w)):
    print("{} - IN ORDER".format(w))
  elif w == "".join(reversed(sorted(w))):
    print("{} - REVERSE ORDER".format(w))
  else:
    print("{} - NOT IN ORDER".format(w))

for n in open("input.txt").read().split():
  order(n)