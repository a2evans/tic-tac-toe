# tic-tac_toe project                                                           Andrew Evans

print("Welcome to tic-tac-toe!")
gameState = [[0 for y in range(3)] for x in range(3)]
print(gameState)

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


print_game_state(gameState)
