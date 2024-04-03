from typing import List

class Playing_Card:
    valid_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    valid_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self, rank: str, suit: str):
        if rank not in self.valid_ranks:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in self.valid_suits:
            raise ValueError(f"Invalid suit: {suit}")
        self.rank: str = rank
        self.suit: str = suit

    def __repr__(self) -> str:
        return f"Playing_Card({self.rank}, {self.suit})"

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def get_numeric(self) -> List[int]:
        """Returns the numeric values of the card. For Aces, returns [1, 11]. For face cards and 10, returns [10].
        For other ranks, returns their numeric value as a list."""
        if self.rank == 'A':
            return [1, 11]
        elif self.rank in ('K', 'Q', 'J', '10'):
            return [10]
        return [int(self.rank)]

