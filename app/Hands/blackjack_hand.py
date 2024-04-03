from ..Common.hand import Hand
from ..Common.deck import Deck

class Blackjack_Hand(Hand):

    def __init__(self, deck: Deck, is_dealer: bool = False,):
        self.player_name = "Dealer" if is_dealer else "Player"
        self.assigned_deck = deck
        self.hand = []
        self.subscribed_game = None

    def add_subscribed_game(self):
        pass

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
            print(f"{self.player_name} received a {hit_card} ")
        except:
            print("Assigned Deck is missing or invalid.")
            print(f"Hand is now {self.get_hand_array}")
