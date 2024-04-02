from abc import ABC, abstractmethod 

class Hand(ABC):

    @abstractmethod
    def get_hand(self):
        pass
