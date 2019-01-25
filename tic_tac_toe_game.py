#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 15:50:57 2018

@author: rj
"""

#Function for displaying thr board
def print_board(board):
    print('\n'*100)
    print('   ' + ' | ' + '  ' + ' | ')
    print('  ' + board[1] + ' | ' + board[2] + '  | ' + board[3])
    print('   ' + ' | ' + '  ' + ' | ')
    print("---------------")
    print('   ' + ' | ' + '  ' + ' | ')
    print('  ' + board[4] + ' | ' + board[5] + '  | ' + board[6])
    print('   ' + ' | ' + '  ' + ' | ')
    print("---------------")
    print('   ' + ' | ' + '  ' + ' | ')
    print('  ' + board[7] + ' | ' + board[8] + '  | ' + board[9])
    print('   ' + ' | ' + '  ' + ' | ')
    
#Function for taking the input from the player
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1  : Do you want to be X or O ? ').upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#Function for marking the symbol on the board
def place_marker(board,marker,position):
    board[position] = marker

#Function for checking if the player has won
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

import random
    
#Function for randomly choosing either of the player to play first
def choose_first():
    if random.randint(1,2) == 2:
        return 'Player 2'
    else:
        return 'Player 1'
    
#Function to check if space is available on the board
def space_check(board,position):
    
    return board[position] == ' '

#Function to check if the board is fully occupied
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#Function for taking input for position of marker on the board from player
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

#Function to ask the player if he/she wants to play the game
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


#################################################################################
    
print("************** WELCOME TO RJ'S GRAND TIC-TAC-TOE GAME ****************")

while True:
    #Reset the board
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    print(f"Player 1's symbol is {player1_marker}")
    print(f"Player 2's symbol is {player2_marker}")
    turn = choose_first()
    print (turn + ' will go first ..')
    
    play_game = input('Are you ready to play? Enter Yes or No : ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == 'Player 1':
            #Player1's turn
            
            print_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            
            if win_check(theBoard,player1_marker):
                print_board(theBoard)
                print('Congratulations! Player 1 have won the game..!!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    print_board(theBoard)
                    print("Oooohhh....The Game is a draw...Better luck next time ")
                    break
                else:
                    turn = 'Player 2'
        else:
            
            print_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            
            if win_check(theBoard,player2_marker):
                print_board(theBoard)
                print('Congratulations! Player 2 have won the game..!!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    print_board(theBoard)
                    print("Oooohhh....The Game is a draw...Better luck next time ")
                    break
                else:
                    turn = 'Player 1'
                    
    if not replay():
        break
        


    
    
    

    