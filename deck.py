import itertools, random

# Creating a 'deck of cards'. The suits ('♥','♠','♣','♦') are a valid ASCII characters
deck = list(itertools.product(['2','3','4','5','6','7','8','9','10','J','Q','K','A']
,['♥','♠','♣','♦']))

class Deck(object):

    @staticmethod
    def draw():
        random.shuffle(deck)
        return (deck[0][0], deck[1][1]);

