# given grid h = height, w = width
# point particle begins in upper left
# v = velocity theta = -pi/4 rad or -45 degrees

# Determine C, b, and t WHERE:
# C = corner in which particle will stop
# b = number of ricochets
# t = time for particle to reach 'C'


# initialize an array to describe the four possible directions of travel
DIRECTIONS = [ [1,-1] , [-1,-1] , [1,-1] , [1,1] ]

def ricochet(h, w, vel):
  # initialize the simulation time and number of ricochets at 0
  b, t = 0, 0

  # define the coordinates and names of the corners
  CORNERS = [ [w,0] , [0,0] , [0,h] , [w,h] ]
  NAMES = ["UR", "UL", "LL", "LR"]

  # initialize the position and vector of the ball in the UL corner
  pos = [0,0]
  C = "UL"
  v = [1,1]

  # MAIN LOOP
  while True:
    # print("Position: {}".format(pos))
    # print("Velocity: {}".format(v))
    # print("Ricochets: {}".format(b))
    # print("Time: {}".format(t))
    # print("")
    if pos in CORNERS and t != 0 :
      # print("Corner reached!")
      break
    # only process deflection if one direction is obstructed
    if bool(pos[0] % w) != bool(pos[1] % h):
      # process a ricochet along the x-axis
      if bool(pos[0] % w) == 0 :
        # print("Horizontal collision")
        v[0] *= -1

      # process a ricochet along the y-axis
      if bool(pos[1] % h) == 0 :
        # print("Vertical collision")
        v[1] *= -1

      # print("")
      b += 1
    # otherwise, velocity is preserved
    pos[0] += v[0]
    pos[1] += v[1]
    t += 1

  t = t/vel
  print("{} {} {}".format(NAMES[CORNERS.index(pos)], b, t))

ricochet(8,3,1)
ricochet(15,4,2)
