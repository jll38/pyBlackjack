from ..Common.deck import Deck
from ..Common.game import Game
from app.Hands.blackjack_hand import Blackjack_Hand

class Blackjack(Game):
    def __init__(self):
        super().__init__(); 
        self.deck = Deck()
        self.deck.shuffle()

        self.player = Blackjack_Hand(self.deck)
        self.player.add_subscribed_game(self)

        self.dealer = Blackjack_Hand(self.deck, True)
        self.dealer.add_subscribed_game(self)

    def start(self) -> None:
        self.player.hit()
        self.dealer.hit()
        self.player.hit()
        self.dealer.hit()
        print(self.player.get_hand_array())
        self.dealer.get_hand_array()
        print(self.dealer.get_hand_array())
        while True:
            break

    def end(self) -> None:
        pass

    def initiate_turn(self) -> None:
        pass

    def check_values(self) -> None:
        print("Checking values...")
        