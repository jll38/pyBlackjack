from typing import Self, List


class Playing_Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f"playing_card({self.rank}, {self.suit})"

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def get_numeric(self) -> List[int]:
        if self.rank == 'A':
            return [1, 11]
        elif self.rank in ('K', 'Q', 'J', '10'):
            return [10]
        return [int(self.rank)]
