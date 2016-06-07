#------------------------------------------------------------
# Challenge #227: "Adjacency Matrix"
# Difficulty: Hard
# August 14, 2015
# Brandon Newbright
#------------------------------------------------------------

filein = open("input1.txt")
lines, *graph = filein.read().splitlines()

visits = [[False] * len(line) for line in graph]

def visited(x,y):
  global visits
  return visited[y][x]

def visit(x,y):
  global visits
  visits[y][x] = True
