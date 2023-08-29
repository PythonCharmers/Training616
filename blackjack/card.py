from dataclasses import dataclass
from enum import Enum


class CardRank(Enum):
    JACK = "j"
    QUEEN = "q"
    KING = "k"
    ACE = "a"


ROYAL_RANKS: set[CardRank] = {CardRank.JACK, CardRank.QUEEN, CardRank.KING}


class CardSuit(Enum):
    HEARTS = "h"
    SPADES = "s"
    CLUBS = "c"
    DIAMONDS = "💎"


@dataclass
class PlayingCard:
    rank: str
    suit: CardSuit

    # value: PositiveInt

    def is_royal(self):
        # if self.rank in {'j', 'q', 'k'}:
        #     return True
        # else:
        #     return False
        return self.rank in ROYAL_RANKS

    def blackjack_value(self):
        if self.is_royal():
            return 10
        if self.rank == 'a':
            return 11
        return int(self.rank.value)

    def __str__(self):
        return f"The {self.rank} of {self.suit}"
