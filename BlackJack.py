import random
playerin = True
dealerin = True


# card deck / dealer hand
CardDeck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
dealerHand = []
playerHand = []


# Dealing of the cards
def cardDeal(turn):
    card = random.choice(CardDeck)
    turn.append(card)
    CardDeck.remove(card)


# calculating total of player and dealer hand
def total(turn):
    total = 0
    faceCards = ['J', 'Q', 'K']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in faceCards:
            total += 10
# Determines value of Ace card
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total
# evaluating the winner
def showDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

# Blackjack loop, range specifies cards in hand
for i in range(2):
    cardDeal(dealerHand)
    cardDeal(playerHand)

# Inputs for stay or hit
while playerin or dealerin:
    print(f"Dealer's hand is {showDealerHand()} and X")
    print(f"Your hand is{playerHand} for the total of {total(playerHand)}")
    if playerin:
        hitOrStay = input("1: Stay\n2: Hit\n")
    if total(dealerHand) > 17:
        dealerin = False
    else:
        cardDeal(dealerHand)
    if hitOrStay == '1':
        playerin = False
# determines the winner and loser
    else:
        cardDeal(playerHand)
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break
# blackjack results
if total(playerHand) == 21:
    print(f'\n BlackJack!!!, you have {playerHand} for a total of {total(playerHand)} and the dealer had {dealerHand} for a total of {total(dealerHand)}')
elif total(dealerHand) == 21:
    print(f'\n Dealer has BlackJack :( You Lose, you had {playerHand} for a total of {total(playerHand)} and the dealer had {dealerHand} for a total of {total(dealerHand)}')
elif total(playerHand) > 21:
    print(f'\n You Bust :( Dealer Wins, you have {playerHand} for a total of {total(playerHand)} and the dealer had {dealerHand} for a total of {total(dealerHand)}')
elif total(dealerHand) > 21:
    print(f'\n Dealer Busts! You Win!!, you have {playerHand} for a total of {total(playerHand)} and the dealer had {dealerHand} for a total of {total(dealerHand)}')
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f'\n You Lose, you have {playerHand} for a total of {total(playerHand)} and the dealer had {dealerHand} for a total of {total(dealerHand)}')
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f'\n You Win!!, you have {playerHand} for a total of {total(playerHand)} and the dealer had {dealerHand} for a total of {total(dealerHand)}')



