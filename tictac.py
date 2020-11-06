"""
Moja verzija iks-oks igrice. / prva verzija /
# resiti problem sa brojanjem kombinacija tako da se ne broje iste kad neki igrac napravi prvu kombinaciju
"""


gameboard = [
    ['','','',''],
    ['','','',''],
    ['','','',''],
    ['','','','']
]





def print_gameboard(gameboard):
    print(gameboard[0])
    print(gameboard[1])
    print(gameboard[2])
    print(gameboard[3])

print_gameboard(gameboard)

turn = 'X'
game_end = False
taken_places = 0

def three_in_a_row(gameboard):
    i = 0
    while i<4:
       if gameboard[x][y]== gameboard[1][0]== gameboard[i][1]==gameboard[i][2]== gameboard[i][3] and gameboard[x][i]!='' or\
                gameboard[x][y]== gameboard[0][i]== gameboard[1][i]== gameboard[2][i]== gameboard[3][i] and gameboard[1][i]!='' or\
                      gameboard[x][y]== gameboard[0][0]==gameboard[1][1]== gameboard[2][2]== gameboard[3][3] and gameboard[2][2]!='' or\
                          gameboard[x][y]== gameboard[0][3]==gameboard[1][2]== gameboard[2][1]== gameboard[3][0] and gameboard[3][0]!='':
                             print('Player', turn, 'made a combination. Great job!')
                             break
       else:
          i +=1
          continue




             
 
while not game_end:
    print('Player', turn, ' is on turn. Please input your coordinates. ')
    x = int(input())
    y = int(input())
    

    while (x>3 or y>3) or gameboard[x][y] != '':
        print('Ups. Wrong spot. Try again.')
        x = int(input())
        y = int(input())

    gameboard[x][y] = turn
    print_gameboard(gameboard)
    three_in_a_row(gameboard)
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    taken_places +=1
    if taken_places < 16:
        continue
    else:
        break
print('Game over!')

