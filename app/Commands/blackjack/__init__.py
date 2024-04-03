import sys
from app.Commands import Command
from app.Games.blackjack import Blackjack

class BlackjackCommand(Command):
    def execute():
        print("Starting Blackjack...")
        Blackjack().start()