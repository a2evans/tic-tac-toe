# tic-tac_toe project                                                           Andrew Evans
import random

print("Welcome to tic-tac-toe!")
legend = "['7', '8', '9']\n['4', '5', '6']\n['1', '2', '3']"
openStates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playerMarker = ' '
antiPlayerMarker = ' '

gameState = [[' ' for y in range(3)] for x in range(3)]


# function for checking if the selection is a non-open state

# function for choosing "ai(not yet)" moves

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
# Initial Board
print_game_state(gameState)

# determine number of user inputs
mode = input("Would you like to go first(enter 1) or second(enter 2)?\n")
mFlag = mode_parse(int(mode))

# check to see if comp should go first
if mode == '2':
    # have the comp make a turn
    firstMove = random.randint(1, 9)
    print("first move is: ", firstMove)
    stateChangeDict[firstMove](1)
    # print_game_state(gameState)
    openStates.remove(firstMove)

for j in range(mFlag):
    print(legend)
    print("")
    selection = input("Where would you like to mark?\n")
    stateChangeDict[int(selection)](0)
    openStates.remove(int(selection))
    print_game_state(gameState)
    print("")


