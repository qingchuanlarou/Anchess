import numpy as np
import libs.EinsteinMK3.EnvFile as env

BOARD = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]
Reward_map_red = [[0, 0, 0, 0, 0],
                  [0, 4, 4, 4, 0],
                  [0, 4, 8, 8, 10],
                  [0, 4, 8, 16, 20],
                  [0, 0, 10, 20, 40]]

Reward_map_blue = [[40, 20, 10, 0, 0],
                  [ 20, 16,  8, 4, 0],
                  [ 10,  8,  8, 4, 0],
                  [  0,  4,  4, 4, 0],
                  [  0,  0,  0, 0, 0]]
decay_rate = 0.4
decay_rate_nodes = 0.1
prior_rate_positive = 1.25
prior_rate_negative = 0.75 #如果执行了特殊处理 正的就增加，负的就减少

blue_win = 0
Enter = 4
BLUE = True
RED = False
LocRed = [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
LocBlue = [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
blueprobability = [1/6,1/6,1/6,1/6,1/6,1/6]
blueprobabilityflag = [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
bluevalue = [-1,-1,-1,-1,-1,-1]
bluethreaten = [-1,-1,-1,-1,-1,-1]
redprobability = [1/6,1/6,1/6,1/6,1/6,1/6]
redprobabilityflag = [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
redthreaten = [-1,-1,-1,-1,-1,-1]
redvalue = [-1,-1,-1,-1,-1,-1]
flag4 = 0
DEP = 3
a_ = 3.0
b_ = 1.0
c_ = 0.2  # 选择回报率和遍历的深度 a,b,c是一个常数
d_ = 0.0
infinity = 100

def Prior(team,temp1,temp2):
    global bluevalue
    global redvalue
    i,j = 0,0
    #这里是确认位置，方便对DesignatedProcess进行操作
    loctemp1 = [-1,-1]
    loctemp2 = [-1,-1]
    emptyboard = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    while i < 5:
        while j < 5:
            if team and env.node_chess[i][j] == temp1 + 1:
                loctemp1 = [i,j]
            elif team and env.node_chess[i][j] == temp2 + 1:
                loctemp2 = [i,j]
            if not team and -env.node_chess[i][j] == temp1 + 1:
                loctemp1 = [i, j]
            elif not team and -env.node_chess[i][j] == temp2 + 1:
                loctemp2 = [i, j]
            if team:
                emptyboard[i][j] = env.node_chess[i][j]
            elif not team:
                emptyboard[i][j] = -env.node_chess[4-i][4-j]
            j += 1
        j = 0
        i += 1

    if team:
        Execuate1,_,reward1 = DesignatedProcess(loctemp1,emptyboard)
        Execuate2,_,reward2 = DesignatedProcess(loctemp2,emptyboard)
        #如果都满足
        if Execuate1 and Execuate2:
            if reward1 > reward2:
                return temp1
            else:
                return temp2
        #如果只满足一个条件
        if Execuate1 and reward1 > reward2:
            return temp1
        if Execuate2 and reward2 > reward1:
            return temp2

        v1,v2 = bluevalue[temp1],bluevalue[temp2]
        if v1 > v2:
            return temp1
        else:
            return temp2
    else:
        Execuate1, _, reward1 = DesignatedProcess(loctemp1, emptyboard)
        Execuate2, _, reward2 = DesignatedProcess(loctemp2, emptyboard)
        # 如果都满足
        if Execuate1 and Execuate2:
            if reward1 > reward2:
                return temp1
            else:
                return temp2
        # 如果只满足一个条件
        if Execuate1:
            return temp1
        if Execuate2:
            return temp2


        v1, v2 = redvalue[temp1], redvalue[temp2]
        if v1 > v2:
            return temp1
        else:
            return temp2

#这个函数用于计算概率
def Probability(team):
    global BOARD
    B,R = Judge()
    if B and R:
        return [1,1,1,1,1,1]
    exist_array = [False,False,False,False,False,False]
    i,j = 0,0

    while i < 5:
        while j < 5:
            if BOARD[i][j] > 0 and team:
                exist_array[BOARD[i][j] - 1] = True
            elif BOARD[i][j] < 0 and not team:
                exist_array[-BOARD[i][j] - 1] = True
            j += 1
        j = 0
        i += 1

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

def BlueProbability():
    global blueprobability
    global BOARD
    global redvalue
    global bluevalue
    global blueprobabilityflag
    global bluethreaten
    global redprobability
    global redprobabilityflag
    global redthreaten
    bluedistancerate = [0, 0, 0, 0, 0, 0]
    blueprobability = [0, 0, 0, 0, 0, 0]
    blueprobabilityflag = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    bluevalue = [-1,-1,-1,-1,-1,-1]
    redvalue = [-1,-1,-1,-1,-1,-1]
    bluethreaten = [0, 0, 0, 0, 0, 0]

    i,j = 0,0
    while i < 5: #这个代码段是在计算红方的每个棋子的价值
        while j < 5:
            if (BOARD[i][j] < 0):
                redvalue[-BOARD[i][j] - 1] = Reward_map_red[i][j]
            j += 1
        j = 0
        i += 1

    i,j = 0,0
    while i < 5:
        while j < 5:
            if (BOARD[i][j] > 0): #这里是对蓝色棋子进行设定价值和是否存在
                #以下代码均是做相同的工作
                bluevalue[BOARD[i][j] - 1] = Reward_map_blue[i][j]
                blueprobabilityflag[BOARD[i][j] - 1][0] = 1 #如果存在为1
                a = 0
                b = 0
                c = 0
                if (j - 1 >= 0 and BOARD[i][j - 1] < 0):
                    a = redvalue[-BOARD[i][j-1]-1]
                if (i - 1 >= 0 and j - 1 >= 0 and BOARD[i-1][j-1] < 0):
                    b = redvalue[-BOARD[i-1][j-1]-1]
                if (i - 1 >= 0 and BOARD[i-1][j] < 0):
                    c = redvalue[-BOARD[i-1][j]-1]
                temp=max(a, b)
                temp=max(temp, c)
                bluethreaten[BOARD[i][j]-1]=temp #用红方的棋子价值来评估威胁值
            j += 1
        j = 0
        i += 1

    # if redvalue[0] != -1:
    #     redvalue[0] += 2
    # if redvalue[5] != -1:
    #     redvalue[5] += 2
    # if bluevalue[0] != -1:
    #     bluevalue[0] += 2
    # if bluevalue[5] != -1:
    #     bluevalue[5] += 2

    distancerate = 0
    i,j = 0,0
    while i < 5: #这里是在设定优先度
        j = 0
        while j < i:
            if (BOARD[i][j] > 0):
                bluedistancerate[distancerate] = BOARD[i][j]
                distancerate += 1
            j += 1
        j = i
        while j > 0:
            if(BOARD[j - 1][i] > 0):
                bluedistancerate[distancerate] = BOARD[j - 1][i]
                distancerate += 1
            j -= 1
        i += 1
    sum_ = 0
    i = 0
    while i < 6: #越靠近对方老家，行动概率越大，优先度越高
        if (bluedistancerate[i] > 0):
            num = bluedistancerate[i] - 1
            while (num > 0 and blueprobabilityflag[num][0] == 0 and blueprobabilityflag[num][1] == 0):
                sum_ += 1
                blueprobabilityflag[num][1] = 1
                num -= 1
            num = bluedistancerate[i] - 1
            while (num < 5 and blueprobabilityflag[num][0] == 0 and blueprobabilityflag[num][1] == 0):
                sum_ += 1
                blueprobabilityflag[num][1] = 1
                num += 1
            num = bluedistancerate[i] - 1
            sum_ += 1
            blueprobabilityflag[num][1] = 1
            blueprobability[num] = sum_ / 6.0
            sum_ = 0
        i += 1

#这里和BlueProbability一样的功能 不再详细阐述
def RedProbability():
    global redprobability
    global redprobabilityflag
    global redvalue
    global bluevalue
    global redthreaten
    global BOARD
    reddistancerate = [0, 0, 0, 0, 0, 0]
    redprobability = [0, 0, 0, 0, 0, 0]
    redprobabilityflag = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    bluevalue = [-1,-1,-1,-1,-1,-1]
    redvalue = [-1,-1,-1,-1,-1,-1]
    redthreaten = [0,0,0,0,0,0]

    i,j = 0,0
    while i < 5:
        while j < 5:
            if (BOARD[i][j] > 0):
                bluevalue[BOARD[i][j] - 1] = Reward_map_blue[i][j]
            j += 1
        j = 0
        i += 1

    i,j = 0,0
    while i < 5:
        while j < 5:
            if (BOARD[i][j] < 0):
                redprobabilityflag[-BOARD[i][j] - 1][0] = 1
                redvalue[-BOARD[i][j] - 1] = Reward_map_red[i][j]
                a,b,c = 0,0,0
                if (j + 1 < 5 and BOARD[i][j + 1] > 0):
                    a = bluevalue[BOARD[i][j+1]-1]
                if (i + 1 < 5 and j + 1 < 5 and BOARD[i+1][j+1] > 0):
                    b = bluevalue[BOARD[i+1][j+1]-1]
                if (i + 1 < 5 and BOARD[i+1][j] > 0):
                    c = bluevalue[BOARD[i+1][j]-1]
                temp = max(a, b)
                temp = max(temp, c)
                redthreaten[-BOARD[i][j]-1] = temp
            j += 1
        j = 0
        i += 1

    # if redvalue[0] != -1:
    #     redvalue[0] += 2
    # if redvalue[5] != -1:
    #     redvalue[5] += 2
    # if bluevalue[0] != -1:
    #     bluevalue[0] += 2
    # if bluevalue[5] != -1:
    #     bluevalue[5] += 2

    distancerate = 0
    i,j = 4,4
    while i >= 0:
        j = 4
        while j >= i:
            if (BOARD[i][j] < 0):
                reddistancerate[distancerate] = BOARD[i][j]
                distancerate += 1
            j -= 1
        j = i
        while j < 4:
            if (BOARD[j + 1][i] < 0):
                reddistancerate[distancerate] = BOARD[j + 1][i]
                distancerate += 1
            j += 1
        i -= 1
    sum_ = 0
    i = 0
    while i < 6:
        if (-reddistancerate[i] > 0):
            num = -reddistancerate[i] - 1
            while (num > 0 and redprobabilityflag[num][0] == 0 and redprobabilityflag[num][1] == 0):
                sum_ += 1
                redprobabilityflag[num][1] = 1
                num -= 1
            num = -reddistancerate[i] - 1
            while (num < 5 and redprobabilityflag[num][0] == 0 and redprobabilityflag[num][1] == 0):
                sum_ += 1
                redprobabilityflag[num][1] = 1
                num += 1
            num = -reddistancerate[i] - 1
            sum_ += 1
            redprobabilityflag[num][1] = 1
            redprobability[num] = sum_ / 6.0
            sum_ = 0
        i += 1

def Judge(board):
    global infinity
    i,j = 0,0
    BlueFail, RedFail = True,True
    if board[0][0] > 0:
        return not BlueFail, RedFail
    elif board[4][4] < 0:
        return BlueFail, not RedFail
    while i < 5:
        while j < 5:
            if board[i][j] < 0 and RedFail:
                RedFail = False
            elif board[i][j] > 0 and BlueFail:
                BlueFail = False
            j += 1
        j = 0
        i += 1
    return BlueFail, RedFail

def DesignatedProcess(loc, board_input):
    global infinity
    global BOARD
    global flag4
    x,y = loc[0],loc[1]

    board = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]
    itemp, jtemp = 0, 0
    while itemp < 5:
        while jtemp < 5:
            board[itemp][jtemp] = BOARD[itemp][jtemp]
            BOARD[itemp][jtemp] = board_input[itemp][jtemp]
            jtemp += 1
        jtemp = 0
        itemp += 1

    n,m,num1 = 5,0,0
    while n > 0:
        n -= 1
        j = m
        while j < 5:
            if BOARD[j][n] < 0:
                num1 += 1  # 当前位置之前计算还有多少对方的棋子
            j += 1
        m += 1

    i,j,num2 = x - 1,y - 1,0
    while i >= 0:
        while j >= 0:
            if BOARD[i][j] < 0:
                num2 += 1  # 当前位置之前计算还有多少对方的棋子
            j -= 1
        j = y
        i -= 1

    if (num1 == 1 and ((x == 2 and y == 3) or (x == 2 and y == 4) or (x == 3 and y == 2) or (x == 4 and y == 2) or (x == 3 and y == 3))):
        if (BOARD[x - 1][y] < 0):
            temp1,temp2 = BOARD[x-1][y],BOARD[x][y]
            BOARD[x-1][y] = BOARD[x][y]
            BOARD[x][y] = 0
            reward = value2()
            BOARD[x-1][y],BOARD[x][y] = temp1,temp2

            if reward >= 0:
                reward *= prior_rate_positive
            else:
                reward *= prior_rate_negative

            itemp, jtemp = 0, 0
            while itemp < 5:
                while jtemp < 5:
                    BOARD[itemp][jtemp] = board[itemp][jtemp]
                    jtemp += 1
                jtemp = 0
                itemp += 1

            return True, 0, reward

        if (BOARD[x - 1][y - 1] < 0):
            temp1, temp2 = BOARD[x - 1][y - 1], BOARD[x][y]
            BOARD[x - 1][y - 1] = BOARD[x][y]
            BOARD[x][y] = 0
            reward = value2()
            BOARD[x - 1][y - 1], BOARD[x][y] = temp1, temp2

            if reward >= 0:
                reward *= prior_rate_positive
            else:
                reward *= prior_rate_negative

            itemp, jtemp = 0, 0
            while itemp < 5:
                while jtemp < 5:
                    BOARD[itemp][jtemp] = board[itemp][jtemp]
                    jtemp += 1
                jtemp = 0
                itemp += 1
            return True, 1, reward

        if (BOARD[x][y - 1] < 0):
            temp1, temp2 = BOARD[x][y - 1], BOARD[x][y]
            BOARD[x][y - 1] = BOARD[x][y]
            BOARD[x][y] = 0
            reward = value2()
            BOARD[x][y - 1], BOARD[x][y] = temp1, temp2
            if reward >= 0:
                reward *= prior_rate_positive
            else:
                reward *= prior_rate_negative
            itemp, jtemp = 0, 0
            while itemp < 5:
                while jtemp < 5:
                    BOARD[itemp][jtemp] = board[itemp][jtemp]
                    jtemp += 1
                jtemp = 0
                itemp += 1
            return True, 2, reward

    # if (flag4 == 0 or flag4 == 1) and ((x == 4 and y == 4) or (x == 3 and y == 3)):
    #     if np.random.rand() > 0.4:
    #         temp1, temp2 = BOARD[x - 1][y - 1], BOARD[x][y]
    #         BOARD[x - 1][y - 1] = BOARD[x][y]
    #         BOARD[x][y] = 0
    #         reward = value2()
    #         BOARD[x - 1][y - 1], BOARD[x][y] = temp1, temp2
    #
    #         if reward >= 0:
    #             reward *= prior_rate_positive
    #         else:
    #             reward *= prior_rate_negative
    #         return True, 1, reward

    if (num1 == 0 and ((x == 2 and y == 4) or (x == 4 and y == 2))):
        temp1, temp2 = BOARD[x - 1][y - 1], BOARD[x][y]
        BOARD[x - 1][y - 1] = BOARD[x][y]
        BOARD[x][y] = 0
        reward = value2()
        BOARD[x - 1][y - 1], BOARD[x][y] = temp1, temp2

        if reward >= 0:
            reward *= prior_rate_positive
        else:
            reward *= prior_rate_negative

        itemp, jtemp = 0, 0
        while itemp < 5:
            while jtemp < 5:
                BOARD[itemp][jtemp] = board[itemp][jtemp]
                jtemp += 1
            jtemp = 0
            itemp += 1

        return True, 1, reward

    if (x == 1 and y == 1):
        temp1, temp2 = BOARD[x - 1][y - 1], BOARD[x][y]
        BOARD[x - 1][y - 1] = BOARD[x][y]
        BOARD[x][y] = 0
        reward = value2()
        BOARD[x - 1][y - 1], BOARD[x][y] = temp1, temp2

        if reward >= 0:
            reward *= prior_rate_positive
        else:
            reward *= prior_rate_negative

        itemp, jtemp = 0, 0
        while itemp < 5:
            while jtemp < 5:
                BOARD[itemp][jtemp] = board[itemp][jtemp]
                jtemp += 1
            jtemp = 0
            itemp += 1
        return True, 1, reward

    if (x == 1 and y == 0):
        temp1, temp2 = BOARD[x - 1][y], BOARD[x][y]
        BOARD[x - 1][y] = BOARD[x][y]
        BOARD[x][y] = 0
        reward = value2()
        BOARD[x - 1][y], BOARD[x][y] = temp1, temp2

        if reward >= 0:
            reward *= prior_rate_positive
        else:
            reward *= prior_rate_negative

        itemp, jtemp = 0, 0
        while itemp < 5:
            while jtemp < 5:
                BOARD[itemp][jtemp] = board[itemp][jtemp]
                jtemp += 1
            jtemp = 0
            itemp += 1
        return True,0,reward

    if (x == 0 and y == 1):
        temp1, temp2 = BOARD[x][y - 1], BOARD[x][y]
        BOARD[x][y - 1] = BOARD[x][y]
        BOARD[x][y] = 0
        reward = value2()
        BOARD[x][y - 1], BOARD[x][y] = temp1, temp2

        if reward >= 0:
            reward *= prior_rate_positive
        else:
            reward *= prior_rate_negative

        itemp, jtemp = 0, 0
        while itemp < 5:
            while jtemp < 5:
                BOARD[itemp][jtemp] = board[itemp][jtemp]
                jtemp += 1
            jtemp = 0
            itemp += 1
        return True,2,reward

    #残局专用
    if num2 == 0 and x < 3 and y < 3:
        temp1, temp2 = BOARD[x - 1][y - 1], BOARD[x][y]
        BOARD[x - 1][y - 1] = BOARD[x][y]
        BOARD[x][y] = 0
        reward = value2()
        BOARD[x - 1][y - 1], BOARD[x][y] = temp1, temp2

        if reward >= 0:
            reward *= prior_rate_positive
        else:
            reward *= prior_rate_negative

        itemp, jtemp = 0, 0
        while itemp < 5:
            while jtemp < 5:
                BOARD[itemp][jtemp] = board[itemp][jtemp]
                jtemp += 1
            jtemp = 0
            itemp += 1
        return True, 1, reward

    itemp, jtemp = 0, 0
    while itemp < 5:
        while jtemp < 5:
            BOARD[itemp][jtemp] = board[itemp][jtemp]
            jtemp += 1
        jtemp = 0
        itemp += 1

    return False,-1,infinity

def ValueCount(actions,board,loc,dep = 3,alpha = -infinity,beta = infinity,enter = True):
    global flag4
    global a_
    global b_
    global c_
    global d_
    global redprobability
    global blueprobability
    global Enter
    global BOARD

    i,j = 0,0
    while i < 5:
        while j < 5:
            BOARD[i][j] = board[i][j]
            j += 1
        j = 0
        i += 1
    x,y = loc[0],loc[1]
    #这里我规定：水平行动是0 斜方行动是1 垂直行动是2
    val,flag = 0.0,0.0
    if enter:
        flag4 += 1
    if flag4 < Enter:
        depth = dep
        a_ = 3.0
        b_ = 0.5
        c_ = 0.2
        d_ = 0.0
    else:
        depth = dep
        a_ = 2.5
        b_ = 1.5
        c_ = 0.1  # 选择回报率和遍历的深度 a,b,c是一个常数
        d_ = 0.0
    if actions == 1:
        a = BOARD[x - 1][y - 1]
        BOARD[x - 1][y - 1] = BOARD[x][y]
        BOARD[x][y] = 0
        i,j = 0,0
        while i <= 4:
            while j <= 4:
                if BOARD[i][j] > 0:
                    BlueProbability()
                    val += blueprobability[BOARD[i][j] - 1] * BlueMax(i, j, depth, alpha, beta)  # 加上红方的值
                j += 1
            j = 0
            i += 1
        BOARD[x][y] = BOARD[x - 1][y - 1]
        BOARD[x - 1][y - 1] = a
    elif actions == 0:
        a = BOARD[x - 1][y]
        BOARD[x - 1][y] = BOARD[x][y]
        BOARD[x][y] = 0
        i,j = 0,0
        while i <= 4:
            while j <= 4:
                if BOARD[i][j] > 0:
                    BlueProbability()
                    val += blueprobability[BOARD[i][j] - 1] * BlueMax(i, j, depth, alpha, beta)
                j += 1
            j = 0
            i += 1
        BOARD[x][y] = BOARD[x - 1][y]
        BOARD[x - 1][y] = a
    elif actions == 2:
        a = BOARD[x][y - 1]
        BOARD[x][y - 1] = BOARD[x][y]
        BOARD[x][y] = 0
        i,j = 0,0
        while i <= 4:
            while j <= 4:
                if BOARD[i][j] > 0:
                    BlueProbability()
                    val += blueprobability[BOARD[i][j] - 1] * BlueMax(i, j, depth, alpha, beta)
                j += 1
            j = 0
            i += 1
        BOARD[x][y] = BOARD[x][y - 1]
        BOARD[x][y - 1] = a
    return actions,True,val

def MatrixTransfrom(board):
    temp_board = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]
    i,j = 0,0
    while i <= 4:
        while j <= 4:
            temp_board[i][j] = -board[4-i][4-j]
            j += 1
        j = 0
        i += 1
    return temp_board

def LocationTransfrom(location):
    return [4 - location[0],4 - location[1]]

def AvailableAction(chara,team,loc):
    # 0:up/down 1:upleft/downright 2:left/right
    if team:
        clx = loc[chara][0]
        cly = loc[chara][1]
        if(clx == 0 and cly != 0):
            return [2]
        elif(cly == 0 and clx != 0):
            return [0]
        else:
            return [0,1,2]
    else:
        clx = loc[chara][0]
        cly = loc[chara][1]
        if (clx == 4 and cly != 4):
            return [2]
        elif (cly == 4 and clx != 4):
            return [0]
        else:
            return [0, 1, 2]

#这个函数用于决定那个棋子可以用于行动
def AvaliableActor(action,team,board):
    exist_array = [False, False, False, False, False, False]
    i, j = 0, 0
    while i < 5:
        while j < 5:
            if board[i][j] > 0 and team:
                exist_array[board[i][j] - 1] = True
            elif board[i][j] < 0 and not team:
                exist_array[-board[i][j] - 1] = True
            j += 1
        j = 0
        i += 1
    upper = -1
    lower = -1
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

#仅适用于三边操作都允许的情况
def Simulation(RED_OR_BLUE, loc, simulate_tree_depth, board):
    global infinity
    global Enter
    global flag4
    global BLUE
    global RED
    loc_redc = [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
    loc_bluec = [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
    exist_blue = [False, False, False, False, False, False]
    exist_red = [False, False, False, False, False, False]

    i,j = 0,0
    while i <= 4:
        while j <= 4:
            if board[i][j] > 0:
                loc_bluec[board[i][j] - 1] = [i, j]
                exist_blue[board[i][j] - 1] = True
            elif board[i][j] < 0:
                loc_redc[-board[i][j] - 1] = [i, j]
                exist_red[-board[i][j] - 1] = True
            j += 1
        j = 0
        i += 1
    temp = -infinity
    flag4 += 1
    reward_array = []

    if RED_OR_BLUE:
        temp_board = [[0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0]]
        i,j = 0,0
        while i < 5:
            while j < 5:
                temp_board[i][j] = board[i][j]
                j += 1
            j = 0
            i += 1
        Execute, label, reward = DesignatedProcess(loc, temp_board)
        if Execute:
            print('执行特殊行动：')
            print(label)
            print('得到回报：')
            print(reward)
            return label, reward, True

        chess = temp_board[loc[0]][loc[1]]
        record_chess = -1
        avaliable_action = AvailableAction(chess - 1, BLUE, loc_bluec)
        print('Simulation函数执行棋子：')
        print(chess)
        for action in avaliable_action:
            act, _, value = ValueCount(action, temp_board, loc, simulate_tree_depth, -infinity, infinity, False)
            print('执行行动:')
            print(act)
            print('获得回报：')
            print(value)
            reward_array.append(value)
            if action == 0:
                record_chess = temp_board[loc[0] - 1][loc[1]]
                temp_board[loc[0] - 1][loc[1]] = temp_board[loc[0]][loc[1]]
                temp_board[loc[0]][loc[1]] = 0
            elif action == 1:
                record_chess = temp_board[loc[0] - 1][loc[1] - 1]
                temp_board[loc[0] - 1][loc[1] - 1] = temp_board[loc[0]][loc[1]]
                temp_board[loc[0]][loc[1]] = 0
            elif action == 2:
                record_chess = temp_board[loc[0]][loc[1] - 1]
                temp_board[loc[0]][loc[1] - 1] = temp_board[loc[0]][loc[1]]
                temp_board[loc[0]][loc[1]] = 0
            if temp < value: #选取最大值，因为是对红方的value，因此取得最小值对应蓝方的最大值
                temp = value
                label = action

            exist_blue = [False, False, False, False, False, False]
            exist_red = [False, False, False, False, False, False]

            i, j = 0, 0
            while i <= 4:
                while j <= 4:
                    if temp_board[i][j] > 0:
                        loc_bluec[temp_board[i][j] - 1] = [i, j]
                        exist_blue[temp_board[i][j] - 1] = True
                    elif temp_board[i][j] < 0:
                        loc_redc[-temp_board[i][j] - 1] = [i, j]
                        exist_red[-temp_board[i][j] - 1] = True
                    j += 1
                j = 0
                i += 1

            if action == 0:
                temp_board[loc[0] - 1][loc[1]] = record_chess
                temp_board[loc[0]][loc[1]] = chess
            elif action == 1:
                temp_board[loc[0] - 1][loc[1] - 1] = record_chess
                temp_board[loc[0]][loc[1]] = chess
            elif action == 2:
                temp_board[loc[0]][loc[1] - 1] = record_chess
                temp_board[loc[0]][loc[1]] = chess

        val = temp
        #执行行动
        if label == 0:
            temp_board[loc[0] - 1][loc[1]] = temp_board[loc[0]][loc[1]]
            temp_board[loc[0]][loc[1]] = 0
        elif label == 1:
            temp_board[loc[0] - 1][loc[1] - 1] = temp_board[loc[0]][loc[1]]
            temp_board[loc[0]][loc[1]] = 0
        elif label == 2:
            temp_board[loc[0]][loc[1] - 1] = temp_board[loc[0]][loc[1]]
            temp_board[loc[0]][loc[1]] = 0

        BlueFail,RedFail = Judge(temp_board)
        if BlueFail and RED_OR_BLUE:
            return label, -infinity, False
        elif RedFail and RED_OR_BLUE:
            return label, infinity, False
        #验证是否把对方棋子吃光了
    else:
        temploc = [4 - loc[0],4 - loc[1]]
        temp_board2 = [[0,0,0,0,0],
                       [0,0,0,0,0],
                       [0,0,0,0,0],
                       [0,0,0,0,0],
                       [0,0,0,0,0]]
        transformed_board = [[0,0,0,0,0],
                             [0,0,0,0,0],
                             [0,0,0,0,0],
                             [0,0,0,0,0],
                             [0,0,0,0,0]]
        transformed_board_temp = [[0,0,0,0,0],
                                  [0,0,0,0,0],
                                  [0,0,0,0,0],
                                  [0,0,0,0,0],
                                  [0,0,0,0,0]]
        loc_redct = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
        loc_bluect = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
        i, j = 0, 0
        while i < 5:
            while j < 5:
                transformed_board[i][j] = -board[4 - i][4 - j]
                temp_board2[i][j] = transformed_board[i][j]
                if temp_board2 > 0:
                    loc_redct[temp_board2 - 1] = [i,j]
                elif temp_board2 < 0:
                    loc_bluect[-temp_board2 - 1] = [i, j]
                j += 1
            j = 0
            i += 1
        Execute, label, reward = DesignatedProcess([4 - loc[0],4 - loc[1]], temp_board2)
        if Execute:
            return label, reward, True

        #红色行动
        chess = temp_board2[temploc[0]][temploc[1]]
        record_chess = -1
        avaliable_action = AvailableAction(chess - 1, BLUE, loc_redct)
        for action in avaliable_action:
            act, _, value = ValueCount(action, temp_board2, temploc, simulate_tree_depth, -infinity, infinity)
            reward_array.append(value)
            if action == 0:
                record_chess = temp_board2[temploc[0] - 1][temploc[1]]
                temp_board2[temploc[0] - 1][temploc[1]] = temp_board2[temploc[0]][temploc[1]]
                temp_board2[temploc[0]][temploc[1]] = 0
            elif action == 1:
                record_chess = temp_board2[temploc[0] - 1][temploc[1] - 1]
                temp_board2[temploc[0] - 1][temploc[1] - 1] = temp_board2[temploc[0]][temploc[1]]
                temp_board2[temploc[0]][temploc[1]] = 0
            elif action == 2:
                record_chess = temp_board2[temploc[0]][temploc[1] - 1]
                temp_board2[temploc[0]][temploc[1] - 1] = temp_board2[temploc[0]][temploc[1]]
                temp_board2[temploc[0]][temploc[1]] = 0
            if temp < value:
                temp = value
                label = action
            i, j = 0, 0
            while i < 5:
                while j < 5:
                    transformed_board_temp[i][j] = -temp_board2[4 - i][4 - j]
                    j += 1
                j = 0
                i += 1

            i, j = 0, 0
            while i <= 4:
                while j <= 4:
                    if transformed_board_temp[i][j] > 0:
                        loc_bluec[transformed_board_temp[i][j] - 1] = [i, j]
                        exist_blue[transformed_board_temp[i][j] - 1] = True
                    elif transformed_board_temp[i][j] < 0:
                        loc_redc[-transformed_board_temp[i][j] - 1] = [i, j]
                        exist_red[-transformed_board_temp[i][j] - 1] = True
                    j += 1
                j = 0
                i += 1
            if action == 0:
                temp_board2[temploc[0] - 1][temploc[1]] = record_chess
                temp_board2[temploc[0]][temploc[1]] = chess
            elif action == 1:
                temp_board2[temploc[0] - 1][temploc[1] - 1] = record_chess
                temp_board2[temploc[0]][temploc[1]] = chess
            elif action == 2:
                temp_board2[temploc[0]][temploc[1] - 1] = record_chess
                temp_board2[temploc[0]][temploc[1]] = chess

        val = temp
        # 执行行动
        if label == 0:
            temp_board2[temploc[0] - 1][temploc[1]] = temp_board2[temploc[0]][temploc[1]]
            temp_board2[temploc[0]][temploc[1]] = 0
        elif label == 1:
            temp_board2[temploc[0] - 1][temploc[1] - 1] = temp_board2[temploc[0]][temploc[1]]
            temp_board2[temploc[0]][temploc[1]] = 0
        elif label == 2:
            temp_board2[temploc[0]][temploc[1] - 1] = temp_board2[temploc[0]][temploc[1]]
            temp_board2[temploc[0]][temploc[1]] = 0

        BlueFail,RedFail = Judge(transformed_board)
        if BlueFail and not RED_OR_BLUE:
            return label, infinity, False
        elif RedFail and not RED_OR_BLUE:
            return label, -infinity, False

    temp3 = reward_array[0]
    length = len(reward_array)
    if length == 3:
        flag1 = True
        for v in reward_array:
            if flag1 and temp3 != v:
                flag1 = False
        if flag1:
            label = 1
            print('三边回报相等，执行行为1')

    return label,val,True

def Execuate(action, loc, RED_OR_BLUE, board_before):
    global blue_win
    board = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]

    i, j = 0, 0
    while i < 5:
        while j < 5:
            board[i][j] = board_before[i][j]
            j += 1
        j = 0
        i += 1

    if RED_OR_BLUE:
        if action == 0:
            board[loc[0] - 1][loc[1]] = board[loc[0]][loc[1]]
            board[loc[0]][loc[1]] = 0
        elif action == 1:
            board[loc[0] - 1][loc[1] - 1] = board[loc[0]][loc[1]]
            board[loc[0]][loc[1]] = 0
        elif action == 2:
            board[loc[0]][loc[1] - 1] = board[loc[0]][loc[1]]
            board[loc[0]][loc[1]] = 0
    else:
        if action == 0:
            board[loc[0] + 1][loc[1]] = board[loc[0]][loc[1]]
            board[loc[0]][loc[1]] = 0
        elif action == 1:
            board[loc[0] + 1][loc[1] + 1] = board[loc[0]][loc[1]]
            board[loc[0]][loc[1]] = 0
        elif action == 2:
            board[loc[0]][loc[1] + 1] = board[loc[0]][loc[1]]
            board[loc[0]][loc[1]] = 0
    BlueFail,RedFail = Judge(board)
    if RedFail:
        blue_win += 1
        return True,board
    if BlueFail:
        return True, board
    return False,board

def init():
    global BOARD
    global flag4
    itemp, jtemp = 0, 0
    while itemp < 5:
        while jtemp < 5:
            BOARD[itemp][jtemp] = env.node_chess[itemp][jtemp]
            jtemp += 1
        jtemp = 0
        itemp += 1
    flag4 = 0

def BlueMax(x,y,depth,alpha,beta):
    global BOARD
    global redprobability
    global infinity
    BlueFail, RedFail = Judge(BOARD)
    if RedFail:
        return infinity #如果判断红方获胜
    elif BlueFail:
        return -infinity
    val,temp = 0.0,0.0
    if depth == 0:
        if x > 0 and y > 0:
            a = BOARD[x - 1][y - 1]
            BOARD[x - 1][y - 1] = BOARD[x][y]
            BOARD[x][y] = 0
            val = value2()
            BOARD[x][y] = BOARD[x - 1][y - 1]
            BOARD[x - 1][y - 1] = a
            alpha = max(alpha, val) #蓝方会想尽办法使得红方的回报最小
            if (beta <= alpha): #对于蓝方而言，如果alpha下限大于了上限值，返回上限值
                return alpha
            a = BOARD[x - 1][y]
            BOARD[x - 1][y] = BOARD[x][y]
            BOARD[x][y] = 0
            temp = value2()
            BOARD[x][y] = BOARD[x - 1][y]
            if (temp > val):
                val = temp
            BOARD[x - 1][y] = a
            alpha = max(alpha, val)
            if (beta <= alpha):
                return alpha
            a = BOARD[x][y - 1]
            BOARD[x][y - 1] = BOARD[x][y]
            BOARD[x][y] = 0
            temp = value2()
            BOARD[x][y] = BOARD[x][y - 1]
            if (temp > val):
                val = temp
            BOARD[x][y - 1] = a
            alpha = max(alpha, val)
            if (beta <= alpha):
                return alpha
        elif (x == 0):
            a = BOARD[x][y - 1]
            BOARD[x][y - 1] = BOARD[x][y]
            BOARD[x][y] = 0
            val = value2()
            BOARD[x][y] = BOARD[x][y - 1]
            BOARD[x][y - 1] = a
        elif (y == 0):
            a = BOARD[x - 1][y]
            BOARD[x - 1][y] = BOARD[x][y]
            BOARD[x][y] = 0
            val = value2()
            BOARD[x][y] = BOARD[x - 1][y]
            BOARD[x - 1][y] = a
        return val

    if (x > 0 and y > 0):
        a = BOARD[x - 1][y - 1]
        BOARD[x - 1][y - 1] = BOARD[x][y]
        BOARD[x][y] = 0
        i,j = 0,0
        while i < 5:
            while j < 5:
                if BOARD[i][j] < 0:
                    RedProbability()
                    val += redprobability[-BOARD[i][j] - 1] * RedMin(i, j, depth - 1, alpha, beta)
                j += 1
            j = 0
            i += 1
        BOARD[x][y] = BOARD[x - 1][y - 1]
        BOARD[x - 1][y - 1] = a
        alpha = max(alpha, val) #计算最大回报
        if (beta <= alpha):
            return alpha
        a = BOARD[x - 1][y]
        BOARD[x - 1][y] = BOARD[x][y]
        BOARD[x][y] = 0
        i = 0
        j = 0
        while i < 5:
            while j < 5:
                if BOARD[i][j] < 0:
                    RedProbability()
                    temp += redprobability[-BOARD[i][j] - 1] * RedMin(i, j, depth - 1, alpha, beta)
                j += 1
            j = 0
            i += 1
        if (temp > val):
            val = temp
        temp = 0
        BOARD[x][y] = BOARD[x - 1][y]
        BOARD[x - 1][y] = a
        alpha = max(alpha, val)
        if (beta <= alpha):
            return alpha
        a = BOARD[x][y - 1]
        BOARD[x][y - 1] = BOARD[x][y]
        BOARD[x][y] = 0
        i,j = 0,0
        while i < 5:
            while j < 5:
                if BOARD[i][j] < 0:
                    RedProbability()
                    temp += redprobability[-BOARD[i][j] - 1] * RedMin(i, j, depth - 1, alpha, beta)
                j += 1
            j = 0
            i += 1
        if (temp > val):
            val = temp
        BOARD[x][y] = BOARD[x][y - 1]
        BOARD[x][y - 1] = a
        alpha = max(alpha, val)
        if (beta <= alpha):
            return alpha
    elif x == 0:
        a = BOARD[x][y - 1]
        BOARD[x][y - 1] = BOARD[x][y]
        BOARD[x][y] = 0
        i,j = 0,0
        while i < 5:
            while j < 5:
                if BOARD[i][j] < 0:
                    RedProbability()
                    val += redprobability[-BOARD[i][j] - 1] * RedMin(i, j, depth - 1, alpha, beta)
                j += 1
            j = 0
            i += 1
        BOARD[x][y] = BOARD[x][y - 1]
        BOARD[x][y - 1] = a
    elif y == 0:
        a = BOARD[x - 1][y]
        BOARD[x - 1][y] = BOARD[x][y]
        BOARD[x][y] = 0
        i,j = 0,0
        while i < 5:
            while j < 5:
                if BOARD[i][j] < 0:
                    RedProbability()
                    val += redprobability[-BOARD[i][j] - 1] * RedMin(i, j, depth - 1, alpha, beta)
                j += 1
            j = 0
            i += 1
        BOARD[x][y] = BOARD[x - 1][y]
        BOARD[x - 1][y] = a
    return val

def RedMin(x,y,depth,alpha,beta):
    global BOARD
    global blueprobability
    global infinity
    BlueFail, RedFail = Judge(BOARD)
    if RedFail:
        return infinity
    elif BlueFail:
        return -infinity

    val = 0.0
    temp = 0.0
    if depth == 0:
        if x < 4 and y < 4:
            a = BOARD[x + 1][y + 1]
            BOARD[x + 1][y + 1] = BOARD[x][y]
            BOARD[x][y] = 0
            val = value2()
            BOARD[x][y] = BOARD[x + 1][y + 1]
            BOARD[x + 1][y + 1] = a
            beta = min(beta, val)
            if (beta <= alpha):
                return alpha
            a = BOARD[x + 1][y]
            BOARD[x + 1][y] = BOARD[x][y]
            BOARD[x][y] = 0
            temp = value2()
            BOARD[x][y] = BOARD[x + 1][y]
            if (temp < val):
                val = temp
            BOARD[x + 1][y] = a
            beta = min(beta, val)
            if (beta <= alpha):
                return alpha
            a = BOARD[x][y + 1]
            BOARD[x][y + 1] = BOARD[x][y]
            BOARD[x][y] = 0
            temp = value2()
            BOARD[x][y] = BOARD[x][y + 1]
            if (temp < val):
                val = temp
            BOARD[x][y + 1] = a
            beta = min(beta, val)
            if (beta <= alpha):
                return alpha
        elif x == 4:
            a = BOARD[x][y + 1]
            BOARD[x][y + 1] = BOARD[x][y]
            BOARD[x][y] = 0
            val = value2()
            BOARD[x][y] = BOARD[x][y + 1]
            BOARD[x][y + 1] = a
        elif y == 4:
            a = BOARD[x + 1][y]
            BOARD[x + 1][y] = BOARD[x][y]
            BOARD[x][y] = 0
            val = value2()
            BOARD[x][y] = BOARD[x + 1][y]
            BOARD[x + 1][y] = a
        return val

    if x < 4 and y < 4:
        a = BOARD[x + 1][y + 1]
        BOARD[x + 1][y + 1] = BOARD[x][y]
        BOARD[x][y] = 0
        i,j = 0,0
        while i < 5:
            while j < 5:
                if BOARD[i][j] > 0:
                    BlueProbability()
                    val += blueprobability[BOARD[i][j] - 1] * BlueMax(i, j, depth - 1, alpha, beta);
                j += 1
            j = 0
            i += 1
        BOARD[x][y] = BOARD[x + 1][y + 1]
        BOARD[x + 1][y + 1] = a
        beta = min(beta, val)
        if (beta <= alpha):
            return alpha
        a = BOARD[x + 1][y]
        BOARD[x + 1][y] = BOARD[x][y]
        BOARD[x][y] = 0
        i,j = 0,0
        while i < 5:
            while j < 5:
                if BOARD[i][j] > 0:
                    BlueProbability()
                    temp += blueprobability[BOARD[i][j] - 1] * BlueMax(i, j, depth - 1, alpha, beta)
                j += 1
            j = 0
            i += 1
        if (temp < val):
            val = temp
        temp = 0
        BOARD[x][y] = BOARD[x + 1][y]
        BOARD[x + 1][y] = a
        beta = min(beta, val)
        if (beta <= alpha):
            return alpha
        a = BOARD[x][y + 1]
        BOARD[x][y + 1] = BOARD[x][y]
        BOARD[x][y] = 0
        i,j = 0,0
        while i < 5:
            while j < 5:
                if BOARD[i][j] > 0:
                    BlueProbability()
                    temp += blueprobability[BOARD[i][j] - 1] * BlueMax(i, j, depth - 1, alpha, beta)
                j += 1
            j = 0
            i += 1
        if (temp < val):
            val = temp
        BOARD[x][y] = BOARD[x][y + 1]
        BOARD[x][y + 1] = a
        beta = min(beta, val)
        if (beta <= alpha):
            return alpha
    elif x == 4:
        a = BOARD[x][y + 1]
        BOARD[x][y + 1] = BOARD[x][y]
        BOARD[x][y] = 0
        i,j = 0,0
        while i < 5:
            while j < 5:
                if BOARD[i][j] > 0:
                    BlueProbability()
                    val += blueprobability[BOARD[i][j] - 1] * BlueMax(i, j, depth - 1, alpha, beta)
                j += 1
            j = 0
            i += 1
        BOARD[x][y] = BOARD[x][y + 1]
        BOARD[x][y + 1] = a
    elif y == 4:
        a = BOARD[x + 1][y]
        BOARD[x + 1][y] = BOARD[x][y]
        BOARD[x][y] = 0
        i,j = 0,0
        while i < 5:
            while j < 5:
                if BOARD[i][j] > 0:
                    BlueProbability()
                    val += blueprobability[BOARD[i][j] - 1] * BlueMax(i, j, depth - 1, alpha, beta)
                j += 1
            j = 0
            i += 1
        BOARD[x][y] = BOARD[x + 1][y]
        BOARD[x + 1][y] = a
    return val

def value2():
    global blueprobability
    global bluevalue
    global bluethreaten
    global redprobability
    global redvalue
    global redthreaten
    global infinity
    global BOARD
    global a_
    global b_
    global c_
    global d_
    BlueFail,RedFail = Judge(BOARD)
    if RedFail:
        return infinity
    elif BlueFail:
        return -infinity
    bluedistance = 0
    reddistance = 0
    blue_threaten = 0
    red_threaten = 0
    BlueProbability()
    i = 0
    while(i < 6):
        if blueprobability[i] != 0:
            bluedistance += blueprobability[i] * bluevalue[i]
            blue_threaten += blueprobability[i] * bluethreaten[i]
        i += 1
    RedProbability()
    i = 0
    while (i < 6):
        if redprobability[i] != 0:
            reddistance += redprobability[i] * redvalue[i]
            red_threaten += redprobability[i] * redthreaten[i]
        i += 1
    val = (-b_ * reddistance + a_ * bluedistance + d_ * blue_threaten - c_ * red_threaten)
    return val