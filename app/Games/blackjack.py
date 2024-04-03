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

    def compare_player_values(self):
    # Get the hand values for the player and dealer
        player_value = self.player.get_hand_value()
        dealer_value = self.dealer.get_hand_value()

    # Adjust for Aces if the second value is over 21
        player_final_value = player_value[0] if player_value[1] > 21 else player_value[1]
        dealer_final_value = dealer_value[0] if dealer_value[1] > 21 else dealer_value[1]

    # Compare the final values to determine the winner
        if player_final_value > 21:  # Player busts
            self.end(True)  # Dealer wins
        elif dealer_final_value > 21:  # Dealer busts
            self.end(False)  # Player wins
        elif player_final_value > dealer_final_value:
            self.end(False)  # Player wins
        elif dealer_final_value > player_final_value:
            self.end(True)  # Dealer wins
        else:
            print("It's a tie!")
        

        

    def start(self) -> None:
        self.player.hit()
        self.dealer.hit()
        self.player.hit()
        self.dealer.hit()
        print(f"Player Hand: {self.player.get_hand_value()[0]} or {self.player.get_hand_value()[1]}")
        print(f"Dealer Hand: {self.dealer.get_hand_value()[0]} or {self.dealer.get_hand_value()[1]}")
        while not self.stand:
            self.initiate_turn()
            print(f"Player {self.player.get_hand_value()} | Dealer {self.dealer.get_hand_value()}")
        while not self.dealer.get_hand_value()[0] > 17 and not self.dealer.get_hand_value()[1] > 17:
            self.dealer.hit()
        self.compare_player_values()

    def end(self, winner: bool = None) -> None:
        if winner is None:
            print("It's a tie!")
        print(f"Winner: {'Dealer' if winner else 'Player'}")
        replay = input("Play again? (y\\n)\n>>>")
        if replay == 'y':
            Blackjack().start()

    def initiate_turn(self) -> None:
        is_stand = input("Hit or Stand? (h\s)\n>>>")
        if is_stand == 's':
            self.stand = True
        else:
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
