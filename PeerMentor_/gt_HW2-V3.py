# Class based version of Blackjack
# more efficient

class Card:
    def __init__(self,suit,value,card_value):
        self.suit = suit
        self.value = value
        self.card_value = card_value

class Deck:
    def __init__(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.card_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
                            "Q": 10, "K": 10}
        self.deck_list = [Card(suit, value, self.card_values[value]) for value in cards for suit in suits]
def PrintHand(hand):
    str_ = "| "
    for card in hand:
       str_ += f'{card.value} of {card.suit}'
    print(str_)
class BlackjackGame:
    def __init__(self):
        self.carddeck = Deck()

    def CasinoPlay(self, player_score):
        player_cards = []
        for i in range(2):
            player_card = random.choice(self.carddeck.deck_list)
            player_cards.append(player_card)
            self.carddeck.deck_list.remove(player_card)
            if player_cards[i].card_value == 11:
                ace = input("You've got an ace! Would you like it to be a 1 or an 11?")
                if ace == "1":
                    player_cards[i].card_value = 1
                else:
                    player_cards[i].card_value = 11
            player_score += player_cards[i].card_value
        print("Cards originally dealt: ")
        PrintHand(player_cards)
        return player_cards, player_score

    def getCard(self, cards):
        card = random.choice(self.carddeck.deck_list)
        cards.append(card)
        self.carddeck.deck_list.remove(card)
        return cards, card

    def checkWin(self, player_score, dealer_score):
        playerwin = False
        dealerwin = False

        if player_score == 21:
            if player_score != dealer_score:
                print('Blackjack! You win!')
                playerwin = True
            elif player_score == dealer_score:
                print('Double Blackjack!')

        if dealer_score == 21:
            print('Blackjack! You lose!')
            dealerwin = True

        if player_score > 21:
            if dealer_score > 21:
                print("Bust! It's a draw!")
            else:
                print("Bust! You lose!")
                dealerwin = True

        if player_score < 21:
            if player_score > dealer_score:
                print("You win this round! Congrats ")
                playerwin = True
            elif player_score < dealer_score and dealer_score < 21:
                print("You lose!")
                dealerwin = True
            elif dealer_score >= 21:
                print("You win this round!")
                playerwin = True

        return playerwin, dealerwin

    def FinalDisplay(self, player_cards, dealer_cards):
        print('\nFinal Dealer CPU Cards: ')
        PrintHand(dealer_cards)
        print('Final Player Cards: ')
        PrintHand(player_cards)

    def collect(self, pwin, cwin, pscore, dscore):
        if pwin:
            pscore += 1
        if cwin:
            dscore += 1
        return pscore, dscore

