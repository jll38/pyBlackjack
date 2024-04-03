from abc import ABC, abstractmethod


class Hand(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_hand(self):
        pass

