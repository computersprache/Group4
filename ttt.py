current_player = 0
game_status = []
symbols = [" ", "X", "O"]

def changeStatus(pos, player_number):
    if game_status[pos] == 0:
        game_status[pos] = player_number
        return True
    return False

def checkStatus():
    pass

def getGameInput():
    change_happend = False
    while change_happend == False:
        game_input = int(input("Please chose your position as an int, player %s", symbols[current_player]))
        change_happend = changeStatus(game_input-1, current_player)
    switchCurrentPlayer()

def setUpGame():
    pass

def setUpStatus():
    game_status = []
    for i in range(9):
        game_status.append(0)

def showGameBoard():
    if len(game_status) == 9:
        print(game_status[0] + game_status[1] + game_status[2])
        print(game_status[3] + game_status[4] + game_status[5])
        print(game_status[6] + game_status[7] + game_status[8])
    else:
        print("Error - game_status has not enough values to show.")

def switchCurrentPlayer():
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1