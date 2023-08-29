

from unittest.mock import patch
def test_mock(queen_of_hearts):
    with patch('blackjack.PlayingCard.__str__',
               return_value="Test output"):
        result = str(queen_of_hearts)

    assert result == "Test output"


"""
Exercise

1. Mock the is_royal function to always return True
2. Confirm that calling blackjack_value results in 10

Note: You'll need a different card
"""
