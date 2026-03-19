current_player = 0
game_status = []
symbols = [" ", "X", "O"]
win_conditions = []

def changeStatus(pos, player_number):
    if game_status[pos] == 0:
        game_status[pos] = player_number
        return True
    return False

def checkStatus():
    pass

def getGameInput():
    change_happened = False
    while change_happened == False:
        input_text = "Please chose your position as an int, player " + symbols[current_player]
        game_input = int(input(input_text))
        change_happened = changeStatus(game_input-1, current_player)

def main():
    game_has_ended = False
    global current_player
    current_player = 1
    setUpStatus()
    while game_has_ended == False:
        getGameInput()
        switchCurrentPlayer()
        game_has_ended = checkStatus()
        showGameBoard()
    showGameResult()

def setUpStatus():
    global game_status
    game_status = []
    for i in range(9):
        game_status.append(0)

def showGameBoard():
    if len(game_status) == 9:
        print(symbols[game_status[0]] + symbols[game_status[1]] + symbols[game_status[2]])
        print(symbols[game_status[3]] + symbols[game_status[4]] + symbols[game_status[5]])
        print(symbols[game_status[6]] + symbols[game_status[7]] + symbols[game_status[8]])
    else:
        print("Error - game_status has not enough values to show.")

def showGameResult():
    pass

def switchCurrentPlayer():
    global current_player
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1

main()