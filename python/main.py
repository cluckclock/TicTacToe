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

#Run the computer's turn. Decides where to mark with random.shuffle
def compTurn():
    blankSpaces = list()
    for square in range(9):
        if board[square] == ' ':
            blankSpaces.append(square)
    random.shuffle(blankSpaces)
    board [blankSpaces[0]] = player2

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

def main():
    global mode

    print("Tic-Tac-Toe")
    printBoard()
    mode = input("2-player game or against a computer? (2p/cp) ")
    if mode == '2p':
        twoPlayers()
    else:
        onePlayer()

if __name__ == '__main__':
    main()
