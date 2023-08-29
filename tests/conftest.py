import pytest
from blackjack import PlayingCard, CardRank, CardSuit

@pytest.fixture(scope='function')
def queen_of_hearts():
    print("Queen created")
    card = PlayingCard(CardRank.QUEEN, CardSuit.HEARTS)
    return card




@pytest.fixture(scope='function')
def ace_of_hearts():
    print("Queen created")
    card = PlayingCard(CardRank.ACE, CardSuit.HEARTS)
    return card