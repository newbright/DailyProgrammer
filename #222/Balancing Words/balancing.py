def weight(char):
  letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  return letters.index(char) + 1


def score(segment):
  score = 0
  for i, c in enumerate(segment):
    score += weight(c) * (i + 1)
  return score

def balance(word):
  for i in range(1, len(word) - 1):

    left = word[0:i:]
    balance = word[i]
    right = word[i+1:len(word):]

    left_sum = score(reversed(left))
    right_sum = score(right)

    if (left_sum == right_sum):
      print("{} {} {} - {} points".format(left, balance, right, left_sum))
      return

  print("{} DOES NOT BALANCE".format(word))

balance("STEAD")
balance("CONSUBSTANTIATION")
balance("WRONGHEADED")
balance("UNINTELLIGIBILITY")
balance("SUPERGLUE")