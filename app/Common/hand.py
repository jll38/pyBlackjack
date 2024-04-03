from abc import ABC, abstractmethod
from app.Common.game import Game


class Hand(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_hand(self):
        pass

    def add_subscribed_game(self, game: Game):
        self.subscribed_game = game

    def remove_subscribed_game(self):
        self.subscribed_game = None
