import pytest
from app.Common.playing_card import Playing_Card
class TestPlayingCard:

    # Creating a new Playing_Card object with a valid rank and suit should not raise any exceptions.
    def test_valid_rank_and_suit(self):
        try:
            card = Playing_Card('2', 'Clubs')
        except ValueError:
            pytest.fail("Unexpected ValueError")

    # Creating a new Playing_Card object with an invalid rank should raise a ValueError.
    def test_invalid_rank(self):
        with pytest.raises(ValueError):
            card = Playing_Card('13', 'Hearts')

    # The __repr__ method should return a string representation of the Playing_Card object that can be used to recreate the object.
    def test_repr_method(self):
        card = Playing_Card('2', 'Clubs')
        assert repr(card) == "Playing_Card(2, Clubs)"

    # The __str__ method should return a string representation of the Playing_Card object that is human-readable.
    def test_str_method(self):
        card = Playing_Card('2', 'Clubs')
        assert str(card) == "2 of Clubs"

    # The get_numeric method should return a list of integers representing the numeric value of the card.
    def test_get_numeric_method(self):
        card = Playing_Card('A', 'Spades')
        assert card.get_numeric() == [1, 11]

    # Creating a new Playing_Card object with an invalid suit should raise a ValueError.
    def test_invalid_suit(self):
        with pytest.raises(ValueError):
            card = Playing_Card('2', 'Invalid Suit')

    # The get_numeric method should return [1, 11] for an Ace.
    def test_get_numeric_ace(self):
        card = Playing_Card('A', 'Clubs')
        assert card.get_numeric() == [1, 11]

    # The get_numeric method should return [10] for a face card or a 10.
    def test_get_numeric_face_card(self):
        card = Playing_Card('K', 'Diamonds')
        assert card.get_numeric() == [10]

    # The get_numeric method should return the numeric value of the rank as a list for other ranks.
    def test_get_numeric_other_ranks(self):
        card = Playing_Card('5', 'Clubs')
        assert card.get_numeric() == [5]

    # Creating a new Playing_Card object with a rank or suit that is an empty string should raise a ValueError.
    def test_empty_rank(self):
        with pytest.raises(ValueError):
            card = Playing_Card('', 'Clubs')

    # The get_numeric method should return an empty list for an invalid rank.
    def test_invalid_rank(self):
        card = Playing_Card('X', 'Clubs')
        assert card.get_numeric() == []

    # The get_numeric method should return an empty list for an invalid suit.
    def test_invalid_suit(self):
        card = Playing_Card('2', 'Stars')
        assert card.get_numeric() == []

    # The get_numeric method should return a list of two integers [1, 1] for a Playing_Card object with rank 'A' and suit 'Clubs'.
    def test_ace_card(self):
        card = Playing_Card('A', 'Clubs')
        assert card.get_numeric() == [1, 11]

    # Creating a new Playing_Card object with a valid rank and suit should not raise any exceptions.
    def test_valid_rank_and_suit(self):
        try:
            card = Playing_Card('2', 'Clubs')
        except ValueError:
            pytest.fail("Unexpected ValueError")

    # Creating a new Playing_Card object with an invalid rank should raise a ValueError.
    def test_invalid_rank(self):
        with pytest.raises(ValueError):
            card = Playing_Card('15', 'Hearts')

    # Creating a new Playing_Card object with an invalid suit should raise a ValueError.
    def test_invalid_suit(self):
        with pytest.raises(ValueError):
            card = Playing_Card('A', 'Stars')

    # Creating a new Playing_Card object with a valid rank and suit should not raise any exceptions.
    def test_valid_rank_and_suit(self):
        try:
            card = Playing_Card('2', 'Clubs')
        except ValueError:
            pytest.fail("Unexpected ValueError")

    # Creating a new Playing_Card object with an invalid rank should raise a ValueError.
    def test_invalid_rank(self):
        with pytest.raises(ValueError):
            card = Playing_Card('15', 'Hearts')

    # Creating a new Playing_Card object with an invalid suit should raise a ValueError.
    def test_invalid_suit(self):
        with pytest.raises(ValueError):
            card = Playing_Card('A', 'Stars')