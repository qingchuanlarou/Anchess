import numpy as np
import tensorflow as tf
import os
import libs.EinsteinMK3.Einstein2 as Em

print('开始坑爹了，要是你们看见了这个别在意，反正就是坑爹就完事了')

class DeepQNetwork:
    def __init__(
            self,
            n_actions,
            n_features,
            learning_rate=0.0001,
            reward_decay=0.9,
            e_greedy=0.99,
            replace_target_iter=50,
            memory_size=30000,
            batch_size=64,
            e_greedy_increment=None,
            output_graph=True,
    ):
        tf.reset_default_graph()
        self.n_actions = n_actions
        self.n_features = n_features
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon_max = e_greedy
        self.replace_target_iter = replace_target_iter
        self.memory_size = memory_size
        self.batch_size = batch_size
        self.epsilon_increment = e_greedy_increment
        self.epsilon = 0 if e_greedy_increment is not None else self.epsilon_max
        # 统计训练次数
        self.learn_step_counter = 1
        # 初始化记忆 memory [s, a, r, s_]
        self.memory = np.zeros((self.memory_size, n_features * 2 + 2))
        # 有两个网络组成 [target_net, evaluate_net]
        self._build_net()
        t_params = tf.get_collection('target_net_params')
        e_params = tf.get_collection('eval_net_params')
        self.replace_target_op = [tf.assign(t, e) for t, e in zip(t_params, e_params)]
        self.sess = tf.Session()
        self.upperindex = 10000
        if output_graph:
            # 开启tensorboard
            # $ tensorboard --logdir=logs
            # tf.train.SummaryWriter soon be deprecated, use following
            tf.summary.FileWriter(r'./logs', self.sess.graph)
        self.sess.run(tf.global_variables_initializer())
        self.cost_his = []
        self.index_ed = False
        self.saver = tf.train.Saver()

    def _build_net(self):
        # -------------- 创建 eval 神经网络, 及时提升参数 --------------
        self.s = tf.placeholder(tf.float32, [None, self.n_features], name='s')  # 用来接收 observation 25
        self.q_target = tf.placeholder(tf.float32, [None, self.n_actions],
                                       name='Q_target')  # 用来接收 q_target 的值, 这个之后会通过计算得到 3
        with tf.variable_scope('eval_net'):
            # c_names(collections_names) 是在更新 target_net 参数时会用到
            c_names, n_l1, w_initializer, b_initializer = \
                ['eval_net_params', tf.GraphKeys.GLOBAL_VARIABLES], 25 * self.n_features, \
                tf.random_normal_initializer(0., 0.3), tf.constant_initializer(0.1)  # config of layers

            # eval_net 的第一层. collections 是在更新 target_net 参数时会用到
            with tf.variable_scope('l1e'):
                w1 = tf.get_variable('w1e', [self.n_features, n_l1], initializer=w_initializer, collections=c_names)
                b1 = tf.get_variable('b1e', [1, n_l1], initializer=b_initializer, collections=c_names)
                l1 = tf.nn.relu(tf.matmul(self.s, w1) + b1)

            # eval_net 的第二层. collections 是在更新 target_net 参数时会用到
            with tf.variable_scope('l2e'):
                w2 = tf.get_variable('w2e', [n_l1, self.n_actions], initializer=w_initializer, collections=c_names)
                b2 = tf.get_variable('b2e', [1, self.n_actions], initializer=b_initializer, collections=c_names)
                self.q_eval = tf.matmul(l1, w2) + b2

        with tf.variable_scope('loss'):  # 求误差
            self.loss = tf.reduce_mean(tf.squared_difference(self.q_target, self.q_eval))
        with tf.variable_scope('train'):  # 梯度下降
            self._train_op = tf.train.RMSPropOptimizer(self.lr).minimize(self.loss)

        # ---------------- 创建 target 神经网络, 提供 target Q ---------------------
        self.s_ = tf.placeholder(tf.float32, [None, self.n_features], name='s_')  # 接收下个 observation
        with tf.variable_scope('target_net'):
            # c_names(collections_names) 是在更新 target_net 参数时会用到
            c_names = ['target_net_params', tf.GraphKeys.GLOBAL_VARIABLES]

            # target_net 的第一层. collections 是在更新 target_net 参数时会用到
            with tf.variable_scope('l1t'):
                w1 = tf.get_variable('w1t', [self.n_features, n_l1], initializer=w_initializer, collections=c_names)
                b1 = tf.get_variable('b1t', [1, n_l1], initializer=b_initializer, collections=c_names)
                l1 = tf.nn.relu(tf.matmul(self.s_, w1) + b1)

            # target_net 的第二层. collections 是在更新 target_net 参数时会用到
            with tf.variable_scope('l2t'):
                w2 = tf.get_variable('w2t', [n_l1, self.n_actions], initializer=w_initializer, collections=c_names)
                b2 = tf.get_variable('b2t', [1, self.n_actions], initializer=b_initializer, collections=c_names)
                self.q_next = tf.matmul(l1, w2) + b2

    def store_transition(self, s, a, r, s_):
        # 判断是否包含对应属性 没有就赋予初值
        if not hasattr(self, 'memory_counter'):
            self.memory_counter = 1
        # 纵向延伸
        transition = np.hstack((s, [a, r], s_))
        # 使用新的记忆替换掉旧网络的记忆
        index = self.memory_counter % self.memory_size
        self.memory[index, :] = transition
        self.memory_counter += 1

        if self.memory_counter > self.memory_size:
            self.index_ed = True
            self.memory_counter = self.upperindex

    def choose_action(self, observation):
        # 给观测值加上batch_size维度
        #print(observation)
        #observation = observation[np.newaxis, :]
        value1p = 1.05
        value1n = 0.95

        if np.random.uniform() < self.epsilon:
            # forward feed the observation and get q value for every actions
            actions_value = self.sess.run(self.q_eval, feed_dict={self.s: observation})

            if actions_value[0][1] > 0:
                actions_value[0][1] *= value1p
            else:
                actions_value[0][1] *= value1n

            print('DQN得到了以下的回报：')
            print(actions_value)
            action = np.argmax(actions_value)
        else:
            action = np.random.randint(0, self.n_actions)
        return action

    def learn(self):
        # 判断是否应该更新target-net网络了
        if self.learn_step_counter % self.replace_target_iter == 0:
            self.sess.run(self.replace_target_op)
            print('\ntarget_params_replaced\n')
        # 从以前的记忆中随机抽取一些记忆
        if self.memory_counter > self.memory_size:
            sample_index = np.random.choice(self.memory_size, size=self.batch_size)
        else:
            sample_index = np.random.choice(self.memory_counter, size=self.batch_size)
        batch_memory = self.memory[sample_index, :]

        q_next, q_eval = self.sess.run(
            [self.q_next, self.q_eval],
            feed_dict={
                self.s_: batch_memory[:, -self.n_features:],  # fixed params
                self.s: batch_memory[:, :self.n_features],  # newest params
            })

        # change q_target w.r.t q_eval's action
        q_target = q_eval.copy()
        batch_index = np.arange(self.batch_size, dtype=np.int32)
        eval_act_index = batch_memory[:, self.n_features].astype(int)
        reward = batch_memory[:, self.n_features + 1]

        q_target[batch_index, eval_act_index] = reward + self.gamma * np.max(q_next, axis=1)

        # 训练eval网络
        _, self.cost = self.sess.run([self._train_op, self.loss],
                                     feed_dict={self.s: batch_memory[:, :self.n_features],
                                                self.q_target: q_target})
        self.cost_his.append(self.cost)

        # 因为在训练过程中会逐渐收敛所以此处动态设置增长epsilon
        self.epsilon = self.epsilon + self.epsilon_increment if self.epsilon < self.epsilon_max else self.epsilon_max
        self.learn_step_counter += 1

    def save(self,i):
        path = "./dqn"
        if not os.path.exists(path):
            os.makedirs(path)
        self.saver.save(self.sess, path + '/model-' + str(i) + '.cptk')

    def restore(self, dirname='./model/', modelname = 'model-dqn.cptk'):
        if os.path.exists(dirname):
            saver = tf.train.import_meta_graph(dirname + modelname + '.meta')
            saver.restore(self.sess, dirname + modelname)
            print('权重加载完毕...')
        else:
            print('文件不存在...')


def choose_action_mkii(DQN,states,location,board):
    done, action, reward = Em.DesignatedProcess(location,board)
    if done:
        return action, reward, True
    action = DQN.choose_action(states)
    return action, None, False