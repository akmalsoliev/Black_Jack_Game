import random
import future_changes

colors = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
card_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
draft = {}
index = 0
for card_colors in colors:
    for cards in card_names:
        draft[index] = f'{cards} of {card_colors}'
        index += 1

def deck_generator():
    random_numbers = random.sample(range(0, len(draft)), len(draft))
    deck = {}
    for cards in draft:
        deck[cards] = draft.get(random_numbers[cards])
    return deck 

card_values = [[11, 'Ace'], [2, '2 '], [3, '3 '], [4, '4 '], [5, '5 '], [6, '6 '], [7, '7 '], [8, '8 '], [9, '9 '], [10, '10'], [10, 'Ja'], [10, 'Qu'], [10, 'Ki']]