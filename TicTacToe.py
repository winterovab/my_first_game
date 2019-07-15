import random

def display_board(board):
    print('  |   |  ')
    print(board[7] + ' | ' + board[8] + ' | '+ board[9])
    print('  |   |  ')
    print(board[4] + ' | ' + board[5] + ' | '+ board[6])
    print('  |   |  ')
    print(board[1] + ' | ' + board[2] + ' | '+ board[3])
    print('  |   |  ')

def select_symbol():
    #select symbol
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Please pick a marker 'X' or 'O': ")
    player1 = marker
    
    if player1 == 'O':
        player2 = 'X'
    else:
        player2 = 'O'
    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark): 
    return (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark) or (board[3] == mark and board[6] == mark and board[9] == mark) or (board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[1] == mark and board[5] == mark and board[9] == mark) or (board[3] == mark and board[5] == mark and board[7] == mark)

def choose_first():
    num = random.randint(1,2) 
    if num == 1:
        first_player = 'X'
    else:
        first_player = 'O'
    return first_player

def is_empty(board, position):
    return board[position] == ' '

def full_board_check(board):
    for item in board:
        if item == ' ':
            return False
    return True

def player_choice(board):
    next_pos = 0
    while next_pos not in range(1,10):
        next_pos = int(input("Please enter next position: "))
        if is_empty(board, next_pos):
            return next_pos
        next_pos = 0

def replay():
    next_game = ''
    while next_game != 'Yes' or next_game != 'No':
        next_game = input("Would you like to play again: ")
        if next_game.lower() == 'yes':
            return True
        if next_game.lower() == 'no':
            return False

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = ['@',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board)
    #determine symbols for each player
    print("Please choose a symbol for player 1: ")
    player1, player2 = select_symbol()
    #determine first player
    current_player = choose_first()
    print("First Player " + current_player)

    while True:
        #1. Accept user imput
        position = player_choice(board)
        #2. Place a marker
        place_marker(board, current_player, position)
        #3. Display updated board
        display_board(board)
        #4. Check if the current player won
        if win_check(board, current_player):
            print(current_player + " won")
            break
        #5. Check for a tie
        if full_board_check(board):
            print("It's a tie")
            break
        #6. Next player's turn
        if current_player == 'O':
            current_player = 'X'
        else:
            current_player = 'O'

    if not replay():
        break


