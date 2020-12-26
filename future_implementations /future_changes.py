class Deck(): 
    def __init__(self):
        self.card_deck_size = 52
        self.drawn_cards = 0 
        self.deck = self.deck_generator()
    
    def draw(self):
        card = self.deck[self.drawn_cards]
        self.drawn_cards += 1 
        return card 
    
    def deck_generator(self):
        random_numbers = random.sample(range(0, len(draft)), len(draft))
        deck = {}
        for cards in draft:
            deck[cards] = draft.get(random_numbers[cards])
        return deck 

class Card():
    def __init__(self, text, color, value): 
        self.text = text
        self.color = color 
        self.value = value
    
    def card_name(self):
        combination = ''
        return combination
jack = Card('Jack', 'Blue', 10)
print(jack.card_name())