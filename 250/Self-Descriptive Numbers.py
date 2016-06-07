def main(i):

  numberOfDigits = i
  searchMin = pow(10, numberOfDigits - 1)
  searchMax = int(str(i - 1) * i) + 1

  found = False

  for n in range(searchMin, searchMax):

    digitSum = sum(map(int, str(n)))
    weightedSum = sum(int(digit) * index for index, digit in enumerate(str(n)))

    if digitSum != i and weightedSum != i:
      continue

    checkList = [""] * i

    for j in range(i):
      k = str(n).split(str(j))
      checkList[j] = str(len(k) - 1)
      if checkList[j] != str(n)[j]:
        break

    if "".join(checkList) == str(n):
      print(str(n) + " is self-descriptive.")
      found = True

  if found == False:
    print("No self-descriptive numbers of " + str(numberOfDigits) + " digits found.")

main(3)
main(4)
main(5)
main(6)