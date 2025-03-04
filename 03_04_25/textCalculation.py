from game import Game
def main():
    game = Game()
    finish = False
    while not finish:
        displayGame(game)
        choice = gameMenu(game)
        finish = processChoice(choice, game)

    
def gameMenu(game:Game):
    print("Please choose an option:")
    if game.cardToPlay != None:
        print("1. Play Drawn Card")
    elif game.cardToPlay == None and not game.finished():
        print("1. Draw Card")
    elif game.finished():
        print("1. Finish Game and Calculate Score")
    if game.wastePlay():
        print("2. Play Card from Waste Pile")
    try:
        choice = int(input('Your Choice: '))
        if (choice < 1) or (not game.wastePlay() and choice > 1) or (game.wastePlay() and choice > 2):
            print("That is an invalid choice")
            return gameMenu(game)
        return choice
    except ValueError:
        print("You entered something that is not a number.")
        return gameMenu(game)
    
def displayGame(game:Game):
    foundation_str = ""
    waste_str = ""
    for i in range(4):
        foundation_str += f"F{i+1}: {game.foundations[i].cards[game.foundations[i].topCard]}     "
        waste_str += f"W{i+1}: "
        if len(game.wastes[i]) > 0:
            waste_str += f"{game.wastes[i].cards[game.wastes[i].topCard]}     "
        else:
            waste_str += "        "

    print(foundation_str)
    print(waste_str)

    if game.cardToPlay != None:
        print(f"Drawn Card: {game.cardToPlay}")
    else:
        print(f"Remaining Cards({len(game.deck)})")

def playCard(game:Game):
    pileType = input("Do you want to play on a (F)oundation or (W)aste pile? ")
    if pileType.upper() != 'F' and pileType.upper() != 'W':
        print("Please enter F for foundation and W for waste.")
        return playCard(game)
    
    if pileType.upper() == 'F':
        pileType = 'foundation'
    else:
        pileType = 'waste'
    while True:
        try:
            pileNum = int(input(f"Which {pileType} pile (1-4) do you want to play on? "))
            if pileNum < 1 or pileNum > 4:
                print("Please enter a number 1 - 4")
                continue
            else:
                break
        except ValueError:
            print("You entered something that is not a number.")
    try:
        game.playCard(destNum=pileNum-1, destination=pileType)
    except RuntimeError as e:
        print(e)


def processChoice(choice:int, game:Game):
    if choice == 1:
        if game.cardToPlay == None and not game.finished():
            game.drawCard()
            return False
        elif game.cardToPlay != None:
            playCard(game)
            return False
        else:
            return True


    

if __name__ == "__main__":
    main()