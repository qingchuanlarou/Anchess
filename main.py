from PyQt5.QtWidgets import QApplication, QPushButton
from libs.AnWindow import AnWindow
from libs.Threads import AiThread
import libs.EinsteinMK3.EnvFile as env
import libs.EinsteinMK3.api as api
import sys


class AnChess(AnWindow):
    def __init__(self):
        super().__init__()
        self.ai = AiThread()
        self.ai.signal_actor.connect(self.ai_actor)
        self.ai.signal_finish.connect(self.ai_move)
        self.signal_init.connect(lambda: self.ai.init(self.bord2list(), self.mode))  # 初始化ai

    # 我方走子按钮
    def ai_go_clicked(self):
        if self.round != AnWindow.weROUND:
            self.textEdit_status.append('当前是对方回合')
        elif not self.ai.running_flag:
            self.btn_weGo.setEnabled(False)
            self.btn_weGo.setText('走子中...')
            self.textEdit_status.append('Ai思考中...')

            self.ai.dice = self.diceNum
            env.node_chess = self.bord2list()
            api.update_vars()
            self.ai.start()

    # ai计算完该走哪个棋子后执行
    def ai_actor(self, actor):
        """actor int类型，表示用哪个棋子走"""
        for x in range(AnWindow.HEIGHT):
            for y in range(AnWindow.WIDTH):
                piece = self.findChild(QPushButton, 'piece_{}{}'.format(x, y))
                if piece.text() == str(actor) and piece.property('color') == self.weColor:
                    t = piece.text()
                    c = piece.property('color')

                    self.pieceFrom = (c, t, x, y)
                    piece.setProperty('type', AnWindow.From)
                    self.reload_qss()
                    return

    # ai计算完该往哪里走后执行
    def ai_move(self, act):
        piece_from_x = self.pieceFrom[2]
        piece_from_y = self.pieceFrom[3]
        piece_to_x, piece_to_y = None, None
        if act == 0:  # 左
            piece_to_x = piece_from_x-1
            piece_to_y = piece_from_y
        elif act == 2:  # 上
            piece_to_x = piece_from_x
            piece_to_y = piece_from_y - 1
        elif act == 1:  # 斜
            piece_to_x = piece_from_x - 1
            piece_to_y = piece_from_y - 1
        piece = self.findChild(QPushButton, 'piece_{}{}'.format(piece_to_x, piece_to_y))
        self.pieceTo = (piece.property('color'), piece.text(), piece_to_x, piece_to_y)

        self.move_piece(piece)   # 走子
        self.log_mov()   # 记录走子
        self.show_log()  # 展示走子记录
        self.exchange_round()  # 交换回合
        self.btn_weGo.setEnabled(True)  # 设置按钮
        self.btn_weGo.setText('我方走子')
        self.pieceFrom, self.pieceTo = None, None
        self.refresh_board()  # 刷新界面

        self.judge()       # 判断是否分出胜负

    # 将棋盘信息转为二维列表（右下角为正，我方）
    def bord2list(self):
        node_chess = []
        for x in range(AnWindow.HEIGHT):
            tmp = []
            for y in range(AnWindow.WIDTH):
                piece = self.findChild(QPushButton, 'piece_{}{}'.format(x, y))
                piece_color = piece.property('color')
                piece_value = int(piece.text()) if piece.text() else 0
                piece_value = piece_value if piece_color == self.weColor else -piece_value
                tmp.append(piece_value)
            node_chess.append(tmp)
        return node_chess


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnChess()
    window.show()
    sys.exit(app.exec_())
