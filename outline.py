#Blackjack game

# print('Hello and welcome to our Casino, you have chosen Blackjack Table')
# start = input("To start press any key")

#Step 0: Create a deck, give cards value 
from card_support import *
from card_value import *

def print_cards(whos_cards, input_list):
    print('-' *20)
    print(f'{whos_cards} cards are:')
    for index, _ in enumerate(input_list):
        print(deck[input_list[index]])


dealer_bust = False
player_bust = False
start = 1 

#Game start

while start == 1:

#Step 1: Deck Generation
    deck = deck_generator()
    players_cards = []
    dealers_cards = []
    players_value = 0
    dealers_value = 0
    counter = 0
    for number in range(0,4):
        if number < 2:
            players_cards.append(number)
            players_value += check_value(deck[number])
        else:
            dealers_cards.append(number)
            dealers_value += check_value(deck[number])
        counter += 1
    
    print_cards('Players', players_cards)
    print('-'*20)    
    print(f"Dealer's first card is: \n{deck[dealers_cards[0]]} \nSecond card is uknown")   
    print('-'*20)

#Step 3: player has blackjack!

    if players_value == 21:
        print('BLACKJACK!')

#Step 4: pass or hit me - Player

    else:
        while True:
            players_choice = input('Hit or Stay? ')
            if players_choice.upper() == "HIT":
                players_cards.append(counter)
                players_value += check_value(deck[counter])
                print_cards('Players', players_cards)
                counter += 1
                print(players_value)
            elif players_choice.upper() == 'STAY':
                break
            if players_value>=22:
                players_value = check_if_ace(players_value, players_cards, deck)
                player_bust = True
                print('BUSTED')
                break

#Step 5: Dealer hit me

    if players_value < 22:
        while True:
            if 17 > dealers_value:
                dealers_cards.append(counter)
                dealers_value += check_value(deck[counter])
                print_cards('Dealers', players_cards)
                counter += 1
            elif 21 > dealers_value > 17:
                break
            elif dealers_value >= 22:
                check_if_ace(dealers_value, dealers_cards, deck)
                dealer_bust = True
                print('DEALER IS BUSTED!')
                break
    
    print_cards('Players', players_cards)
    print_cards('Dealers', dealers_cards)
    print(f"Your total is {players_value} and dealer's total is {dealers_value}")

#Step 6: Check the winner    
    
    if dealer_bust == False and player_bust == False:
        if players_value > dealers_value:
            print("Congrats you won!")
        elif players_value < dealers_value:
            print("I'm sorry, but you lost.")
        elif players_value == dealers_value:
            print('TIE!')
    
    elif dealer_bust == True and player_bust == False:
        print("Dealer is busted! \nCongrats you won!")
    elif dealer_bust == False and player_bust == True:
        print("You are busted! \nI'm sorry, but you lost.")



    restart = input('Would you like to restart?')
    if restart.upper() != "YES":
        start = 0