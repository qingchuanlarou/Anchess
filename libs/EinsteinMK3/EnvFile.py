import numpy as np

counter = 1
win = 0
steps = 0
discount = 0.9
steps_r = 0
steps_b = 0
action_type = [0,1,2]
init_chess = [[-6,-2,-4,0,0],
              [-1,-5,0,0,0],
              [-3,0,0,0,3],
              [0,0,0,5,1],
              [0,0,4,2,6]]
init_loc_red = [[1,0],[0,1],[2,0],[0,2],[1,1],[0,0]]
init_loc_blue = [[3,4],[4,3],[2,4],[4,2],[3,3],[4,4]]
init_value_red = [4,2,2,2,4,3]
init_value_blue = [4,2,2,2,4,3]
init_value_board_red = [[1,2,2,2,2],[2,4,4,4,5],[2,4,8,8,10],[2,4,8,16,20],[2,5,10,20,32]]
init_value_board_blue = [[32,20,10,5,2],[20,16,8,4,2],[10,8,8,4,2],[5,4,4,4,2],[2,2,2,2,1]]
init_exist_red = [True,True,True,True,True,True]
init_exist_blue = [True,True,True,True,True,True]
init_prob_red = [1/6,1/6,1/6,1/6,1/6,1/6]
init_prob_blue = [1/6,1/6,1/6,1/6,1/6,1/6]

node_chess = [[-6,-2,-4,0,0],
              [-1,-5,0,0,0],
              [-3,0,0,0,3],
              [0,0,0,5,1],
              [0,0,4,2,6]]
node_loc_red = [[1,0],[0,1],[2,0],[0,2],[1,1],[0,0]]
node_loc_blue = [[3,4],[4,3],[2,4],[4,2],[3,3],[4,4]]
node_value_red = [4,2,2,2,4,3]
node_value_blue = [4,2,2,2,4,3]
node_value_board_red = [[1,2,2,2,2],[2,4,4,4,5],[2,4,8,8,10],[2,4,8,16,20],[2,5,10,20,32]]
node_value_board_blue = [[32,20,10,5,2],[20,16,8,4,2],[10,8,8,4,2],[5,4,4,4,2],[2,2,2,2,1]]
node_exist_red = [True,True,True,True,True,True]
node_exist_blue = [True,True,True,True,True,True]
node_prob_red = [1/6,1/6,1/6,1/6,1/6,1/6]
node_prob_blue = [1/6,1/6,1/6,1/6,1/6,1/6]


def init():
    global node_chess
    global node_loc_red
    global node_loc_blue
    global node_value_red
    global node_value_blue
    global node_exist_red
    global node_exist_blue
    global node_prob_red
    global node_prob_blue
    global init_loc_red
    global init_loc_blue
    global init_value_red
    global init_value_blue
    global init_exist_red
    global init_exist_blue
    global init_prob_red
    global init_prob_blue

    i,j = 0,0
    while i < 5:
        while j < 5:
            node_chess[i][j] = init_chess[i][j]
            j += 1
        j = 0
        i += 1

    ax = 0
    while ax <= 5:
        node_loc_red[ax] = init_loc_red[ax]
        node_loc_blue[ax] = init_loc_blue[ax]
        node_value_red[ax] = init_value_red[ax]
        node_value_blue[ax] = init_value_blue[ax]
        node_exist_red[ax] = init_exist_red[ax]
        node_exist_blue[ax] = init_exist_blue[ax]
        node_prob_red[ax] = init_prob_red[ax]
        node_prob_blue[ax] = init_prob_blue[ax]
        ax += 1

