from ..Common.deck import Deck
from abc import ABC, abstractmethod 

class Game(ABC):

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def end(self) -> None:
        pass
    @abstractmethod
    def initiate_turn(self) -> None:
        pass
