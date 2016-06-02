string = '''   \\\\  /\    
            \\
   /         
      \     \\
    \        
  /      /   
\  /      \  
     \       
\/           
/            
          \  
    \/       
   /       / 
TpnQSjdmZdpoohd'''

lines = string.splitlines()

grid = lines[:13]
word = lines[13]

def find_mirror(c):
  if ord(c) < ord('N'):
    row, col, direct = ord(c)-ord('A'), -1, [0,1]
  elif ord(c) < ord('a'):
    row, col, direct = 13, ord(c)-ord('N'), [-1,0]
  elif ord(c) < ord('n'):
    row, col, direct = -1, ord(c) - ord('a'), [1,0]
  else:
    row, col, direct = ord(c)-ord('n'), 13, [0,-1]

  while True:
    row, col = row + direct[0], col + direct[1]
    if 0 <= row <= 12 and 0 <= col <= 12:
      if grid[row][col] == '/':
        direct[0], direct[1] = -direct[1], -direct[0]
      elif grid[row][col] == '\\':
        direct[0], direct[1] = direct[1], direct[0]
    else:
      if col == -1:
        return chr( ord('A') + row )
      elif col == 13:
        return chr( ord('n') + row )
      elif row == -1:
        return chr( ord('a') + col)
      elif row == 13:
        return chr( ord('N') + col)

def solve(s):
  solved = ""
  for c in s:
    solved += find_mirror(c)
  print("The solved word is:")
  print(solved)

solve(word)