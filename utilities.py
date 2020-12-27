def check_win(player1_value, dealers_value, dealer_bust, player_bust):
    if dealer_bust == False and player_bust == False:
        if player1_value > dealers_value:
            print("Congrats you won!")
        elif player1_value < dealers_value:
            print("I'm sorry, but you lost.")
        elif player1_value == dealers_value:
            print('TIE!')
    
    elif dealer_bust == True and player_bust == False:
        print("Dealer is busted! \nCongrats you won!")
    
    elif dealer_bust == False and player_bust == True:
        print("You are busted! \nI'm sorry, but you lost.")

def hand_score(cards):
    hand_score = 0
    Ace_in_hand = 0 
    for card in cards:
        hand_score += card.card_value 
        if card.card_name == 'Ace':
            Ace_in_hand += 1
    while hand_score > 21 and Ace_in_hand > 0: 
        hand_score -= 10
        Ace_in_hand -= 1        
    return hand_score

def print_out_information(player1, player1_value, dealer, dealer_value, card_reveale = False):
    for n in range(len(player1)):
            print(f'Your {n+1} card is: ', player1[n].print_card_name())
    print(f'Total value of your hand is {player1_value}.')
    print('Dealers 1 card is: ', dealer[0].print_card_name())
    if card_reveale == True: 
        for n in range(1, len(dealer)):
            print(f'Dealers {n+1} card is: ', dealer[n].print_card_name())
        print(f"Total value of dealer's hand is {dealer_value}.")
    else:
        print("Dealer's second card is hidden.")