from card import Card, Deck


class Pile():
    def __init__(self):
        self.cards = []
        self.topCard = -1
    def playCard(self, card:Card):
        self.cards.append(card)
        self.topCard += 1
        return True
    def getTopCard(self):
        self.topCard -= 1
        return self.cards.pop()
    def __len__(self):
        return len(self.cards)
    
class FoundPile(Pile):
    def __init__(self, num):
        super().__init__()
        self.sequence = []
        self.num = num
        for i in range(13):
            self.sequence.append(Card.RANKS[((i + 1) *self.num-1) % 13])
    def playCard(self, card:Card):
        if card.rank == self.sequence[self.topCard + 1]:
            self.cards.append(card)
            self.topCard += 1
            return True
        else:
            return False

class Game():
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.foundations = []
        self.wastes = []
        for i in range(4):
            self.foundations.append(FoundPile(i + 1))
            self.wastes.append(Pile())
        self.cardToPlay = None
        self.foundationSetup()
    
    def foundationSetup(self):
        for card in self.deck.cards:
            if card.rank == 'A':
                self.deck.cards.remove(card)
                self.foundations[0].playCard(card)
                break
        for card in self.deck.cards:
            if card.rank == '2':
                self.deck.cards.remove(card)
                self.foundations[1].playCard(card)
                break
        for card in self.deck.cards:
            if card.rank == '3':
                self.deck.cards.remove(card)
                self.foundations[2].playCard(card)
                break
        for card in self.deck.cards:
            if card.rank == '4':
                self.deck.cards.remove(card)
                self.foundations[3].playCard(card)
                break
    

