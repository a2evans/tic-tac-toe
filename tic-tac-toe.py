# tic-tac_toe project                                                           Andrew Evans
import random
import time
import sys

print("Welcome to tic-tac-toe!")
legend = "['7', '8', '9']\n['4', '5', '6']\n['1', '2', '3']"
openStates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playerMarker = ' '
antiPlayerMarker = ' '

gameState = [[' ' for y in range(3)] for x in range(3)]


# function for checking if the selection is a non-open state
def selection_correct(select):
    # print(select in openStates)
    return select in openStates


# function to check if someone won
def did_win(gameStateP):
    win = False
    # check the rows
    for i in range(3):
        if ((gameStateP[i][0] == gameStateP[i][1] == gameStateP[i][2]) and
                (gameStateP[i][0] == gameStateP[i][1] == gameStateP[i][2] != ' ')):
            win = True
    # check the columns
    for j in range(3):
        if ((gameStateP[0][j] == gameStateP[1][j] == gameStateP[2][j]) and
                (gameStateP[0][j] == gameStateP[1][j] == gameStateP[2][j] != ' ')):
            win = True
    # check the diagonals
    if ((gameStateP[0][0] == gameStateP[1][1] == gameStateP[2][2]) and
            (gameStateP[0][0] == gameStateP[1][1] == gameStateP[2][2] != ' ')):
        win = True
    if ((gameStateP[2][0] == gameStateP[1][1] == gameStateP[0][2]) and
            (gameStateP[2][0] == gameStateP[1][1] == gameStateP[0][2] != ' ')):
        win = True
    return win


# function to print the board
def print_game_state(gameStateP):
    for i in range(3):
        print(gameStateP[i])
    print("")


# function for determining mode
def mode_parse(mode):
    global playerMarker
    global antiPlayerMarker
    if mode == 1:
        playerMarker = 'X'
        antiPlayerMarker = 'O'
        return 5
    elif mode == 2:
        playerMarker = 'O'
        antiPlayerMarker = 'X'
        return 4
    else:
        print("please choose either 1 or 2 for the mode")
        return -1


# functions for updating the gameState
def first(player):
    if player == 0:
        gameState[2][0] = playerMarker
    else:
        gameState[2][0] = antiPlayerMarker


def second(player):
    if player == 0:
        gameState[2][1] = playerMarker
    else:
        gameState[2][1] = antiPlayerMarker


def third(player):
    if player == 0:
        gameState[2][2] = playerMarker
    else:
        gameState[2][2] = antiPlayerMarker


def fourth(player):
    if player == 0:
        gameState[1][0] = playerMarker
    else:
        gameState[1][0] = antiPlayerMarker


def fifth(player):
    if player == 0:
        gameState[1][1] = playerMarker
    else:
        gameState[1][1] = antiPlayerMarker


def sixth(player):
    if player == 0:
        gameState[1][2] = playerMarker
    else:
        gameState[1][2] = antiPlayerMarker


def seventh(player):
    if player == 0:
        gameState[0][0] = playerMarker
    else:
        gameState[0][0] = antiPlayerMarker


def eighth(player):
    if player == 0:
        gameState[0][1] = playerMarker
    else:
        gameState[0][1] = antiPlayerMarker


def ninth(player):
    if player == 0:
        gameState[0][2] = playerMarker
    else:
        gameState[0][2] = antiPlayerMarker

# dictionary for game input states
stateChangeDict = {1: first, 2: second, 3: third, 4: fourth, 5: fifth, 6: sixth, 7: seventh, 8: eighth, 9: ninth}


# function for choosing "ai"(not yet) moves
def anti_player_move():
    move = random.choice(openStates)
    stateChangeDict[move](1)
    openStates.remove(move)
    print("Your opponent has chosen: ", move)
    print("")
    time.sleep(0.3)
    print_game_state(gameState)
    if did_win(gameState):
        print("The Computer has won")
        time.sleep(5)
        sys.exit(0)

# Initial Board
print_game_state(gameState)
# determine number of user inputs
mode = int(input("Would you like to go first(enter 1) or second(enter 2)?\n"))
mFlag = mode_parse(mode)

# check to see if comp should go first
if mode == 2:
    anti_player_move()


for i in range(mFlag):
    print(legend)
    print("")
    selection = int(input("Where would you like to mark?\n"))
    while not selection_correct(selection):
        selection = int(input("The selected input is occupied. Please select a new position\n"))
    # verify the selection
    stateChangeDict[selection](0)
    openStates.remove(selection)
    print_game_state(gameState)
    if did_win(gameState):
        print("You have won!!!!!")
        time.sleep(5)
        sys.exit(0)
    anti_player_move()

print("The game was a tie...")
time.sleep(5)
