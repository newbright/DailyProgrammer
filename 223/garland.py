#------------------------------------------------------------
# Challenge #223: "Garland Words"
# Difficulty: Easy
# July 13, 2015
# Brandon Newbright
#------------------------------------------------------------

def garland(word):
  degree = 0
  for i in range(len(word)):
    if word[:i] == word[-i:]:
      degree = max(degree, i)
  return degree

def chain(word, reps):
  result = word + (word[garland(word):] * reps)
  return result

words = ["programmer", "ceramic", "onion", "alfalfa"]

for w in words:
  print("\"{}\" has a Garland degree of {}.".format(w, garland(w)))
  if garland(w) > 0:
    print(chain(w, 3))
  print()