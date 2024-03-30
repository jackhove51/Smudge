import pytest

from smudge.game_setup import Card, Player, Deck, Game


@pytest.fixture(scope='session')
def deck():
    yield Deck()


@pytest.fixture(scope='session')
def game():
    yield Game()


def test_deck(deck):
    assert isinstance(deck, Deck)
    assert len(deck.cards) == 52
    assert deck.cards[0].suit == 'Diamonds' and deck.cards[0].value == '2'
    assert deck.cards[-1].suit == 'Spades' and deck.cards[-1].value == 'A'


def test_players(game):
    assert isinstance(game, Game)
    for i, player in enumerate(game.players):
        assert isinstance(player, Player)
        assert player.id == i + 1
        assert player.next.id == (i + 1) % 4 + 1
