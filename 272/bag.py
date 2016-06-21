from collections import defaultdict
BAG_COUNT = {
  'A' : 9,
  'B' : 2,
  'C' : 2,
  'D' : 4,
  'E' : 12,
  'F' : 2,
  'G' : 3,
  'H' : 2,
  'I' : 9,
  'J' : 1,
  'K' : 1,
  'L' : 4,
  'M' : 2,
  'N' : 6,
  'O' : 8,
  'P' : 2,
  'Q' : 1,
  'R' : 6,
  'S' : 4,
  'T' : 6,
  'U' : 4,
  'V' : 2,
  'W' : 2,
  'X' : 1,
  'Y' : 2,
  'Z' : 1,
  '_' : 2
}

def tiles_left(s):
  bag = defaultdict(list)
  for k, v in BAG_COUNT.items():
    count = BAG_COUNT[k] - s.count(k)
    bag[count].append(k)
  if sum(c < 0 for c in bag):
    letters = sum([bag[c] for c in bag if c < 0], [])
    print("ERROR : Invalid input.")
    print("More {} have been taken from the bag than possible.".format('\'s, '.join(letters[:-1]) + '\'s and {}\'s'.format(leters[-1]) if len(letters) > 1 else letters[0] + '\'s'))
  else:
    print(''.join(['{}: {}\n'.format(k, ', '.join(sorted(v))) for k, v in sorted(bag.items(), reverse=True)]))

tiles_left('PQAREIOURSTHGWIOAE')
tiles_left('LQTOONOEFFJZT')
tiles_left('AXHDRUIOR_XHJZUQEE')
