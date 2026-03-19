current_player = 0
game_status = []
symbols = [" ", "X", "O"]
win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
player_amount = 0 
winner = "no player"


def algorithm_move():
    algorithm_player_id = 2
    for condition in win_conditions:
        if game_status[condition[0]] == game_status[condition[1]] != 0 and game_status[condition[2]] == 0:
            changeStatus(condition[2], 2)
            return
        if game_status[condition[1]] == game_status[condition[2]] != 0 and game_status[condition[0]] == 0:
            changeStatus(condition[0], 2)
            return
        if game_status[condition[0]] == game_status[condition[2]] != 0 and game_status[condition[1]] == 0:
            changeStatus(condition[1], 2)
            return
    for i in range(9):
        if changeStatus(i, 2):
            return

def changeStatus(pos, player_number):
    if game_status[pos] == 0:
        game_status[pos] = player_number
        return True
    return False

def checkStatus():
    if(checkWin()):
        return True
    if(checkDraw()):
        return True
    return False
        
def checkWin():
    global winner
    for condition in win_conditions:
        if game_status[condition[0]] == game_status[condition[1]] == game_status[condition[2]] != 0:
            winner = "player " + symbols[game_status[condition[0]]]
            return True
    return False

def checkDraw():
    for i in game_status:
        if i == 0:
            return False
    return True


def getGameInput():
    change_happened = False
    while change_happened == False:
        input_text = "Please chose your position as an int, player " + symbols[current_player] + " "
        game_input = int(input(input_text))
        change_happened = changeStatus(game_input-1, current_player)

def main():
    game_has_ended = False
    global current_player
    current_player = 1
    setUpStatus()
    global player_amount
    player_amount = int(input("How many players are playing? (1 or 2)"))
    if player_amount == 1:
        while game_has_ended == False:
            getGameInput()
            algorithm_move()
            game_has_ended = checkStatus()
            showGameBoard()
    else:
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
    global winner
    print("Game has ended, " + winner + " wins!")   

def switchCurrentPlayer():
    global current_player
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1

main()