from game import Pile, FoundPile, Game
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
