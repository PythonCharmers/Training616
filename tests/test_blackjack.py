from blackjack import PlayingCard

import pytest
from blackjack import PlayingCard, CardRank, CardSuit


def test_quick():
    assert True


def test_queen_hearts():
    queen_hearts = PlayingCard(CardRank.QUEEN, CardSuit.HEARTS)
    assert queen_hearts.is_royal()
    assert queen_hearts.blackjack_value() == 10


card_tests = [
    # (rank, suit, is_royal, blackjack_value)
    (CardRank.QUEEN, CardSuit.HEARTS, True, 10),
    (CardRank.ACE, CardSuit.HEARTS, False, 11),
]


@pytest.mark.parametrize("rank,suit,is_royal,blackjack_value", card_tests)
def test_cards(rank, suit, is_royal, blackjack_value):
    my_card = PlayingCard(rank, suit)
    assert my_card.is_royal() == is_royal
    assert my_card.blackjack_value() == blackjack_value


# Don't usually put this here
def square(x):
    return x ** 2


from hypothesis import given, strategies


@given(strategies.floats(min_value=1, max_value=1e100))
def test_square(x):
    print(x)
    assert square(x) >= x
    assert square(x) >= x


@given(strategies.floats(min_value=1, max_value=1e100), strategies.floats(min_value=1, max_value=1e100))
def test_something(x, y):
    assert square(x) >= x
    assert square(y) >= y


def test_queen_royal(queen_of_hearts):
    assert queen_of_hearts.is_royal() == True