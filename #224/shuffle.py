#------------------------------------------------------------
# Challenge #224: "Shuffling A List"
# Difficulty: Easy
# July 20, 2015
# Brandon Newbright
#------------------------------------------------------------

from itertools import zip_longest
from random import *

def faro(li, it):
  mid = int(len(li)/2)
  for i in range(it):
    s = []
    for (a, b) in zip_longest(li[0:mid], li[mid:]):
      s.append(b)
      s.append(a)
    li = s
    print([n for n in s if n is not None])
  return [n for n in s if n is not None]

def fisher_yates(li):
  for i, n in reversed(list(enumerate(li))):
    j = randint(0, i)
    li[i], li[j] = li[j], li[i]
  return li


li = list(range(1,6))

print("Original list: {}".format(li))
print()
print("Faro Shuffle (first 3 iterations):")

faro(li, 3)

print()

li = list(range(1,6))

print("Fisher-Yates Shuffle (3 iterations):")
print(fisher_yates(li))
print(fisher_yates(li))
print(fisher_yates(li))