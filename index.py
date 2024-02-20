from playing_card import Playing_Card
from deck import Deck
card = Playing_Card("10", "Spade")

deck = Deck()


print(card.rank)
deck.shuffle()
print(deck)
deck.deal_card()
print(deck)