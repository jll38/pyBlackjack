from ..Common.hand import Hand
from ..Common.deck import Deck
from ..Games.blackjack import Blackjack


class Blackjack_Hand(Hand):

    def __init__(self, deck: Deck, is_dealer: bool = False,):
        self.dealer = is_dealer
        self.assigned_deck = deck
        self.hand = []
        self.subscribed_game = None

    def add_subscribed_game(self, game: Blackjack):
        self.subscribed_game = game

    def remove_subscribed_game(self):
        self.subscribed_game = None

    def get_hand(self):
        pass

    def get_hand_array(self):
        return self.hand

    def hit(self):
        print("Hit")
        try:
            #self.hand.push(self.assigned_deck.deal_card())
            hit_card = self.assigned_deck.deal_card()
            self.hand.append(hit_card)
            print(f"Player received a {hit_card} ")
        except:
            print("Assigned Deck is missing or invalid.")
            print(f"Hand is now {self.get_hand_array}")
