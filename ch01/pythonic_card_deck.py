import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    # ranked!
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['spades', 'diamonds', 'clubs', 'hearts']

    def __init__(self):

        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):

        return len(self._cards)

    def __getitem__(self, position):

        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):

    rank_value = FrenchDeck.ranks.index(card.rank)

    return rank_value * len(suit_values) + suit_values[card.suit]