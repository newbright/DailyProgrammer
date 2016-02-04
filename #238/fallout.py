#------------------------------------------------------------
# Challenge #238: "Fallout Hacking Game"
# Difficulty: Intermediate
# October 28, 2015
# Brandon Newbright
#------------------------------------------------------------

def get_words(d):

def check_guess(g, ans):

def game():
  print("Choose a dificulty (1-5):")
  diff = input()
  ans, bank = get_words(diff)

  print(bank)

  tries = 5

  while tries > 0:
    print("Your guess? (%d remaining):" % (tries - 1))
    guess = input()
    num = check_guess(guess, ans)
    print("%d/%d correct" % num, len(ans))
    if num == len(ans):
      print("You win!")
      break

game()