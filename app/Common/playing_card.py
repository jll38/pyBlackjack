from typing import Self


class Playing_Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f"playing_card({self.rank}, {self.suit})"
    
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"