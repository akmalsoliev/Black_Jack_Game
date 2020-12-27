import card_deck_support
from utilities import * 

colors = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] 
card_names = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

dealer_bust = False
player_bust = False

def main():
    while True:
        play_black_jack()
        user_input = input("Would you like to restart the game? ")
        if user_input.upper() != "YES":
            break

def play_black_jack():

    global dealer_bust
    global player_bust
    deck = card_deck_support.Deck(colors, card_names)

    player1 = deck.draw_2()
    dealer = deck.draw_2()

    player1_value = hand_score(player1)
    dealer_value = hand_score(dealer)

    while True:
        print_out_information(player1, player1_value, dealer, dealer_value, card_reveale=False)
        player_input = input('Hit or Stay? ')
        if player_input.upper() == 'HIT':
            new_draw = deck.card_draw()
            player1.append(new_draw)
            print('You have drawn ', new_draw.print_card_name(), '\n', '-'*30, '\n')
            player1_value = hand_score(player1)
        elif player_input.upper() == 'STAY':
            break
        if player1_value > 21:
            player_bust = True
            break
    
    if player1_value <= 21:
        while player1_value >= dealer_value <= 21:
            dealer.append(deck.card_draw())
            dealer_value = hand_score(dealer)
        if dealer_value > 21:
            dealer_bust = True
    
    print_out_information(player1, player1_value, dealer, dealer_value, card_reveale=True)

    check_win(player1_value, dealer_value, dealer_bust, player_bust)


if __name__ == "__main__":
    main()