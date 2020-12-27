import random

class Card():
    def __init__(self, color, card_name, card_value):
        self.color = color
        self.card_name = card_name
        self.card_value = card_value
        self.card_full_name = self.card_name + self.color
    def print_card_name(self):
        return '{} of {}'.format(self.card_name, self.color)
    

class Deck():
    def __init__(self, colors, card_names):
        self.colors = colors
        self.card_names = card_names
        self.deck = self.deck_generator()
        self.deck_shuffle()

    def deck_generator(self):
        deck = []
        for card_color in self.colors:
            for card, card_value in self.card_names.items():
                deck.append(Card(card_color, card, card_value))
        return deck
    
    def find_card(self, wanted_card):
        for card in self.deck:
            if card.card_name == wanted_card:
                return card 

    def deck_shuffle(self):
        random.shuffle(self.deck)


    def card_draw(self):
        return self.deck.pop()

    def draw_2(self):
        return [self.card_draw(), self.card_draw()]
