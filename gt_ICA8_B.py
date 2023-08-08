# gt_ICA8_B.py
# Object oriented program that creates deck of cards, shuffles them,
# and deals the specified number to player
# INPUT: number of cards to draw
# OUTPUT: cards drawn from deck, and cards left
# by Gentry Trimble

import random
class Card:
    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank
    def getStr(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.deck = []
        self.deck = [Card(suit,rank) for rank in ranks for suit in suits]
        print(self.deck)
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self, num_cards):
        if num_cards > len(self.deck):
            print('Not enough cards in the deck.')
            return None
        return [self.deck.pop() for i in range(num_cards)]
# The next module CheckDeck() is purely optional for testing purposes only
def CheckDeck():
    deck = Deck()

    print("Full Deck: \n")
    for card in deck.deck:
        print(card.getStr())
# It is always good to have a function to check to ensure you have every value


def main():
    deck = Deck()
    deck.shuffle()
    print("Card Dealer\n\nI have shuffled a deck of 52 cards.\n")
    num = int(input("How many cards would you like ?: "))
    dealt = deck.deal(num)
    if dealt:
        print("\nHere are your cards:")
        for card in dealt:
            print(card.getStr())
    print(f"\nThere are {52-num} cards left in the deck.")
    print()
    print("Good luck!")
main()

