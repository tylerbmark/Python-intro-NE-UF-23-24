# gt_HW2.py

# Blackjack!
# Inputs: 'h' to hold and 'd' to draw
# Outputs: player score, dealer score


# By Gentry Trimble
import random

def Initialize_Deck():
    deck = []
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    for suit in suits:
        for i,rank in enumerate(cards):
            card = [suit,rank,values[i]]
            deck.append(card)
    return deck


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
def PrintCurrentScore(hand):
    score = 0
    for i in range(len(hand)):
        score += hand[i][2]
    print(f"Your new hand is {score}")


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
        elif dealer_score > 21:
            print("You win this round!")
            playerwin = True

    return playerwin, dealerwin

def blackjack(carddeck):
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0
    while dealer_score <= 16:
        dealer_cards, dealer_card = getCard(dealer_cards,carddeck)
        dealer_score += dealer_card[2]
    print("Drawing Cards....")
    while player_score < 21:
        player_cards,player_card = getCard(player_cards,carddeck)
        print(f'You drew a {player_card[1]}!')
        if player_card[2] == 11:
            ace = input("You've got an ace! Would you like it to be a 1 or an 11?")
            if ace == "1":
                player_card[2] = 1
            else:
                player_card[2] = 11
        player_score += player_card[2]
        if player_score < 21:
            PrintCurrentScore(player_cards)
            draw = input('Draw again ? (y/n): ')
            if draw[0].lower() == 'y':
                print('Drawing card...')
                continue
            else: break
        else: break
    print(f'Scores:\nPlayer Score: {player_score}\nDealer Score: {dealer_score} ')
    pwin, dwin = checkWin(player_score,dealer_score)

    return pwin, dwin


def main():
    carddeck = Initialize_Deck()
    print("Welcome to Blackjack!")
    pscore = 0
    dscore = 0
    repeat = 'y'
    while repeat.lower() =='y':
        pwin,dwin = blackjack(carddeck)
        pscore,dscore = collect_scores(pwin,dwin,pscore,dscore)
        print(f'\nPlayer Score: {pscore}\nComputer Score: {dscore} ')
        repeat = input("Play again? (y/n): ")
    print('\nThanks for playing!')









