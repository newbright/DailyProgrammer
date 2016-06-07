#------------------------------------------------------------
# Challenge #270: "Transpose The Input Text"
# Difficulty: Easy
# June 6, 2016
# Brandon Newbright
#------------------------------------------------------------
from itertools import zip_longest

## Transposes a string 's'
def transpose(s):
  ## We represent the string as a list of lines...
  lines = []
  for l in s.splitlines():
    ## ...and make each line list of characters
    lines.append(list(l))

  ## zip_longest() iterates over all these character lists
  ## simultaneously, and appends them by index. If we try to access an
  ## index greater than the length of a given line, the fillvalue (a
  ## space) is used instead.
  for c in list(zip_longest(*lines, fillvalue=' ')):
    ## We now have a list of tuples of characters. Each tuple
    ## contains the characters at a given index in every line of the
    ## input string.
    print(''.join(c))

str1 = '''Some
text.'''

str2 = '''package main

import "fmt"

func main() {
    queue := make(chan string, 2)
    queue <- "one"
    queue <- "twoO"
    close(queue)
    for elem := range queue {
        fmt.Println(elem)
    }
}'''

transpose(str1)
transpose(str2)