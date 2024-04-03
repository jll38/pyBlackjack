from .Common.deck import Deck
from .Hands.blackjack_hand import Blackjack_Hand
def run():
    print("Running...")
    deck = Deck()
    deck.shuffle()
    player1 = Blackjack_Hand(deck)
    player1.hit()
    
