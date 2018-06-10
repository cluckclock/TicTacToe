import random

#List containing Cell Values - 0 1 2 is first row - 3 4 5 is second row - 6 7 8 is third row
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#Default Markings for computer and player
computer = "O"
player = "X"

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
    shuffle(blankSpaces)
    board [blankSpaces[0]] = computer

#Run the player's turn. Asks the player which cell to mark by number (Starting at 0)
def playerTurn():
    target = 0
    blank = False
    while not blank:
        target = int(input("Mark cell: ")) - 1
        if board[target] == ' ':
            blank = True
    board[target] = player

#Check whether the symbol inputted is three in a row somewhere on the board.
#Optimize?
def hasWon(symbol):
    won = False
    if  (board[0] == symbol and board[1] == symbol and board[2] == symbol) or \
        (board[3] == symbol and board[4] == symbol and board[5] == symbol) or \
        (board[6] == symbol and board[7] == symbol and board[8] == symbol) or \
        \
        (board[0] == symbol and board[4] == symbol and board[8] == symbol) or \
        (board[6] == symbol and board[4] == symbol and board[2] == symbol) or \
        \
        (board[0] == symbol and board[3] == symbol and board[6] == symbol) or \
        (board[1] == symbol and board[4] == symbol and board[7] == symbol) or \
        (board[2] == symbol and board[5] == symbol and board[8] == symbol):
        won = True
    return won

def main():
    global computer
    global player

    print("Tic-Tac-Toe")
    printBoard()

    #Emulate do{} while() to ask player whether they want to be X or O
    acceptable = False
    while not acceptable:
        player = input("Be X or O: ")
        if player == "O":
            computer = "X"
            acceptable = True
        elif player == "X":
            acceptable = True

    playerWon = False
    compWon = False
    while not playerWon and not compWon:
        if hasWon(computer):
            compWon = True
            break
        if isFull():
            break

        playerTurn()
        printBoard()

        if hasWon(player):
            playerWon = True
            break
        if isFull():
            break

        compTurn()
        printBoard()

    if playerWon:
        print("Congratulations! Now go eat some pie.")
    elif compWon:
        print("Wow, you lost against a stupid computer. SAD!")
    else:
        print("Somehow, nobody won. Extra pie for the Python!")

if __name__ == '__main__':
    main()
