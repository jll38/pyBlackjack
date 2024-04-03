from colorama import Fore
from .Common.deck import Deck
from .Hands.blackjack_hand import Blackjack_Hand
from app.Commands import CommandHandler
from app.Commands.blackjack import BlackjackCommand


class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def run(self):
        self.init_commands()
        print(f"{Fore.LIGHTBLACK_EX}#################################")
        print(f"{Fore.WHITE} 🃏 Welcome to Lechner Casino 🃏  ")
        print(f"{Fore.YELLOW}         Python Edition          ")
        print(f"{Fore.LIGHTBLACK_EX}#################################")
        print(f"{Fore.WHITE}You are playing: {Fore.YELLOW}Blackjack{Fore.WHITE}")
        print()
        while True:
            input(self.command_handler.execute_command(input("What game would you like to play? \n>>> ").strip()))

    def init_commands(self):
        self.command_handler.register_command("blackjack", BlackjackCommand)
