# tic-tac_toe project                                                           Andrew Evans

print("Welcome to tic-tac-toe!")
legend = "['7', '8', '9']\n['4', '5', '6']\n['1', '2', '3']"
playerMarker = " "

gameState = [[' ' for y in range(3)] for x in range(3)]
# print(gameState)

# function to print the board
def print_game_state(gameStateP):
    for i in range(3):
        print(gameStateP[i])

# function for determining mode
def modeParse(mode):
    global playerMarker
    if mode == 1:
        playerMarker = 'X'
        return 5
    elif mode == 2:
        playerMarker = 'O'
        return 4
    else:
        print("please choose either 1 or 2 for the mode")
        return -1


# functions for updating the gameState
def first():
    # update the gameState
    gameState[2][0] = playerMarker

def second():
    gameState[2][1] = playerMarker

def third():
    gameState[2][2] = playerMarker

def fourth():
    gameState[1][0] = playerMarker

def fifth():
    gameState[1][1] = playerMarker

def sixth():
   gameState[1][2] = playerMarker

def seventh():
    gameState[0][0] = playerMarker

def eighth():
    gameState[0][1] = playerMarker

def ninth():
    gameState[0][2] = playerMarker

# dictionary for game input states
inputDict = {1: first, 2: second, 3: third, 4: fourth, 5: fifth, 6: sixth, 7: seventh, 8: eighth, 9: ninth}
# Initial Board
print_game_state(gameState)

# determine number of user inputs
mode = input("Would you like to go first(enter 1) or second(enter 2)?\n")
# print(mode)
mFlag = modeParse(int(mode))
# print("please select an appropriate mode")
# print(legend)
# print(mFlag)
for j in range(mFlag):
    print(legend)
    print("")
    selection = input("Where would you like to mark?\n")
    inputDict[int(selection)]()
    print_game_state(gameState)
    print("")


