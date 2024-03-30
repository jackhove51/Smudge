__all__ = ['Card', 'Player', 'Deck', 'Game']

from random import shuffle

SUITS = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
MAPPING = {
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '10': 'Ten',
    'J': 'Jack',
    'Q': 'Queen',
    'K': 'King',
    'A': 'Ace'
}


class Card:

    def __init__(self, number: int, suit: str):
        self.number = number
        self.suit = suit
        self._check_errors()
        self._assign_value()

    def _check_errors(self):
        if self.number < 2 or self.number > 14:
            raise ValueError("Card number must be between 2 and 14")
        if self.suit not in SUITS:
            raise ValueError(
                f"Invalid suit: {self.suit}. Suit must be one of {SUITS}"
            )

    def _assign_value(self):
        match self.suit:
            case 11:
                self.value = 'J'
            case 12:
                self.value = 'Q'
            case 13:
                self.value = 'K'
            case 14:
                self.value = 'A'
            case _ if self.number < 11:
                self.value = str(self.number)

    def __print__(self):
        print(f"{MAPPING[self.value]} of {self.suit}")


class Player:

    def __init__(self, number: int):
        self.id = number
        if self.id < 1 or self.id > 4:
            raise ValueError("Player id must be between 1 and 4")
        self.next = None
        self.hand = []


class Deck:

    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for num in range(2, 15):
                self.cards.append(Card(num, suit))

    def __print__(self) -> None:
        for card in self.cards:
            print(card)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def deal(self, player: Player) -> None:
        pass


class Game:

    def __init__(self):
        self.players = [Player(i + 1) for i in range(4)]
        for i, player in enumerate(self.players):
            player.next = self.players[(i + 1) % 4]