def calculate_information(board):
    global node_loc_red
    global node_loc_blue
    global node_value_red
    global node_value_blue
    global node_exist_red
    global node_exist_blue
    global node_value_board_red
    global node_value_board_blue
    node_loc_red = [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
    node_loc_blue = [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
    node_value_red = [0,0,0,0,0,0]
    node_value_blue = [0,0,0,0,0,0]
    node_exist_red = [False,False,False,False,False,False]
    node_exist_blue = [False,False,False,False,False,False]
    ax = 0
    ay = 0
    while(ax <= 4):
        while(ay <= 4):
            if(board[ax][ay] < 0):
                chess = -board[ax][ay] - 1
                node_loc_red[chess] = [ax,ay]
                if chess == 0 or chess == 5:
                    node_value_red[chess] = node_value_board_red[ax][ay] + 2
                else:
                    node_value_red[chess] = node_value_board_red[ax][ay]
                node_exist_red[chess] = True
            elif(board[ax][ay] > 0):
                chess = board[ax][ay] - 1
                node_loc_blue[chess] = [ax, ay]
                if chess == 0 or chess == 5:
                    node_value_blue[chess] = node_value_board_blue[ax][ay] + 2
                else:
                    node_value_blue[chess] = node_value_board_blue[ax][ay]
                node_exist_blue[chess] = True
            ay += 1
        ay = 0
        ax += 1
    probability(0)
    probability(1)

def available_action(chara,team):
    # 0:up/down 1:upleft/downright 2:left/right
    global node_loc_red
    global node_loc_blue
    if team == 1:
        clx = node_loc_blue[chara][0]
        cly = node_loc_blue[chara][1]
        if(clx == 0 and cly != 0):
            return [2]
        elif(cly == 0 and clx != 0):
            return [0]
        else:
            return [0,1,2]
    else:
        clx = node_loc_red[chara][0]
        cly = node_loc_red[chara][1]
        if (clx == 4 and cly != 4):
            return [2]
        elif (cly == 4 and clx != 4):
            return [0]
        else:
            return [0, 1, 2]

#这个函数用于判断是否结束比赛
def judge(board, exist_red, exist_blue):
    if(board[0][0] > 0):
        return 1
    if(board[4][4] < 0):
        return -1

    found_true_red = False
    found_true_blue = False
    for r in exist_red:
        if r == True:
            found_true_red = True
            break
    for b in exist_blue:
        if b == True:
            found_true_blue = True
            break
    if found_true_red == False:
        return 1
    if found_true_blue == False:
        return -1
    return 0

#这个函数用于决定那个棋子可以用于行动
def avaliable(action,team):
    global node_exist_red
    global node_exist_blue
    upper = -1;
    lower = -1;
    if(team == 1):
        exist_array = node_exist_blue
    else:
        exist_array = node_exist_red
    if exist_array[action] == True:
        return action,action
    if action == 0:
        temp = action
        while temp <= 5:
            if(exist_array[temp] == True):
                upper = temp
                return upper,lower
            temp += 1
    if action == 5:
        temp = action
        while temp >= 0:
            if (exist_array[temp] == True):
                lower = temp
                return upper,lower
            temp -= 1
    temp = action
    while temp <= 5:
        if(temp >= 5 and exist_array[temp] == False):
            break
        if(exist_array[temp] == True):
            upper = temp
            break
        temp += 1
    temp = action
    while temp >= 0:
        if (temp <= 0 and exist_array[temp] == False):
            break
        if (exist_array[temp] == True):
            lower = temp
            break
        temp -= 1
    return upper,lower

#这个函数用于计算概率
def probability(team):
    global node_exist_red
    global node_exist_blue
    global node_chess
    if judge(node_chess,node_exist_red,node_exist_blue) != 0:
        return [1,1,1,1,1,1]
    if (team == 1):
        exist_array = node_exist_blue
    else:
        exist_array = node_exist_red
    count = [0,0,0,0,0,0]
    i = 0
    while(i <= 5):
        if(exist_array[i]==True):
            count[i] += 1
            temp = i
            if(temp > 0): #是否可以向左寻找
                while(temp >= 5):
                    if(exist_array[temp]==False):
                        count[i] += 1
                    temp -= 1
            temp = i
            if(temp < 5): #是否可以向右寻找
                while(temp <= 5):
                    if(exist_array[temp]==False):
                        count[i] += 1
                    temp += 1
        i += 1
    i = 0
    sum_ = 0
    while i <= 5:
        sum_ += count[i]
        i += 1
    i = 0
    while i <= 5:
        count[i] = count[i]/sum_
        i += 1
    return count


def reward_system(team,src_loc,dst_loc):
    global node_value_red
    global node_value_blue
    global node_value_board_red
    global node_value_board_blue
    if team == 1:
        return node_value_board_blue[dst_loc[0]][dst_loc[1]] - node_value_board_blue[src_loc[0]][src_loc[1]]
    else:
        return node_value_board_red[dst_loc[0]][dst_loc[1]] - node_value_board_red[src_loc[0]][src_loc[1]]

def float2int(node):
    ax = 0
    ay = 0
    while(ax <= 4):
        while(ay <= 4):
            node[ax][ay] = int(node[ax][ay])
            ay += 1
        ax += 1
        ay = 0

#这个函数用于计算是那一方行动 0:我方 1：对方
def which_act(rounds):
    return rounds % 2

#这个函数用来决定那个棋子行动
def whoaction():
    temp = np.random.randint(0,1200)
    return temp % 6

def step(action,chara,team,state):
    global node_loc_red
    global node_loc_blue
    global node_value_red
    global node_value_blue
    global node_exist_red
    global node_exist_blue
    global node_value_board_red
    global node_value_board_blue
    global node_chess
    global win
    global steps
    global steps_b
    global steps_r
    global discount
    global counter
    #action: 0 1 2
    #0:up/down 1:upleft/downright 2:left/right
    #chara: 0 1 2 3 4 5 team:1 blue 0 red
    #current_map = state[0][0:25]
    #current_map = np.reshape(current_map,[5,5])
    #current_map = current_map.tolist()
    current_map = np.reshape(state,[5,5])
    node_chess = []
    for v in current_map:
        node_chess.append(v)
    float2int(node_chess)
    calculate_information(node_chess)
    value1 = Value_count(team)
    dstx = 5
    dsty = 5
    clx = 5
    cly = 5
    if team == 1:
        steps += 1
        steps_b += 1
        clx = node_loc_blue[chara][0]
        cly = node_loc_blue[chara][1]
        if(action == 0):
            dstx = clx - 1
            dsty = cly
        elif(action == 1):
            dstx = clx - 1
            dsty = cly - 1
        elif(action == 2):
            dstx = clx
            dsty = cly - 1
        else:
            print('error 380')
    else:
        steps_r += 1
        clx = node_loc_red[chara][0]
        cly = node_loc_red[chara][1]
        if (action == 0):
            dstx = clx + 1
            dsty = cly
        elif (action == 1):
            dstx = clx + 1
            dsty = cly + 1
        elif (action == 2):
            dstx = clx
            dsty = cly + 1
        else:
            print('error 395')
    current_map[dstx][dsty] = current_map[clx][cly]
    current_map[clx][cly] = 0

    calculate_information(current_map)
    value2 = Value_count(team)
    reward = reward_system(team,[clx,cly],[dstx,dsty]) + value2 - value1
    rew_r = 0
    rew_b = 0
    done = False
    node_chess = []
    for v in current_map:
        node_chess.append(v)
    float2int(node_chess)
    result = getenv(chara,team)
    if team == 1:
        rew_b = reward * (discount)**steps_b
    else:
        rew_r = reward * (discount)**steps_r
    if judge(current_map,node_exist_red,node_exist_blue) == 1:
        init()
        result = np.reshape(node_chess, [1, 25]).tolist()
        win += 1
        counter += 1
        rew_b += 50
        rew_r = -50
        done = True
        steps_b = 0
        steps_r = 0
    elif judge(current_map,node_exist_red,node_exist_blue) == -1:
        init()
        result = np.reshape(node_chess,[1,25]).tolist()
        counter += 1
        rew_r += 50
        rew_b = -50
        done = True
        steps_b = 0
        steps_r = 0
    return result, rew_r, rew_b, done

def Value_count(team):
    global node_exist_red
    global node_exist_blue
    global node_value_blue
    global node_value_red
    global node_prob_blue
    global node_prob_red
    value = 0
    if team == 1:
        i = 0
        while i <= 5:
            if(node_exist_blue[i] == True):
                value += node_prob_blue[i] * node_value_blue[i]
            i += 1
        i = 0
        while i <= 5:
            if(node_exist_red[i] == True):
                value -= node_prob_red[i] * node_value_red[i]
            i += 1
    else:
        i = 0
        while i <= 5:
            if (node_exist_blue[i] == True):
                value -= node_prob_blue[i] * node_value_blue[i]
            i += 1
        i = 0
        while i <= 5:
            if (node_exist_red[i] == True):
                value += node_prob_red[i] * node_value_red[i]
            i += 1
    return value

def getenv(chara,team):
    global node_loc_red
    global node_loc_blue
    global node_value_red
    global node_value_blue
    global node_exist_red
    global node_exist_blue
    global node_prob_red
    global node_prob_blue
    locx = []
    locy = []
    prob = []
    value = []
    if team == 1:
        locx = node_loc_blue[chara][0]
        locy = node_loc_blue[chara][1]
        prob = node_prob_blue[chara]
        value = node_value_blue[chara]
    else:
        locx = node_loc_red[chara][0]
        locy = node_loc_red[chara][1]
        prob = node_prob_red[chara]
        value = node_value_red[chara]
    data = np.reshape(node_chess,[1,25])
    data = data.tolist()
    return data