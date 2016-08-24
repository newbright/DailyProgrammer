import re

# 'fingers' is a string of five binary numbers
def check(fingers):
  return re.search(".*10+1.*", fingers)

def fingers(fingerString):
  left, right = fingerString[:5], fingerString[5:]

  if not check(left) and not check(right):
    leftSum = 10 * (left[:4].count("1")) + 50 * (int(left[4]))
    rightSum = right[1:].count("1") + 5 * int(right[0])
    print(fingerString + " -> " + str(leftSum + rightSum))
  else:
    print(fingerString + " -> Invalid.")


fingers("0111011100")
fingers("1010010000")
fingers("0011101110")
fingers("0000110000")
fingers("1111110001")
