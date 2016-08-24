import re

def nameCheck(name, abbr):
  searchString = (abbr[0] + ".*" + abbr[1]).lower()
  containsAbbr = bool(re.search(searchString, name.lower()))
  print(name + ", " + abbr + " -> " + str(containsAbbr))

elements = [("Spenglerium", "Ee"), ("Zeddemorium", "Zr"), ("Venkmine", "Kn"), ("Stantzon", "Zt"), ("Melintzum", "Nm"), ("Tullium", "Ty")]

for e in elements:
  nameCheck(e[0], e[1])
