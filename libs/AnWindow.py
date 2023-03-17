from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSignal
from resources.new_ui import Ui_AN_Chess
import sys
import os
import time
import random


class AnWindow(QWidget, Ui_AN_Chess):
    """
    每一个棋子是一个按钮，按钮名称为piece_xy  其中，x和y是棋子的坐标，可以通过x和y定位这个棋子
    棋子有四个自定义属性：color、type，值都设置成了类常量；redpos、bluepos 分别表示我方棋子是红方/蓝方时棋子的棋谱位置
        color为棋子的颜色，值可以是 Red和Blue和''
        type为走子时棋子的种类（棋子出发点/允许的棋子落点），值可以是From和CanTo和''
    """
    signal_init = pyqtSignal()     # 初始化完成信号
    WIDTH, HEIGHT = 5, 5           # 棋盘宽度、高度
    weROUND, youROUND = 1, 0       # 谁的回合 （我方回合、对方回合）
    pcDice, manDice = 1, 0         # 掷骰子方式 （电脑掷骰子、人工输入骰子数）
    Blue, Red = 'Blue', 'Red',     # 棋子颜色（蓝方、红方）
    From, CanTo = 'From', 'CanTo'  # 棋子种类（走子时）(棋子出发点、棋子允许的落点)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.initFlag = False
        self.youInitPieceNo = 1  # 对方初始棋号，用于画对面的初始布局 1,2,3,4,5,6
        self.weColor, self.youColor = AnWindow.Blue, AnWindow.Red  # 我方和对方棋子颜色
        self.diceType = AnWindow.pcDice  # 掷骰子方式
        self.round = AnWindow.weROUND    # 当前是谁的回合
        self.mode = 0         # 模式 0=>Simulation模式  1=>DQN模式
        self.diceNum = 1      # 骰子数
        self.pieceFrom, self.pieceTo = None, None  # 棋子从哪里来，到哪里去（走子） (c, t, x, y)格式 color,text,x,y
        self.can_mov_to = []  # 棋子可以走向的格子，piece_xy格式
        self.log = []         # 走子记录
        self.init_loc_we = [[3, 4], [4, 3], [2, 4], [3, 3], [4, 2], [4, 4]]  # 我方的初始布局，仅输出日志用到
        self.init_loc_you = []  # 记录对方的初始布局，仅输出日志用到
        self.init_piece = [     # 初始棋盘, 负数代表对面的棋子，1~6表示棋号，7表示没有棋号（空）  用来展示我方初始布局
            [-7, -7, -7, 0, 0],
            [-7, -7, 0, 0, 0],
            [-7, 0, 0, 0, 3],
            [0, 0, 0, 4, 1],
            [0, 0, 5, 2, 6]
        ]
        self.widget_board_red_x.hide()
        self.widget_board_red_y.hide()
        self.widget_running.setEnabled(False)
        self.textEdit_status.setText('待初始化')
        self.spinBox_diceNum.valueChanged.connect(self.update_dice)

    # 初始化按钮
    def init_clicked(self):
        self.weColor = AnWindow.Red if self.comboBox_weColor.currentIndex() else AnWindow.Blue
        self.youColor = AnWindow.Blue if self.comboBox_weColor.currentIndex() else AnWindow.Red
        self.diceType = AnWindow.manDice if self.comboBox_diceType.currentIndex() else AnWindow.pcDice
        self.round = AnWindow.youROUND if self.checkBox_youFirst.isChecked() else AnWindow.weROUND
        self.mode = self.comboBox_mode.currentIndex()
        self.widget_init.setEnabled(False)
        if self.diceType == AnWindow.manDice:
            self.btn_pcDice.setEnabled(False)
            self.spinBox_diceNum.setEnabled(True)
        else:
            self.btn_pcDice.setEnabled(True)
            self.spinBox_diceNum.setEnabled(False)
        if self.weColor == AnWindow.Blue:
            self.widget_board_red_x.hide()
            self.widget_board_red_y.hide()
            self.widget_board_blue_x.show()
            self.widget_board_blue_y.show()
        else:
            self.widget_board_red_x.show()
            self.widget_board_red_y.show()
            self.widget_board_blue_x.hide()
            self.widget_board_blue_y.hide()
        self.initFlag = True
        self.draw_init_board()
        self.textEdit_status.setText('设置对手初始布局')

    # 新的一局按钮
    def restart_clicked(self):
        reply = QMessageBox.question(self, '新的一局', '确认要开始新的一局吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        if self.pieceFrom:
            self.pieceFrom = None
            self.can_mov_to.clear()
            for x in range(AnWindow.WIDTH):
                for y in range(AnWindow.HEIGHT):
                    piece = self.findChild(QPushButton, 'piece_{}{}'.format(x, y))
                    piece.setProperty('type', '')
            self.refresh_board()
        self.reload_qss()
        self.widget_init.setEnabled(True)
        # 初始化值
        self.initFlag = False
        self.youInitPieceNo = 1
        self.weColor, self.youColor = AnWindow.Blue, AnWindow.Red
        self.diceType, self.round = AnWindow.pcDice, AnWindow.weROUND
        self.pieceFrom, self.pieceTo = None, None
        self.can_mov_to = []
        self.log = []
        self.init_loc_you = []
        # 初始化棋盘
        self.draw_init_board()
        # 初始化log栏和状态栏
        self.textEdit_log.setText('')
        self.textEdit_status.setText('待初始化')

    # 棋子被点击
    def piece_clicked(self):
        piece = self.sender()
        x = int(piece.objectName()[-2])
        y = int(piece.objectName()[-1])
        t = piece.text()
        c = piece.property('color')
        if self.initFlag:   # 已经初始化过了
            condition1 = piece.property('color') == self.weColor and self.round == AnWindow.weROUND
            condition2 = piece.property('color') == self.youColor and self.round == AnWindow.youROUND
            if self.youInitPieceNo <= 6:     # 还没有画完对方初始布局
                self.draw_you_piece(piece)
            elif condition1 or condition2:   # From
                if not self.pieceFrom:
                    self.pieceFrom = (c, t, x, y)
                    piece.setProperty('type', AnWindow.From)
                    self.calc_can_mov_to()
                    self.activate_can_mov_to()                # 激活可以走的棋子
                elif piece.property('type') == AnWindow.From:  # 两次点击一样的棋子
                    piece.setProperty('type', '')
                    self.deactivate_can_mov_to()
                    self.pieceFrom = None
            if piece.property('type') == 'CanTo':  # To
                self.pieceTo = (c, t, x, y)
                self.move_piece(piece)
                self.log_mov()
                self.show_log()
                self.deactivate_can_mov_to()
                self.exchange_round()
                self.pieceFrom = None
                self.pieceTo = None
            self.reload_qss()
            self.judge()

    # 掷骰子按钮
    def dice_clicked(self):
        self.diceNum = random.randint(1, 6)
        self.spinBox_diceNum.setValue(self.diceNum)
        self.textEdit_status.append('掷骰子完成')

    # 我方走子按钮
    def ai_go_clicked(self):
        pass

    # 悔棋按钮
    def back_clicked(self):
        if self.pieceFrom:
            self.pieceFrom = None
            self.can_mov_to.clear()
            for x in range(AnWindow.WIDTH):
                for y in range(AnWindow.HEIGHT):
                    piece = self.findChild(QPushButton, 'piece_{}{}'.format(x, y))
                    piece.setProperty('type', '')
            self.refresh_board()
        self.reload_qss()
        if self.log:
            self.round = self.log[-1]['round']
            from_ = self.log[-1]['from']
            from_piece = self.findChild(QPushButton, 'piece_{}{}'.format(from_[2], from_[3]))
            from_piece.setText(from_[1])
            from_piece.setProperty('color', from_[0])
            from_piece.setProperty('type', '')
            to_ = self.log[-1]['to']
            to_piece = self.findChild(QPushButton, 'piece_{}{}'.format(to_[2], to_[3]))
            to_piece.setText(to_[1])
            to_piece.setProperty('color', to_[0])
            to_piece.setProperty('type', '')
            self.log.pop()
            self.refresh_board()
            self.show_log()
            self.show_round_status()

    # 保存棋谱按钮
    def save_clicked(self):
        first = self.lineEdit_first.text().strip()
        last = self.lineEdit_last.text().strip()
        win = self.comboBox_win.currentText().strip()
        name = self.lineEdit_name.text().strip()
        place = self.lineEdit_place.text().strip()
        if not first or not last:
            self.textEdit_status.setText('队伍信息不全')
        else:
            # WTN-先手参赛队 vs 后手参赛队-先（后）手胜-比赛时间地点-赛事名称
            dirname = "records/"
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            now_time = time.strftime("%Y.%m.%d %H.%M", time.localtime())
            filename = 'WTN-{} vs {}-{}-{} {}-{}.txt'.format(first, last, win, now_time, place, name)
            info = '#[WTN][{} R][{} B][{}][{} {}][{}];'.format(first, last, win, now_time, place, name)
            with open(dirname+'/'+filename, 'w', encoding='GB2312') as f:
                f.write(info + '\n')
                f.write(self.textEdit_log.toPlainText())
            self.textEdit_status.setText('导出棋谱完成')

    def update_dice(self, num):
        self.diceNum = int(num)

    # 初始化棋盘（我方的）
    def draw_init_board(self):
        for x in range(AnWindow.HEIGHT):
            for y in range(AnWindow.WIDTH):
                piece = self.findChild(QPushButton, 'piece_{}{}'.format(x, y))
                if self.init_piece[x][y] > 0:
                    piece.setProperty('color', self.weColor)
                    piece.setText(str(self.init_piece[x][y]))
                elif self.init_piece[x][y] < 0:
                    piece.setProperty('color', self.youColor)
                    piece.setText('')
                else:
                    piece.setProperty('color', '')
                    piece.setText('')
        self.refresh_board()

    # 画对方的初始化棋子（点击一次设置一颗）
    def draw_you_piece(self, sender):
        if sender.property('color') == self.youColor and sender.text() == '':
            sender.setText(str(self.youInitPieceNo))
            x, y = sender.objectName()[-2], sender.objectName()[-1]
            self.init_loc_you.append([int(x), int(y)])
            self.youInitPieceNo += 1
            if self.youInitPieceNo == 7:  # 6颗棋子都放完了
                self.signal_init.emit()
                self.show_log()
                self.show_round_status()
                self.widget_running.setEnabled(True)

    # 移动棋子
    def move_piece(self, piece_to):
        c, t, x_from, y_from = self.pieceFrom
        color = self.weColor if self.round == AnWindow.weROUND else self.youColor
        piece_from = self.findChild(QPushButton, 'piece_{}{}'.format(x_from, y_from))
        piece_to.setProperty('color', color)
        piece_to.setProperty('type', '')
        piece_to.setText(t)
        piece_from.setProperty('color', '')
        piece_from.setProperty('type', '')
        piece_from.setText('')
        piece_from.setEnabled(False)

    # 计算当前可以移动到哪些格子
    def calc_can_mov_to(self):
        c, t, x, y = self.pieceFrom
        if self.round == AnWindow.weROUND:
            if x - 1 >= 0:
                self.can_mov_to.append('piece_{}{}'.format(x - 1, y))
            if y - 1 >= 0:
                self.can_mov_to.append('piece_{}{}'.format(x, y - 1))
            if x - 1 >= 0 and y - 1 >= 0:
                self.can_mov_to.append('piece_{}{}'.format(x - 1, y - 1))
        else:
            if x + 1 <= 4:
                self.can_mov_to.append('piece_{}{}'.format(x + 1, y))
            if y + 1 <= 4:
                self.can_mov_to.append('piece_{}{}'.format(x, y + 1))
            if x + 1 <= 4 and y + 1 <= 4:
                self.can_mov_to.append('piece_{}{}'.format(x + 1, y + 1))

    # 激活可以移动到的格子
    def activate_can_mov_to(self):
        for piece_name in self.can_mov_to:
            piece = self.findChild(QPushButton, piece_name)
            piece.setEnabled(True)
            piece.setProperty('type', AnWindow.CanTo)

    # 禁用可以移动到的格子
    def deactivate_can_mov_to(self):
        for piece_name in self.can_mov_to:
            piece = self.findChild(QPushButton, piece_name)
            piece.setProperty('type', '')
            if piece.property('color') == '':
                piece.setEnabled(False)
        self.can_mov_to.clear()

    # 记录走子
    def log_mov(self):
        color_from, text_from, x_from, y_from = self.pieceFrom
        color_to, text_to, x_to, y_to = self.pieceTo
        log = {
            'round': self.round,
            'color': color_from,
            'diceNum': self.diceNum,
            'pieceNo': text_from,
            'from': (color_from, text_from, x_from, y_from),
            'to': (color_to, text_to, x_to, y_to)
        }
        self.log.append(log)

    # 显示记录
    def show_log(self):
        self.textEdit_log.setText('')
        log_text = '{}:'.format(self.weColor[0])
        for i in range(len(self.init_loc_we)):
            piece = self.findChild(QPushButton, 'piece_{}{}'.format(self.init_loc_we[i][0], self.init_loc_we[i][1]))
            log_text += '{}-{};'.format(piece.property(self.weColor.lower()+'pos'), i+1)
        self.textEdit_log.append(log_text)
        log_text = '{}:'.format(self.youColor[0])
        for i in range(len(self.init_loc_you)):
            piece = self.findChild(QPushButton, 'piece_{}{}'.format(self.init_loc_you[i][0], self.init_loc_you[i][1]))
            log_text += '{}-{};'.format(piece.property(self.weColor.lower()+'pos'), i+1)
        self.textEdit_log.append(log_text)
        for i in range(len(self.log)):
            log = self.log[i]
            piece = self.findChild(QPushButton, 'piece_{}{}'.format(log['to'][2], log['to'][3]))
            log_text = '{}:{};({}{},{})'.format(
                i+1, log['diceNum'], log['color'][0], log['pieceNo'], piece.property(self.weColor.lower()+'pos')
            )
            self.textEdit_log.append(log_text)

    # 状态框显示当前是谁的回合
    def show_round_status(self):
        if self.round == AnWindow.weROUND:
            self.textEdit_status.setText('我方回合')
        else:
            self.textEdit_status.setText('对方回合')

    # 回合交换
    def exchange_round(self):
        self.round = AnWindow.weROUND if self.round == AnWindow.youROUND else AnWindow.youROUND
        self.show_round_status()

    # 刷新棋盘（设置按钮是否可用）
    def refresh_board(self):
        for x in range(AnWindow.HEIGHT):
            for y in range(AnWindow.WIDTH):
                piece = self.findChild(QPushButton, 'piece_{}{}'.format(x, y))
                if piece.property('color') == AnWindow.Blue or piece.property('color') == AnWindow.Red:
                    piece.setEnabled(True)
                elif piece.property('type') == AnWindow.CanTo:
                    piece.setEnabled(True)
                else:
                    piece.setEnabled(False)
        self.reload_qss()

    # 重新加载qss
    def reload_qss(self):
        qss = self.widget_board.styleSheet()
        self.widget_board.setStyleSheet(qss)

    # 判断胜负
    def judge(self):
        piece_00 = self.findChild(QPushButton, 'piece_00')
        piece_44 = self.findChild(QPushButton, 'piece_44')
        we_flag, you_flag = False, False
        for x in range(AnWindow.HEIGHT):
            for y in range(AnWindow.WIDTH):
                piece = self.findChild(QPushButton, 'piece_{}{}'.format(x, y))
                if piece.property('color') == self.weColor:
                    we_flag = True
                if piece.property('color') == self.youColor:
                    you_flag = True
        if not you_flag or piece_00.property('color') == self.weColor:
            self.textEdit_status.setText('我方胜利')
            QMessageBox.information(self, '提示', '我方胜利')
        elif not we_flag or piece_44.property('color') == self.youColor:
            self.textEdit_status.setText('对方胜利')
            QMessageBox.information(self, '提示', '对方胜利')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnWindow()
    window.show()
    sys.exit(app.exec_())
