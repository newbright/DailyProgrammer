#------------------------------------------------------------
# Challenge #239: "A Game Of Threes"
# Difficulty: Easy
# November 2, 2015
# Brandon Newbright
#------------------------------------------------------------

def threes(x):
  while x != 1:
    if x % 3 == 0:
      print("%d 0" % x)
      x = x/3
    elif x % 3 == 1:
      print("%d -1" % x)
      x = (x-1)/3
    else:
      print("%d 1" % x)
      x = (x+1)/3

  print("%d" % x)

x = 100
y = 31337357

threes(x)
threes(y)