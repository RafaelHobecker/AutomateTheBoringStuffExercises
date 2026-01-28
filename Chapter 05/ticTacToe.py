
theBoard = {'top-L': ' ', 'top-M': ' ','top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def checkWin(board,player):
    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or  #Fila Arriba
            (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or  #Fila Medio
            (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or  #Fila Abajo
            (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or  #Columna Izq
            (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or  # Columna Medio
            (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or  # Columna Derecha
            (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or  # Diagonal 1
            (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player)   # Diagonal 2
            )

turn = 'X'

for i in range(9):
    printBoard(theBoard)

    move = ''

    while True:
        print('Turn for ' + turn + '. Move on which space?')
        move = input()

        # 1. Existe la casilla?
        if move not in theBoard:
            print("Invalid move. Use the format 'top-L','mid-M',etc.")
            continue
        # 2. Está vacía?
        if theBoard[move] != ' ':
            print("Marked move. Choose another move!!")
            continue
        # Si pasa ambas pruebas, salimos del bucle de pregunta
        break
    #Marcamos Casilla

    theBoard[move] = turn

    #Comprobar Victoria

    if checkWin(theBoard,turn):
        printBoard(theBoard)
        print('Congratulations! The player ' + turn + ' wins!')
        break

    # Comprobar Empate
    if i==8:
        printBoard(theBoard)
        print('It is a draw!!')

    # Cambiar de Turno
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'



printBoard(theBoard)
