"""
Design the data structures for a generic deck of cards.
Explain how you would subclass the data structures to
implement blackjack.
"""

class Deck(object):
    def __init__(self, shuffle=False):
        self.cards = self.build_deck()
        self.discards = []
        if shuffle == True: self.shuffle()

    def build_deck(self):
        """Builds standard deck of 52 cards with four suits"""
        spades = [Card("Spade", x) for x in range(1, 13)]
        hearts = [Card("Heart", x) for x in range(1, 13)]
        diamonds = [Card("Diamond", x) for x in range(1, 13)]
        clubs = [Card("Club", x) for x in range(1, 13)]
        return spades + hearts + diamonds + clubs

    def draw(self):
        """Pops card at end, returns the card, and adds to discard"""
        card = self.cards.pop()
        self.discards.append(card)
        return card

    def shuffle(self):
        """Implemenets Knuth Shuffle to randomly shuffle cards"""
        self.cards.append(self.discards)
        self.discards = []


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

##############################################

class BlackJackDeck(Deck):
    def __init__(self):
        super(BlackJackDeck, self).__init__()

    def build_deck(self):
        """
        Builds special deck to take into account the special values
        of blackjack cards. 10-K are 10, Ace is 1.
        """
        values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        spades = [Card("Spade", x) for x in values]
        hearts = [Card("Heart", x) for x in values]
        diamonds = [Card("Diamond", x) for x in values]
        clubs = [Card("Club", x) for x in values]
        return spades + hearts + diamonds + clubs

        
class BlackJackHand(object):
    def __init__(self, deck):
        self.cards = []
        self.deck = deck
        self.draw()
        self.draw()

    def draw(self):
        self.cards.append(self.deck.draw())
        self.total = sum(self.cards)
        self.check_total()

    def check_total(self):
        """Define draw/stand strategy depending on sum"""
        if self.total < 17:
            self.draw()
        elif 17 <= self.total < 21:
            self.stand()
        elif self.total > 21 and 11 in self.cards:
            self.ace_switch()
            self.check_total()
        else:
            self.bust()

    def ace_switch(self)
        """Switches the value of Ace from 11 to 1"""
        index = self.cards.index(11)
        self.cards[index] = 1

    def stand(self):
        pass

    def bust(self):
        pass
