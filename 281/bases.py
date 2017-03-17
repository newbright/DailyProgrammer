def bases(x):
  xBase = int("0123456789abcdef".find(max(str(x))) + 1)
  print("Input : " + str(x))
  for y in range(17 - xBase):
    z = y + xBase
    print("base {} => {}".format(z, int(x, z)))

inputs = ["1", "21", "ab3", "ff"]
for i in inputs:
  bases(i)
  print("")
