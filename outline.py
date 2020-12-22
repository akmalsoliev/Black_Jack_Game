#Blackjack game

# print('Hello and welcome to our Casino, you have chosen Blackjack Table')
# start = input("To start press any key")

#Step 0: Create a deck, give cards value 
from create_deck import deck_generator
from card_value_check import check_value

#Step 1: Draw cards

start = 1 
while start == 1:
    deck = deck_generator()
    players_cards = []
    dealers_cards = []
    players_value = 0
    dealers_value = 0
    counter = 0
    for number in range(0,4):
        print(deck[number])
        if number < 2:
            players_cards.append(number)
            players_value += check_value(deck[number])
        else:
            dealers_cards.append(number)
            dealers_value += check_value(deck[number])
        counter += 1
    
    print('You have {} and {}'.format(deck[players_cards[0]], deck[players_cards[1]]))
    print("Dearler's first card is {}, second is unknown.".format(deck[dealers_cards[0]]))
    
    # while dealers_value<= 21 or players_value<= 21:


    restart = input('Would you like to restart?')
    if restart.upper() != "YES":
        start = 0




#Step 2: Player's cards

#Step 3: Dealer's cards

#Step 4: Check if there is blackjack

#Step 4: pass or hit me - Player

#Step 5: Dealer hit me

#Step 6: Check the winner