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

start = True

#Game start

while start == True:
    dealer_bust = False
    player_bust = False
#Step 1: Deck Generation
    deck = deck_generator()
    players_cards = []
    dealers_cards = []
    players_value = 0
    dealers_value = 0
    draw_card_number = 0
    for number in range(0,4):
        if number < 2:
            players_cards.append(number)
            players_value += check_value(deck[number])
        else:
            dealers_cards.append(number)
            dealers_value += check_value(deck[number])
        draw_card_number += 1
    
    print_cards('Players', players_cards)
    print(f'Your card value is: {players_value}')
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
                players_cards.append(draw_card_number)
                players_value += check_value(deck[draw_card_number])
                print_cards('Players', players_cards)
                draw_card_number += 1
                print(players_value)
            elif players_choice.upper() == 'STAY':
                break
            if players_value > 21 and check_if_ace(players_value, players_cards, deck) == True:
                players_value -= 10
            elif players_value > 21: 
                player_bust = True
                print('-' * 20, '\nBUSTED') 
                break

#Step 5: Dealer hit me

    if players_value <= 21:
        while players_value > dealers_value and players_value <= 21:
            dealers_cards.append(draw_card_number)
            dealers_value += check_value(deck[draw_card_number])
            draw_card_number += 1
            if dealers_value > 21 and check_if_ace(dealers_value, dealers_cards, deck) == True:
                dealers_value -= 10 
            elif dealers_value > 21:    
                dealer_bust = True
                print('-' * 20, '\nDEALER IS BUSTED') 
                break

    print_cards('Players', players_cards)
    print_cards('Dealers', dealers_cards)
    print('-'*20)
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
        start = False