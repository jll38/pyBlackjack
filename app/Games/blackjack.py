from ..Common.deck import Deck
from ..Common.game import Game
from app.Hands.blackjack_hand import Blackjack_Hand


class Blackjack(Game):
    def __init__(self):
        super().__init__()
        self.deck = Deck()
        self.deck.shuffle()
        self.playing = True
        self.player = Blackjack_Hand(self.deck)
        self.player.add_subscribed_game(self)
        self.stand = False
        self.dealer = Blackjack_Hand(self.deck, True)
        self.dealer.add_subscribed_game(self)

    def start(self) -> None:
        self.player.hit()
        self.dealer.hit()
        self.player.hit()
        self.dealer.hit()
        self.dealer.get_hand_array()
        while not self.stand:
            self.initiate_turn()
            print(f"Player {self.player.get_hand_value()} | Dealer {self.dealer.get_hand_value()}")
        while not self.dealer.get_hand_value()[0] > 17 and not self.dealer.get_hand_value()[1] > 17:
            self.dealer.hit()

    def end(self, winner: bool) -> None:
        print(f"Winner: {'Dealer' if winner else 'Player'}")
        replay = input("Play again? (y\\n)\n>>>")
        if replay == 'y':
            self.start()

    def initiate_turn(self) -> None:
        is_stand = input("Hit or Stand? (h\s)\n>>>")
        if is_stand == 's':
            self.stand = True
        self.player.hit()


    def check_values(self, hand: Blackjack_Hand) -> None:
        print("Checking values...")
        value = hand.get_hand_value()
        if value[0] > 21:
            print(f"{'Dealer' if hand.is_dealer else 'Player'} Bust!")
            self.end(not hand.is_dealer)
        if value[0] == 21 or value[1] == 21:
            print(f"{'Dealer' if hand.is_dealer else 'Player'} Wins")
            self.end(hand.is_dealer)
