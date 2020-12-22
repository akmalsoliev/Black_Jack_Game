import create_deck

def check_value(card):
    checking_index = card[0:2]
    for cards in create_deck.card_values:
        if checking_index in cards[1]:
            value = cards[0]
    return value