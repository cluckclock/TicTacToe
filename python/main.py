import random

#List containing Cell Values - 0 1 2 is first row - 3 4 5 is second row - 6 7 8 is third row
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#Default Markings for Player 1 and Player 2 (or computer if gamemode is 1-player)
player1 = "X"
player2 = "O"

#Print the board to the console
def printBoard():
    for i in range(0,9):
        print (board[i], end="")
        if i == 2 or i == 5:
            print()
            print('——————')
        elif i != 8:
            print('|', end='')
    print()
    print()

def isFull():
    for i in range(9):
        if board[i] == ' ':
            return False
    return True

#Level 0 AI. Other AI levels funnel down to this function
def chooseRandom(symbol):
    blankSpaces = list()
    for square in range(9):
        if board[square] == ' ':
            blankSpaces.append(square)
    random.shuffle(blankSpaces)
    board [blankSpaces[0]] = symbol

#Used in AI levels 1 and above. Can be used simply and complex
def checkStrat(symbol, min, strat):
    count = 0
    cells = wins[strat]

    for cell in cells:
        if board[cell] == symbol:
            count+= 1
    if count >= min:
        for cell in cells:
            if board[cell] == ' ':
                return cell
    return -1

#Type of AI strategy. Would be in compTurn, but Python doesn't support nested
#methods for some reason...
def defendStrategy(min, toCheck):
    for i in range(len(wins)):
        goodCell = checkStrat(toCheck, min, i)
        if goodCell != -1:
            board[goodCell] = player2
            return "success"

def advCheckStrats(min, toCheck):
    goodCells = list()
    for strategy in range(len(wins)):
        firstCell = checkStrat(toCheck, min, strategy)
        if firstCell != -1:
            goodCells.append(firstCell)
            board[firstCell] = 'Z'

            secondCell = checkStrat(toCheck, min, strategy)
            board[firstCell] = ' '
            if secondCell != -1:
                goodCells.append(firstCell)
    return goodCells

#Computer strategy check for levels 2 and 3
def tryWin():
    if defendStrategy(2, player2) == "success":
        return
    else:
        return 1

#Find cell that is in list the most
def calcHighest(cells):
    boardStrat = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(cells)):
        boardStrat[cells[i]] += 1

    topScorer = 0
    topScore = boardStrat[0]
    i = 1
    for i in range(9):
        if boardStrat[i] >= topScore:
            topScore = boardStrat[i]
            topScorer = i
    return topScorer

#Run the computer's turn. Decides where to mark with random.shuffle
AILevel = 0
def compTurn():

    if AILevel == 0:
        chooseRandom(player2)

    elif AILevel == 1:
        if defendStrategy(1, player2) == "success":
            return
        chooseRandom(player2)

    elif AILevel == 2:
        if tryWin() == 1:
            if defendStrategy(2, player1) == "success":
                return
            elif defendStrategy(1, player2) == "success":
                return
            else:
                chooseRandom(player2)

    elif AILevel >= 3:
        if tryWin() == 1:
            goodCells = advCheckStrats(2, player1)
            if goodCells != []:
                print('hullo!')
                board[calcHighest(goodCells)] = player2
            else:
                goodCells = advCheckStrats(1, player2)
                if goodCells != []:
                    board[calcHighest(goodCells)] = player2
                else:
                    chooseRandom(player2)

#Run the player's turn. Asks the player which cell to mark by number (Starting at 0)
def playerTurn(symbol):
    target = 0
    blank = False
    while not blank:
        if mode == '2p':
            if symbol == player1:
                turn = name1
            elif symbol == player2:
                turn = name2
            print(turn + "'s turn:")
        target = int(input("Mark cell: ")) - 1
        if board[target] == ' ':
            blank = True
    board[target] = symbol

#Check whether the symbol inputted is three in a row somewhere on the board.
wins = [ [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6] ]
def hasWon(symbol):
    won = False
    for strat in wins:
        count = 0
        for cell in strat:
            if board[cell] == symbol:
                count+= 1
        if count == 3:
            won = True
            return won
    return won

name1 = "Player 1"
name2 = "Player 2"
#Game in 2-player mode
def twoPlayers():
    global player1
    global player2
    global name1
    global name2

    print("2-player it is then!")
    name1 = input("Player 1 name: ")
    name2 = input("Player 2 name: ")

    #Emulate do{} while() to ask players whether they want to be X or O
    acceptable = False
    while not acceptable:
        print("PLAYER 1")
        player1 = input("Be X or O: ")
        if player1 == "O":
            player2 = "X"
            acceptable = True
        elif player1 == "X":
            acceptable = True
    print("Player 1 is " + player1)
    print("Player 2 is " + player2)

    inGame()

def onePlayer():
    global player1
    global player2

    print("Prepare to fight the Python Runtime!")
#Emulate do{} while() to ask player whether they want to be X or O
    acceptable = False
    while not acceptable:
        player1 = input("Be X or O: ")
        if player1 == "O":
            player2 = "X"
            acceptable = True
        elif player1 == "X":
            acceptable = True

    global AILevel
    AILevel = int(input("AI difficulty(0, 1, 2, or 3): "))

    inGame()

#cp: Against computer. 2p: Player 1 vs. Player 2
mode = "cp"
def inGame():
    player1Won = False
    player2Won = False
    while not player1Won and not player2Won:
        if hasWon(player2):
            player2Won = True
            break
        if isFull():
            break

        playerTurn(player1)
        printBoard()

        if hasWon(player1):
            player1Won = True
            break
        if isFull():
            break

        if mode == '2p':
            playerTurn(player2)
        else:
            compTurn()
        printBoard()

    if mode == '2p':
        if player1Won:
            winnerName = name1
        elif player2Won:
            winnerName = name2
        else:
            print("Somehow, nobody won. Extra pie for the Python!")
            return
        print("Congratulations, " +  winnerName + "! Now go eat some pie.")
    else:
        if player1Won:
            print("Congratulations! Now go eat some pie.")
        elif player2Won:
            print("Wow, you lost against a stupid computer. SAD!")
        else:
            print("Somehow, nobody won. Extra pie for the Python!")

    if input("New Game?") == 'yes':
        newGame()
    else:
        print("Play again!")
        exit()

def wipeBoard():
    for i in range(len(board)):
        board[i] = ' '

def newGame():
    wipeBoard()

    mode = input("2-player game or against a computer? (2p/cp) ")
    if mode == '2p':
        twoPlayers()
    else:
        onePlayer()

def main():
    global mode

    print("Tic-Tac-Toe")
    printBoard()
    newGame()


if __name__ == '__main__':
    main()
