from colorama import Fore
from .Common.deck import Deck
from .Hands.blackjack_hand import Blackjack_Hand
def run():
    print(f"{Fore.LIGHTBLACK_EX}#################################")
    print(f"{Fore.WHITE} 🃏 Welcome to Lechner Casino 🃏  ")
    print(f"{Fore.YELLOW}         Python Edition          ")
    print(f"{Fore.LIGHTBLACK_EX}#################################")
    print(f"{Fore.WHITE}You are playing: {Fore.YELLOW}Blackjack{Fore.WHITE}")
    print()
    deck = Deck()
    deck.shuffle()
    player1 = Blackjack_Hand(deck)
    player1.hit()
    
