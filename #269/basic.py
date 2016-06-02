#------------------------------------------------------------
# Challenge #269: "BASIC Formatting"
# Difficulty: Easy
# May 31, 2016
# Brandon Newbright
#------------------------------------------------------------
def parse(code):
  count, indent, *lines = code.splitlines()

  level = 0
  linestack = []
  for l in lines:
    l = l.lstrip(" ·»")
    if l.startswith('ENDIF') or l.startswith('NEXT'):
        level -= 1
    print(indent*level + l)
    if l.startswith('IF') or l.startswith('FOR'):
        level += 1

str1 = '''12
····
VAR I
·FOR I=1 TO 31
»»»»IF !(I MOD 3) THEN
··PRINT "FIZZ"
··»»ENDIF
»»»»····IF !(I MOD 5) THEN
»»»»··PRINT "BUZZ"
··»»»»»»ENDIF
»»»»IF (I MOD 3) && (I MOD 5) THEN
······PRINT "FIZZBUZZ"
··»»ENDIF
»»»»·NEXT'''

parse(str1)