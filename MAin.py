import numpy as np

player1Win = False
player2Win = False

game = [[0,1,1],
        [0,1,2],
        [0,1,2]]

def getGame(player=0,row=0,column=0):
    print('  ','0 ','1 ','2')
    for count,row in enumerate(game):
        print(count, row)

def move(game_map,player=0,row=0,column=0):
    game_map[row][column] = player
    return game_map

def checkEqual(lst):
   if lst.count(lst[0]) == len(lst) and lst[0] == 1:
       return 1
   if lst.count(lst[0]) == len(lst) and lst[0] == 2:
       return 2
   else:
       return False

def checkWin():
    global player1Win
    global player2Win

    for row in game:
        if checkEqual(row) == 1:
            print("player 1 wins")
            player1Win = True
        elif checkEqual(row) == 2:
            print("player 2 wins")
            player2Win = True
        else:
            print("nobody wins")


    for i in range(len(game[0])):
        col = []
        for row in game:
            col.append(row[i])
        if checkEqual(col) == 1:
            print("player 1 wins")
            player1Win = True
        elif checkEqual(col) == 2:
            print("player 2 wins")
            player2Win = True
        else:
            print("nobody wins")
    print(player1Win,player2Win)


globalPlayerCount = 'x'

#def makeMove():
 #   move[1]

move(game,1,0,0)
getGame()
checkWin()


