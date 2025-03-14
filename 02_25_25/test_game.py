from game import Pile, FoundPile, Game
from card import Card
import pytest

def test_pile_sequence():
    pile = Pile()
    with pytest.raises(AttributeError):
        pile.sequence
    found1 = FoundPile(1)
    assert found1.sequence == ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    found2 = FoundPile(2) 
    assert found2.sequence == ['2', '4', '6', '8', '10', 'Q', 'A', '3', '5', '7', '9', 'J', 'K']
    found3 = FoundPile(3)
    assert found3.sequence == ['3', '6', '9', 'Q', '2', '5', '8', 'J', 'A', '4', '7','10', 'K']
    found4 = FoundPile(4)
    assert found4.sequence == ['4', '8', 'Q', '3', '7', 'J', '2', '6', '10', 'A', '5', '9', 'K']

def test_game_setup():
    game = Game()
    assert len(game.deck) == 48
    assert len(game.foundations[0]) == 1
    assert len(game.foundations[1]) == 1
    assert len(game.foundations[2]) == 1
    assert len(game.foundations[3]) == 1
    assert len(game.wastes[0]) == 0
    assert len(game.wastes[1]) == 0
    assert len(game.wastes[2]) == 0
    assert len(game.wastes[3]) == 0
    assert game.cardToPlay == None
    assert game.foundations[0].cards[0].rank == "A"
    assert game.foundations[1].cards[0].rank == "2"
    assert game.foundations[2].cards[0].rank == "3"
    assert game.foundations[3].cards[0].rank == "4"

def test_game_drawCard():
    game = Game()
    game.drawCard()
    assert len(game.deck) == 47
    assert game.cardToPlay != None
    game.drawCard()
    assert len(game.deck) == 47

def test_game_drawAllCards():
    game = Game()
    for i in range(50):
        try:
            game.drawCard()
            game.cardToPlay = None
        except RuntimeError as e:
            assert str(e) == "Deck is empty"
            break           
    assert len(game.deck) == 0

def test_game_playCard():
    game = Game()
    card1 = Card("HEARTS", '3')
    card2 = Card("CLUBS", "2")
    card3 = Card("SPADES", "6")
    card4 = Card("Diamonds", '8')
    card5 = Card('hearts', "4")

    game.cardToPlay = card1
    try:
        game.playCard(0)
    except RuntimeError:
        assert True
    else:
        assert False

    try:
        game.playCard(1)
    except RuntimeError:
        assert True
    else:
        assert False

    try:
        game.playCard(2)
    except RuntimeError:
        assert True
    else:
        assert False

    try:
        game.playCard(3)
    except RuntimeError:
        assert True
    else:
        assert False

    game.playCard(0, destination="waste")
    assert game.cardToPlay == None
    assert len(game.wastes[0]) == 1

    game.cardToPlay = card2
    game.playCard(0)
    assert game.cardToPlay == None
    assert len(game.foundations[0]) == 2

    game.cardToPlay = card5
    game.playCard(1)
    assert game.cardToPlay == None
    assert len(game.foundations[1]) == 2

    game.cardToPlay = card3
    game.playCard(2)
    assert game.cardToPlay == None
    assert len(game.foundations[2]) == 2

    game.cardToPlay = card4
    game.playCard(3)
    assert game.cardToPlay == None
    assert len(game.foundations[3]) == 2

    try:
        game.playCard(destNum=1, source="waste", sourceNum=0)
    except RuntimeError:
        pass
    else:
        assert False
    
    try:
        game.playCard(destNum=2, source="waste", sourceNum=0)
    except RuntimeError:
        pass
    else:
        assert False
    
    try:
        game.playCard(destNum=3, source="waste", sourceNum=0)
    except RuntimeError:
        pass
    else:
        assert False
    
    try:
        game.playCard(destNum=0, source="waste", sourceNum=1)
    except RuntimeError:
        pass
    else:
        assert False
    
    game.playCard(destNum=0, source="waste", sourceNum=0)
    assert len(game.foundations[0]) == 3
    assert len(game.wastes[0]) == 0 
    