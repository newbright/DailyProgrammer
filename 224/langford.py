#------------------------------------------------------------
# Challenge #224: "Langford Strings"
# Difficulty: Hard
# July 24, 2015
# Brandon Newbright
#------------------------------------------------------------

alph = "abcdefghijklmnopqrstuvwxyz"

# Generates the Langford string of order 'n' to list 'arr', where n == (4c || 4c - 1) for all c > 0
def langford(arr, n):

  # Breaks recursion when we've run out of letters to insert
  if n == 0:
    print(''.join(arr))
    return

  # Our loop is bounded by the fact that a character insertion at i happens at i + n + 1 as well
  for i in range(len(arr) - n - 1):

    # If an insertion is possible, we try it...
    if arr[i] == None and arr[i + n + 1] == None:
      arr[i] = alph[n - 1]
      arr[i + n + 1] = alph[n - 1]

      # ...And proceed trying with the next character, of degree n - 1
      langford(arr, n - 1)

      # If that wasn't successful, we 'reset' the pair of positions to 'None' before trying again
      arr[i] = None
      arr[i + n + 1] = None

for order in [3, 4, 7, 8]:
  arr = [None] * order * 2
  print("Langford Strings of order {}:".format(str(order)))
  langford(arr, order)
  print()
