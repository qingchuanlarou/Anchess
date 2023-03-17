from PyQt5.QtCore import QThread, pyqtSignal
import libs.EinsteinMK3.DQN as DQN
import libs.EinsteinMK3.api as api


class AiThread(QThread):
    signal_actor = pyqtSignal(int)
    signal_finish = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        actions = 3
        #actor_num = 1
        states = 25
        self.DQN = DQN.DeepQNetwork(actions, states)
        self.DQN.restore()
        self.dice = 0
        self.running_flag = False

    def run(self):
        if not self.running_flag:
            self.running_flag = True
            actor = api.who_act(self.dice)
            self.signal_actor.emit(actor)

            act = api.action(self.DQN, actor)
            self.signal_finish.emit(act)
            self.running_flag = False

    @staticmethod
    def init(init_chess, mode):
        api.init(init_chess, mode)
