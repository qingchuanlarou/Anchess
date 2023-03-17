import libs.EinsteinMK3.Einstein2 as Em
import libs.EinsteinMK3.EnvFile as env
import libs.EinsteinMK3.DQN as DQN
import numpy as np


train_frequency = 5  # 每隔多久时间训练一次
save_frequency = 50
current_number = 0   # 当前已经进行了多少action函数的次数
counter = 0
infinite = 120
mode = 0



def init(board, mode_):
    global mode
    global counter
    counter = 0
    """
    board为初始棋盘，二维列表
        右下角为正数，我方棋子；左上角为负数，对方棋子
        [[-6,-2,-4,0,0],
        [-1,-5,0,0,0],
        [-3,0,0,0,3],
        [0,0,0,5,1],
        [0,0,4,2,6]]
    """
    for i in range(5):
        for j in range(5):
            env.init_chess[i][j] = board[i][j]

    for i in range(5):
        for j in range(5):
            if board[i][j] > 0:
                env.init_loc_blue[board[i][j] - 1] = [i, j]
            elif board[i][j] < 0:
                env.init_loc_red[-board[i][j] - 1] = [i, j]
    
    env.init()
    Em.init()
    mode = mode_
    print('初始化完成')
    if mode == 0:
        print('使用Simulation模式')
    elif mode == 1:
        print('使用DQN模式')


def who_act(dice_):
    """
    dice_ int 骰子数
    根据骰子数计算应该由那个棋子行走，并返回
    """
    temp1, temp2 = Em.AvaliableActor(dice_ - 1, Em.BLUE, env.node_chess)

    if temp1 == -1 and temp2 != -1:
        actor_ = temp2
        actor_ += 1
    elif temp1 != -1 and temp2 == -1:
        actor_ = temp1
        actor_ += 1
    elif temp1 != -1 and temp2 != -1 and temp1 != temp2:
        actor_ = Em.Prior(True, temp1, temp2)
        actor_ += 1
    else:
        actor_ = dice_
    return actor_


def action(dqn, actor):
    global mode
    global counter
    counter += 1
    """
    dqn是我们训练好的
    actor是行走的棋子，int类型
    根据DQN和传入的棋子数计算并返回棋子应该往哪里走
    """
    # global train_frequency
    global current_number
    global save_frequency
    current_number += 1

    blue_action = Em.AvailableAction(actor - 1, Em.BLUE, env.node_loc_blue)
    reward = -infinite
    if blue_action == [0]:
        action_ = 0  # 指定的棋子向水平方向（左）移动
        action_, _, reward = Em.ValueCount(action_, env.node_chess, [env.node_loc_blue[actor - 1][0],
                                                                     env.node_loc_blue[actor - 1][1]], 3, -infinite, infinite)
    elif blue_action == [2]:
        action_ = 2  # 指定的棋子向垂直方向（上）移动
        action_, _, reward = Em.ValueCount(action_, env.node_chess, [env.node_loc_blue[actor - 1][0],
                                                                     env.node_loc_blue[actor - 1][1]], 3, -infinite, infinite)
    else:
        states_vec = np.reshape(env.node_chess, [1, 25]).tolist()
        if mode == 1:
            # action_ = dqn.choose_action(states_vec)  # 由DQN网络决定向上？向斜上？向左/右移动
            if counter <= 4:
                action_, reward, itx = DQN.choose_action_mkii(dqn, states_vec, env.node_loc_blue[actor - 1], env.node_chess)
                if not itx:
                    print('执行DQN行为：')
                    action_, _, reward = Em.ValueCount(action_, env.node_chess, [env.node_loc_blue[actor - 1][0],
                                                                env.node_loc_blue[actor - 1][1]], 3, -infinite, infinite)
                if itx:
                    print('执行指定行为：')
                print('执行行动：')
                print(action_)
                print('DQN得到回报：')
                print(reward)
            else:
                print('执行行为：')
                action_, _, _ = Em.Simulation(Em.BLUE, env.node_loc_blue[actor - 1], 3, env.node_chess)
                print(action_)
        elif mode == 0:
            action_, reward, _ = Em.Simulation(Em.BLUE, env.node_loc_blue[actor - 1], 3, env.node_chess)

    # 这里存储数据
    done, board_after = Em.Execuate(action_, [env.node_loc_blue[actor - 1][0], env.node_loc_blue[actor - 1][1]],Em.BLUE, env.node_chess)
    states_vec = np.reshape(env.node_chess, [1, 25]).tolist()
    new_state_vec = np.reshape(board_after, [1, 25]).tolist()
    dqn.store_transition(states_vec[0], action_, reward, new_state_vec[0])
    dqn.learn()
    if current_number % save_frequency == 0:
        dqn.save(current_number)

    return action_

def update_vars():
    """
    根据env.node_chess 来更新一些变量
    """
    env.node_loc_blue = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
    env.node_loc_red = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
    env.node_exist_blue = [False, False, False, False, False, False]
    env.node_exist_red = [False, False, False, False, False, False]
    for x in range(5):
        for y in range(5):
            value = env.node_chess[x][y]
            if value > 0:
                env.node_loc_blue[value-1] = [x, y]
                env.node_exist_blue[value-1] = True
            elif value < 0:
                env.node_loc_red[-value-1] = [x, y]
                env.node_exist_red[-value-1] = True

