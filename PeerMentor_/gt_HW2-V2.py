# gt_HW2.py

# Blackjack!
# Input: 'h' to hold, 'd' to draw
# Output: player score, dealer score
# These modules below were compiled to simulate a more accurate blackjack game
# They do not pertain to the assignment specifications, however if you wish for a more
# accurate playing of blackjack using python within your means to code here it is.

# By Gentry Trimble
import random

def Initialize_Deck():
    deck = []
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    for suit in suits:
        for i,rank in enumerate(cards):
            card = [suit,rank,values[i]]
            deck.append(card)
    return deck

global deck
def PrintHand(hand):
    str = '| '
    for i,card in enumerate(hand):
        str_ = f'{hand[i][1]} of {hand[i][0]}'
        str += str_ + ' | '
    print(str)

def CasinoPlay(player_score,pcards,deck):

    for i in range(2):
        player_cards, player_card = getCard(pcards, deck)
        if player_cards[i][2] == 11:
            ace = input("You've got an ace! Would you like it to be a 1 or an 11 ?")
            if ace == '1':
                player_cards[i][2] == 1
            else:
                player_cards[i][2] == 11
        player_score += player_cards[i][2]
    print('Cards originally dealt: ')
    PrintHand(player_cards)
    return player_cards,player_score

def getCard(cards,deck):
    card = random.choice(deck)
    cards.append(card)
    deck.remove(card)
    return cards,card


def collect_scores(pwin,dwin,pscore,dscore):
    if pwin == True:
        pscore +=1
    if dwin == True:
        dscore +=1
    return pscore,dscore

def checkWin(player_score, dealer_score):
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

def FinalDisplay(player_cards,dealer_cards):
    print('\nFinal Dealer CPU Cards: ')
    PrintHand(dealer_cards)
    print('Final Player Cards: ')
    PrintHand(player_cards)


def blackjack(carddeck):
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0
    while dealer_score <= 16:
        dealer_cards, dealer_card = getCard(dealer_cards,carddeck)
        dealer_score += dealer_card[2]
    print("Welcome to the Blackjack table,\n here's your hand.")

    print("Drawing Cards....\n")
    player_cards, player_score = CasinoPlay(player_score, player_cards, carddeck)

    while player_score < 21:
        if player_score < 21:
            draw = input(f"Your current score is {player_score} would you like to hold or draw? : ")
            if draw[0].lower() == 'd':
                player_cards,player_card = getCard(player_cards,carddeck)
                if player_card[2] == 11:
                    ace = input("You've got an ace! Would you like it to be a 1 or an 11?")
                    if ace == "1":
                        player_card[2] = 1
                    else:
                        player_card[2] = 11

                player_score += player_card[2]
                PrintHand(player_cards)
            else: break
    FinalDisplay(player_cards, dealer_cards)
    print(f'Final Score for this round:\nPlayer Score: {player_score}\nDealer Score: {dealer_score} ')
    pwin, dwin = checkWin(player_score,dealer_score)

    return pwin, dwin


def main():
    carddeck = Initialize_Deck()
    pscore = 0
    dscore = 0
    repeat = 'y'
    while repeat.lower() =='y':
        pwin,dwin = blackjack(carddeck)
        pscore,dscore = collect_scores(pwin,dwin,pscore,dscore)
        print(f'\nPlayer Score: {pscore}\nComputer Score: {dscore} ')
        repeat = input("Play again? (y/n): ")
    print('\nThanks for playing!')
main()













