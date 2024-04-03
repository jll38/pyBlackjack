from .playing_card import Playing_Card
import random

class Deck:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self._cards = [Playing_Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def add_card(self, card: Playing_Card) -> None:
        if not isinstance(card, Playing_Card):
            raise ValueError("Only instances of Playing_Card can be added to the deck.")
        if card in self._cards:
            raise ValueError("Duplicate card cannot be added to the deck.")
        self._cards.append(card)

    def remove_card_index_at(self, index: int) -> None:
        if index < 0 or index >= len(self._cards):
            raise IndexError("Card index out of bounds.")
        self._cards.pop(index)

    def deal_card(self):
        if len(self._cards) == 0:
            raise ValueError("Cannot deal from an empty deck.")
        return self._cards.pop()

    def __repr__(self):
        return f"Deck of {len(self._cards)} cards: {self._cards}"
    
    def __str__(self):
        card_descriptions = [str(card) for card in self._cards]
        return f"Deck with {len(self._cards)} cards: {', '.join(card_descriptions)}"

