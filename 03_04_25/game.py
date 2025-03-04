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
    def drawCard(self):
        if len(self.deck) == 0:
            raise RuntimeError("Deck is empty")
        if self.cardToPlay == None:
            self.cardToPlay = self.deck.deal()
    def playCard(self, destNum, sourceNum = 0, source = "deck", destination="foundation"):
        if source == "deck":
            if self.cardToPlay == None:
                raise RuntimeError("Invalid Move")
            if destination == "foundation":
                if self.foundations[destNum].playCard(self.cardToPlay):
                    self.cardToPlay = None
                else:
                    raise RuntimeError(f"Invalid Move: The next card for foundation #{destNum + 1} is {self.foundations[destNum].sequence[self.foundations[destNum].topCard + 1]}")
            elif destination == "waste":
                self.wastes[destNum].playCard(self.cardToPlay)
                self.cardToPlay = None
        elif source == "waste":
            if len(self.wastes[sourceNum]) == 0:
                raise RuntimeError("Invalid Move: Waste Pile is Empty")
            if destination == "foundation":
                card = self.wastes[sourceNum].getTopCard()
                if not self.foundations[destNum].playCard(card):
                    self.wastes[sourceNum].playCard(card)
                    raise RuntimeError(f"Invalid Move: The next card for foundation #{destNum + 1} is {self.foundations[destNum].sequence[self.foundations[destNum].topCard + 1]}")
            else:
                raise RuntimeError("Invalid Move: Waste Cards can only be played on foundations")
    
    def calculateScore(self):
        score = 0
        score += len(self.deck)
        for pile in self.wastes:
            score += len(pile)
        return score      

    def finished(self):
        return self.cardToPlay == None and len(self.deck) == 0

    def wastePlay(self):
        return len(self.wastes[0]) > 0 or len(self.wastes[1]) > 0 or len(self.wastes[2]) > 0 or len(self.wastes[3]) > 0

