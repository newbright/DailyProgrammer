#------------------------------------------------------------
# Challenge #271: "Critical Hit!"
# Difficulty: Easy
# June 13, 2016
# Brandon Newbright
#------------------------------------------------------------

def crit(d, h):
  ## If more health is left than sides on our die...
  if h > d:
    ## Find the odds of rolling d, and recursively check the chance of rolling d again
    return crit(d, (h - d)) / d
  else:
    ## Otherwise, check what rolls are greater than or equal to the new h
    return ((d + 1 - h) / d)

print(crit(4, 1))
print(crit(4, 4))
print(crit(4, 5))
print(crit(4, 6))
print(crit(1, 10))
print(crit(100, 200))
print(crit(8, 20))