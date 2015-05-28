import random

#Card class. Translate card information between data and recognizable values
class Card:

    stringValues = {
        10: "Jack",
        11: "Queen",
        12: "King",
        13: "Ace"
    }
    
    stringSuits = {
        0: "Clubs",
        1: "Diamonds",
        2: "Hearts",
        3: "Spades"
    }
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def toString(self):
        if self.value > 9:
            valueStr = Card.stringValues.get(self.value)
        else:
            valueStr = str(self.value + 1)
        
        return valueStr + " of " + Card.stringSuits.get(self.suit)

#Deck class. Holds card values in the deck and handles basic deck operations.
class Deck:
    def __init__(self):
        self.deck = []
        for x in range(13):
            for y in range(4):
                self.deck.append(Card(x + 1, y))
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def dealCards(self, n):
        cards = []
        for x in range(n):
            cards.append(self.deck.pop(0))
        return cards

#Hand class. Holds card values in a hand.
class Hand:
    def __init__(self):
        self.cards = []
 
    def addCards(self, addedCards):
        for card in addedCards:
            self.cards.append(card)
        
    def printHand(self):
        for card in self.cards:
            print(card.toString())

#Player class. Holds basic player information and logic to determine hand rank.
class Player:
    communityCards = []

    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.folded = False
        
    #Royal Flush > Straight Flush > 4oaK > Full House > Flush > Straight > 3oaK > 2 Pair > 1 Pair > High Card
    def evaluateHandRank(self, communityCards):
        cardPool = self.hand.cards + communityCards
        
        
        

# #CPUPlayer sub-class. Contains AI logic to evaluate the decision to fold.
# class CPUPlayer(Player):
    # def evaluateFold(self):
        
        
        
        

print("Welcome to Texas Hold 'Em!")

print("")

print("How many players? (Enter a number 2-8. pls no errorino)")

numberOfPlayers = int(input("Players: "))

players = [Player("Player")]

for n in range(numberOfPlayers - 1):
    players.append(Player("CPU " + str(n)))
    
print("")
print(str(numberOfPlayers) + " players, got it. Shuffling the deck...")

myDeck = Deck()
myDeck.shuffle()

print("")
print("Dealing hands...")

print("")    
for p in players:
    p.hand.addCards(myDeck.dealCards(2))
    print(p.name + "'s hand:")
    p.hand.printHand()
    print("")

print("")    
        
print("Here's the flop...")

flop = myDeck.dealCards(3)
for card in flop:
    Player.communityCards.append(card)
    print(card.toString())

print("")
print("Here's the turn...")

turn = myDeck.dealCards(1)
for card in turn:
    Player.communityCards.append(card)
    print(card.toString())

print("")
print("And here's the river.")

river = myDeck.dealCards(1)
for card in river:
    Player.communityCards.append(card)
    print(card.toString())
