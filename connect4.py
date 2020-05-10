import random
import tkinter 
print("\n"*10 +"Hello and welcome to Connect 4!")
# player1=input("Please choose the name for Player 1:   ")
# player2=input("Please choose the name for Player 2:   ")


testboard=[[' ']*7 for i in range(6)]
def showboard(board):
    print('|1|2|3|4|5|6|7| \n+-+-+-+-+-+-+-+')
    for x in board:
        print('|'+'|'.join(x)+'|')
def row_win_check(board):
    for i in board:
        if '1111' in ''.join(i):
            return True
        elif '2222' in ''.join(i):
            return True

def col_win_check(board):
    columns=[[' ']*6 for i in range(7)]
    #creates a list of columns, much like how board is a list of rows
    for i in range(0,7):
         for j in range(0,6):
            columns[i][j]=board[j][i]
    #now we can then apply the row_win_check code to the list of columns
    for i in columns:
        if '1111' in ''.join(i):
            return True
        elif '2222' in ''.join(i):
            return True
def diag_win_check(board):
    #for loops to find upward diagonal wins (left to right)
    for i in range(3,6): 
        for j in range(4):
            if board[i][j]==board[i-1][j+1]==board[i-2][j+2]==board[i-3][j+3]==('1' or '2'):
                
                return True
    for i in range(3,6):
        for j in range (3,7):
            if board[i][j]==board[i-1][j-1]==board[i-2][j-2]==board[i-3][j-3]==('1' or '2'):
                
                return True

def wincheck(board):
    checking=True
    while checking:
        if col_win_check(board):
            
            return True
                   
        elif row_win_check(board):           
            return True
            
        elif diag_win_check(board):
            return True
            
        else:
            return(False)
showboard(testboard)

def choose_slot():
    choice =' '
    while type(choice)!= int:
        try:
            choice=int(input("Please  choose where you would like to place your coin. Type a number from 1-7 where 1 is the leftmost position and 7 is the furthest to the right.    "))
        except:
            print("Please enter a number beween 1-7")
            continue
        break
    return(choice)
def correct_choice():
    choice=choose_slot()
    while(choice < 1 or choice > 7) :
        print("Please choose a number between 1 and 7 \n")
        choice=choose_slot()
    return(choice-1)

def place_coin(board, player):
    while True:
        choice=correct_choice()
        if board[0][choice]!=(" "):
            print("Sorry this column is full, please pick another")
            continue
        else:
            break
    vert_position=5
    while vert_position >=0:
        if board[vert_position][choice]!= ' ':
            vert_position-=1
            continue
        else:
            board[vert_position][choice]=player
            break
def fullboard_check(board):
    filled_spaces=0
    for x in range(6):
        for y in range(7):
            if board[x][y] !=" ":
                filled_spaces+=1
    return(filled_spaces)



playing =True
while playing:
    
    
    
    
    print('\n'*2)
    print("It's Player 1's go")
    
    place_coin(testboard,'1')
    showboard(testboard)
    
    if wincheck(testboard)==True:
        print("Player 1 wins")
        break
    print(fullboard_check(testboard))
    if fullboard_check(testboard) == 42:
        print("\n The board is full, the game is a draw!")
        break

    print("\n")
    print("It's Player 2's go")
    
    
    place_coin(testboard,'2')
    showboard(testboard)
    
    if wincheck(testboard) == True:
        print("Player 2 wins")
        break
    print(fullboard_check(testboard))
    if fullboard_check(testboard) == 42:
        print("\n The board is full, the game is a draw!")
        break
    continue