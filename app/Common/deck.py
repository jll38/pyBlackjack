from .playing_card import Playing_Card
import random
class Deck:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self.cards = [Playing_Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def add_card(self, card : Playing_Card) -> None:
        self.cards.append(card)

    def remove_card_index_at(self, index: int) -> None:
        self.cards.pop(index)

    def deal_card(self) -> None:
        return self.cards.pop()

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards: {self.cards}"
    
    def __str__(self):
        return f"{self.cards}"