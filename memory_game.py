import random as r

def initGame(rows, columns, board) -> dict[any]:
    '''This func resets the gameData values'''
    gameData = {
        'rows':rows,
        'columns':columns,
        'score': {'player1': 0, 'player2': 0},
        'turn': 'player1',
        'gameOver':False,
        'moveHistory':[],
    }
    return gameData

def initBoard(rows,columns,cards) -> dict[any]:
    '''This func resets the gameboard'''
    board = {}
    r.shuffle(cards)
    for i in range(4):
        for j in range(4):
            board.update({(i,j): {'card': cards.pop(), 'flipped': False, 'matched': False}})
    return board


def getCardX() -> int:
    '''This func gets the line of a card'''
    while True:
        x = input("Enter the card's line number ")
        if x in ['1', '2', '3', '4']:
            return int(x)
        else:
            print("Invalid input ")
def getCardY() -> int:
    '''This func gets the line of a card'''
    while True:
        y = input("Enter the card's column number ")
        if y in ['1', '2', '3', '4']:
            return int(y)
        else:
            print("Invalid input ")

def boardDisplay(board) -> None:
    '''This func is displaying the board with print'''
    print('  1 2 3 4', end = '')
    x = '*'
    for i in range(4):
        print()
        print(f"{i+1} ", end= '')
        for j in range(4):
            if board[i,j]['flipped'] or board[i,j]['matched']:
                print(board[i,j]['card'], end='')
            else:
                print("* ",end='')
    print()
    print()

def cardsMatch(board, guess1, guess2) -> bool:
    '''this func checks if the cards match'''
    if board[guess1]['card'] == board[guess2]['card']:
        return True
    else:
        return False

def isBoardComplete(board) -> bool:
    '''This func checks if all the cards have been revealed'''
    for i in range(4):
        for j in range(4):
            if board[i,j]['matched']:
                continue
            else:
                return False
    return True
def replay() -> bool:
    '''This func checks if the user wants to play another game, using recursion with an answer other than yes or no '''
    print("You have won! ")
    ans = input("Do you wish to play again ? (yes or no) ")
    if ans.lower() == 'yes':
        print("Restarting the game...")
        initGame(4, 4, ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H'])
        initBoard(4, 4, ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H'])
        return True
    elif ans.lower() == 'no':
        print("Bye Bye! ")
        return False
    else:
        print("Invalid input, enter yes or no")
        replay()
def play(gameData) -> None:
    '''This func lets you run the game'''
    board = initBoard(4,4,['A ', 'A ', 'B ', 'B ', 'C ', 'C ', 'D ', 'D ', 'E ', 'E ', 'F ', 'F ', 'G ', 'G ', 'H ', 'H '])
    print(board)
    while True:
        if(isBoardComplete(board)):
            if replay():
                continue
            else:
                break
        boardDisplay(board)
        print(f"Its {gameData['turn']}'s turn")
        while True:
            print("Enter below the first card's position! ")
            guess1 = (getCardX()-1, getCardY()-1)
            if board[guess1]['flipped'] or board[guess1]['matched'] :
                print("This card has already been revealed ")
            else:
                break
        board[guess1]['flipped'] = True
        boardDisplay(board)
        while True:
            print("Enter below the second card's position! ")
            guess2 = (getCardX()-1, getCardY()-1)
            if board[guess2]['flipped'] or board[guess2]['matched']:
                print("This card has already been revealed ")
            else:
                break
        board[guess2]['flipped'] = True
        boardDisplay(board)
        #Cards matched
        if board[guess1]['card'] == board[guess2]['card']:
            print("You matched the cards! ")
            board[guess1]['matched'] = True
            board[guess2]['matched'] = True
            #Player 1
            if gameData['turn'] == 'player1':
                gameData['score']['player1'] += 1
                print("You have another turn! ")
            #Player 2
            else:
                gameData['score']['player2'] += 1
                print("You have another turn! ")
        # Cards not matched
        else:
            print("You didn't match the cards ")
            #Player 1
            if gameData['turn'] == 'player1':
                gameData['turn'] = 'player2'
                print(f"Now its {gameData['turn']}'s turn! ")
            else:
                gameData['turn'] = 'player1'
                print(f"Now its {gameData['turn']}'s turn! ")
        gameData['moveHistory'].extend([guess1, guess2])
        board[guess1]['flipped'] = False
        board[guess2]['flipped'] = False
    print("Thank you for playing! ")




