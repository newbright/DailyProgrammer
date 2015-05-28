import random

#Card class. Constructs cards and translates their information.
class Card:

    #Dictionary for non-integer card values.
    #Based on this convention, index 0 corresponds to a card value of 2, index 1 to a card value of 3, and so on.
    stringValues = {
        9: "Jack",
        10: "Queen",
        11: "King",
        12: "Ace"
    }
    
    #Dictionary to handle suits as integers.
    stringSuits = {
        0: "Clubs",
        1: "Diamonds",
        2: "Hearts",
        3: "Spades"
    }
    
    #Creates a card given its number and suit.
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    #Translates a card object into a string.
    def toString(self):
        #If the value's "index" is greater than 9, it is a face card and we determine its value via the dictionary.
        if self.value > 8:
            valueStr = Card.stringValues.get(self.value)
        #Otherwise, translate the "index" into the appropriate numbered face card.
        else:
            valueStr = str(self.value + 2)
        
        return valueStr + " of " + Card.stringSuits.get(self.suit)

#Deck class. Holds card values in the deck and handles basic deck operations.
class Deck:
    #Builds a standard 52-card deck of Cards.
    def __init__(self):
        self.deck = []
        for x in range(13):
            for y in range(4):
                self.deck.append(Card(x, y))
    
    #Because Deck is constructed in a predictable order, it must later be shuffled.
    def shuffle(self):
        random.shuffle(self.deck)
    
    #Removes n card(s) from the Deck, returning the Card(s) in a list.
    def dealCards(self, n):
        cards = []
        for x in range(n):
            cards.append(self.deck.pop(0))
        return cards

#Hand class. Holds Card values in a "hand" list and allows for basic operations.
class Hand:
    #Initializes Hand an empty list of cards.
    def __init__(self):
        self.cards = []
    
    #Adds a single Card or list of Cards to a Hand.
    def addCards(self, addedCards):
        self.cards = self.cards + addedCards
        
    def printHand(self):
        for card in self.cards:
            print(card.toString())

#Player class. Holds basic player information and logic to determine hand rank.
class Player:
    #Global list of "community cards" corresponding to the flop, turn, and river.
    communityCards = []

    #Initializes Player with a name, fold status, and a new hand later populated from the Deck.
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.folded = False
    
    #TODO: Implement handRank method to evaluate rank of hand.
        
#TODO: Implement CPUPlayer subclass to control AI.

        
def main():
    print("Welcome to Texas Hold 'Em!")
    print("")
    print("How many players? (Enter a number 2-8.)")
    
    #Accepts 2-8 Players: The user, and 1-7 CPU Players.
    numberOfPlayers = int(input("Players: "))
    #Initialize list of Players
    players = [Player("Player")]
    #Add CPU Players to list
    for n in range(numberOfPlayers - 1):
        players.append(Player("CPU " + str(n)))
    
    print("")
    print(str(numberOfPlayers) + " players, got it. Shuffling the deck...")
    
    #Create standard 52-card Deck
    myDeck = Deck()
    #Deck is initially in a predictable order, so we shuffle it!
    myDeck.shuffle()
    
    print("")
    print("Dealing hands...")
    print("")
    
    #Loop through the player list
    for p in players:
        #Deal 2 cards to each player
        p.hand.addCards(myDeck.dealCards(2))
        #Display each player's hand
        print(p.name + "'s hand:")
        p.hand.printHand()
        print("")
    
    #There is no way the folded() property can be True at this point, but we still check for the sake of convention.
    if !players["Player"].folded():    
        print("Will you fold?")
        #TODO: Clean up this input.
        foldChoice = str(input("(y/n): "))
            if foldchoice == "y":
                players["Player"].folded() = True
    
    print("")    
    print("Here's the flop...")
    
    flop = myDeck.dealCards(3)
    for card in flop:
        #Update the community card list available to all Players
        Player.communityCards.append(card)
        #Display the card
        print(card.toString())
        
    #We only prompt the player to fold if they have not yet done so.
    if !players["Player"].folded():    
        print("Will you fold?")
        #TODO: Clean up this input.
        foldChoice = str(input("(y/n): "))
            if foldchoice == "y":
                players["Player"].folded() = True
    
    print("")
    print("Here's the turn...")

    turn = myDeck.dealCards(1)
    for card in turn:
        #Update the community card list available to all Players
        Player.communityCards.append(card)
        #Display the card
        print(card.toString())
        
    #We only prompt the player to fold if they have not yet done so.
    if !players["Player"].folded():    
        print("Will you fold?")
        #TODO: Clean up this input.
        foldChoice = str(input("(y/n): "))
            if foldchoice == "y":
                players["Player"].folded() = True
        
    print("")
    print("And here's the river.")

    river = myDeck.dealCards(1)
    for card in river:
        #Update the community card list available to all Players
        Player.communityCards.append(card)
        #Display the card
        print(card.toString())
    
if __name__ == "__main__":
    main()





