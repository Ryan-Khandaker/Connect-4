board2 = [['-', '-','-', '-', '-','-', '-'], 
          ['-', '-','-', '-', '-','-', '-'], 
          ['-', '-','-', '-', '-','-', '-'], 
          ['-', '-','-', '-', '-','-', '-'], 
          ['-', '-','-', '-', '-','-', '-'], 
          ['-', '-','-', '-', '-','-', '-'], 
          ['-', '-','-', '-', '-','-', '-']]
current_player = 'X'
score_count={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
game_running = True
winner = None

#initilizing the board
def boardd():
    print (board2 [0][0] + '|' + board2[0][1] + '|' + board2[0][2] + '|' + board2[0][3] + '|' + board2[0][4] + '|' + board2[0][5] + '|' + board2[0][6])
    print ("-------------")
    print (board2 [1][0] + '|' + board2[1][1] + '|' + board2[1][2] + '|' + board2 [1][3] + '|' + board2[1][4] + '|' + board2[1][5] + '|' + board2[1][6])
    print ("-------------")
    print (board2 [2][0] + '|' + board2[2][1] + '|' + board2[2][2] + '|' + board2 [2][3] + '|' + board2[2][4] + '|' + board2[2][5] + '|' + board2[2][6])
    print ("-------------")
    print(board2 [3][0] + '|' + board2[3][1] + '|' + board2[3][2] + '|' + board2 [3][3] + '|' + board2[3][4] + '|' + board2[3][5] + '|' + board2[3][6])
    print ("-------------")
    print(board2 [4][0] + '|' + board2[4][1] + '|' + board2[4][2] + '|' + board2 [4][3] + '|' + board2[4][4] + '|' + board2[4][5] + '|' + board2[4][6])
    print ("-------------")
    print(board2 [5][0] + '|' + board2[5][1] + '|' + board2[5][2] + '|' + board2[5][3] + '|' + board2[5][4] + '|' + board2[5][5] + '|' + board2[5][6])
    print ("-------------")
    print(board2 [6][0] + '|' + board2[6][1] + '|' + board2[6][2] + '|' + board2[6][3] + '|' + board2[6][4] + '|' + board2[6][5] + '|' + board2[6][6])
    print ("-------------")
    print('1' + '|' + '2' + '|' + '3' + '|' + '4' + '|' + '5' + '|' '6' + '|' + '7')

#player input
def Playerinput():
    global current_player
    while True:
        try:
            inp = int(input('Insert an integer from 1-7: '))
            n = score_count[inp]
            break
        except KeyError:
            print('Enter an integer from 1-7 ')
        except ValueError:
            print('Enter a valid number')
    
    if board2[6-n][inp-1] == '-':
        board2[6-n][inp-1]=current_player
        score_count[inp]+=1
    else:
        print('Invalid entry')
        swich_player()


#switching players
def swich_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player ='X'

#win and tie conditions

def win_diag(board):
    global winner
    global game_running
    for i in range(0, 4):
        if board[i][i]==board[i+1][i+1]==board[i+2][i+2]==board[i+3][i+3] and board[i][i]!='-':
            winner = board[i][i]
        
        elif board[6-i][i]==board[5-i][i+1]==board[4-i][i+2]==board[3-i][i+3] and board[6-i][i]!='-':
            winner = board[6-i][i]

    for k in range(0, 3):
        if board[k][k+1]==board[k+1][k+2]==board[k+2][k+3]==board[k+3][k+4] and board[k][k+1]!='-':
            winner = board[k][k+1]

        elif board[k+1][k]==board[k+2][k+1]==board[k+3][k+2]==board[k+4][k+3] and board[k+1][k]!='-':
            winner = board[k+1][k]
        
        elif board[5-k][k]==board[4-k][k+1]==board[3-k][k+2]==board[2-k][k+3] and board[5-k][k]!='-':
            winner = board[5-k][k]
        
        elif board[6-k][k+1]==board[5-k][k+2]==board[4-k][k+3]==board[3-k][k+4] and board[3-k][k+4]!='-':
            winner = board[3-k][k+4]
        
    for l in range(0, 2):
        if board[l][l+2]==board[l+1][l+3]==board[l+2][l+4]==board[l+3][l+5] and board[l][l+2]!='-':
            winner = board[l][l+2]

        elif board[l+2][l]==board[l+3][l+1]==board[l+4][l+2]==board[l+5][l+3] and board[l+2][l]!='-':
            winner = board[l+2][l]

        elif board[4-l][l]==board[3-l][l+1]==board[2-l][l+2]==board[1-l][l+3] and board[1-l][l+3]!='-':
            winner = board[1-l][l+3]

        elif board[6-l][l+2]==board[5-l][l+3]==board[4-l][l+4]==board[3-l][l+5] and board[3-l][l+5]!='-':
            winner = board[3-l][l+5]

    if board[0][3]==board[1][4]==board[2][5]==board[3][6] and board[2][5]!='-':
        winner = board[2][5]

    elif board[3][0]==board[4][1]==board[5][2]==board[6][3] and board[5][2]!='-':
        winner = board[5][2]
    
    elif board[3][0]==board[2][1]==board[1][2]==board[0][3] and board[1][2]!='-':
        winner = board[1][2]

    elif board[6][3]==board[5][4]==board[4][5]==board[3][6] and board[4][5]!='-':
        winner = board[4][5]
    
    if winner!=None:
        print('The winner is', winner)
        game_running = False
    
def win_horizontal(board):
    global current_player
    global winner
    global game_running
    for h in range(6, -1, -1):
        lst = board[h]
        indices = [i for i, x in enumerate(lst) if x == current_player]
        if len(indices)>=4:
            consec = ranges(indices)
            if len(consec)==1:
                if (max(consec[0])-min(consec[0]))>=3:
                    winner = current_player
                    print ('The winner is', winner)
                    game_running = False
                    break
            elif len(consec)==2:
                if (max(consec[1])-min(consec[1]))>=3:
                    winner = current_player
                    print ('The winner is', winner)
                    game_running = False
                    break
def win_vertical(board):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    for j in range(6, -1, -1):
        list1.append(board[j][0])
        list2.append(board[j][1])
        list3.append(board[j][2])
        list4.append(board[j][3])
        list5.append(board[j][4])
        list6.append(board[j][5])
        list7.append(board[j][6])

    win_horizontal([list1, list2, list3, list4, list5, list6, list7])
    
#consecutive numbers check
def ranges(nums):
    nums = sorted(set(nums))
    gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
    edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
    return list(zip(edges, edges))

#check win and tie again

def tie(board):
    global game_running
    global current_player
    for number in range(0, 7):
        if board[0][number] == '-':
            break
    if number == 6:
        if board[0][number]!='-':
            board[0][number] = current_player
            game_running = False
            print ('It is a draw')
            
#run win and tie functions repeatedly    
while game_running:
    print (current_player + ' is to play')
    boardd()
    Playerinput()
    win_diag(board2)
    win_horizontal(board2)
    win_vertical(board2)
    tie(board2)
    swich_player()
    if not game_running:
        boardd()