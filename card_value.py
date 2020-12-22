from card_support import *

def check_value(card):
    checking_index = card[0:2]
    for cards in card_values:
        if checking_index in cards[1]:
            value = cards[0]
    return value

def check_if_ace(value, input_list, deck):
    for cards in input_list:
        if deck[cards] == 'A':
            return True
    return False