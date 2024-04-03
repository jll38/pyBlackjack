from ..Common.hand import Hand
from ..Common.deck import Deck
from app.Common.playing_card import Playing_Card
from typing import List


class Blackjack_Hand(Hand):

    def __init__(self, deck: Deck, is_dealer: bool = False,):
        self.is_dealer = is_dealer
        self.player_name = "Dealer" if is_dealer else "Player"
        self.assigned_deck = deck
        self.hand = []
        self.total = [0, 0]
        self.subscribed_game = None

    def get_hand(self) -> List:
        pass

    def get_hand_array(self) -> List:
        return self.hand

    def get_hand_value(self) -> List[int]:
        return self.total

    def update_hand_value(self, card: Playing_Card) -> None:
        self.hand.append(card)
        self.total[0] = self.total[0] + card.get_numeric()[0]
        if len(card.get_numeric()) > 1:
            self.total[1] = self.total[1] + card.get_numeric()[1]
        else:
            self.total[1] = self.total[1] + card.get_numeric()[0]

    def hit(self) -> None:
        print("Hit")
        try:
            hit_card = self.assigned_deck.deal_card()
            self.update_hand_value(hit_card)
            print(f"{self.player_name} received a {hit_card}")
            self.notify_game()
        except Exception as e: 
            print("Error occurred drawing card:", e)
            print(f"Hand is now {self.get_hand_array()}")

    def notify_game(self):
        self.subscribed_game.check_values(self)
