import random

def set_players():
    player1 = input("Please pick a marker 'X' or 'O'")
    player2 = input("Please pick a marker 'X' or 'O'")

def set_position():
    position = int(input('Please enter a number'))

def display_board(board):
    print('\n'*100)
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])

def  player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return(player1,player2)

def place_marker(board, marker, position):
    board[position] = marker
    return board

def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board [3] == mark:
        print(mark + " wins!")

def choose_first():

    first_player = random.randint(0,1)
    goes_first = "" 

    if first_player == 0:
        goes_first = "Player 1"
    else:
        goes_first = "Player 2"

    print(goes_first + " goes first")

    return goes_first

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose position 1-9: '))

    return position

def replay():
    choice = input("play again? enter yes or no")
    return choice

# while loop to keep running the game
print('Welcome to tic tac toe')

while True:
    # set up everything, board, who goes first, choose markers
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()

    print(turn + ' will go first')
    play_game = input('Ready to play? y or n')

    if play_game == 'y':
        game_on = True
    else: 
        game_on = False

    # gameplay player one turn, player two turn

    while game_on:

        if turn == 'Player 1':
            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won')
                game_on = False
            else: 
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)

            position = player_choice(the_board)
            
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won')
                game_on = False
            else: 
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
#break out of while loop on replay() function


#test_board = ['#', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
#place_marker(test_board, '$',8)
#display_board(test_board)
#win_check(test_board, 'X')
#choose_first()

