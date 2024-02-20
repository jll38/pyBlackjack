from typing import Self


class playing_card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f"playing_card({self.rank}, {self.suit})"
    
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
    
    def create(rank: str, suit: str) -> Self:
        return playing_card(rank, suit)