# tic-tac_toe project                                                           Andrew Evans

print("Welcome to tic-tac-toe!")
legend = "['7', '8', '9']\n['4', '5', '6']\n['1', '2', '3']"

# dictionary for game input states
inputDict = {1 : ,}

gameState = [[0 for y in range(3)] for x in range(3)]
# print(gameState)

# function to print the board
def print_game_state(gameStateP):
    gameStateTemp = gameStateP

    for x in range(3):
        for y in range(3):
            if(gameStateTemp[x][y] == 1):
                gameStateTemp[x][y] = "O"
            elif(gameStateTemp[x][y] == -1):
                gameStateTemp = "X"
            else:
                gameStateTemp[x][y] = " "

    for i in range(3):
        print(gameStateTemp[i])

# function for determining mode
def modeParse(mode):
    if mode == 1:
        return 5
    elif mode == 2:
        return 4
    else:
        print("please choose either 1 or 2 for the mode")
        return -1


# functions for the user's possible inputs

# Initial Board
print_game_state(gameState)

# determine number of user inputs
mode = input("Would you like to go first(enter 1) or second(enter 2)?\n")
print(mode)
mFlag = modeParse(int(mode))
# print("please select an appropriate mode")
print(legend)
# print(mFlag)
for j in range(mFlag):
    print(legend)
    selection = input("Where would you like to mark?\n")



