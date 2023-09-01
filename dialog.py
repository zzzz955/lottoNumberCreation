from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, \
    QGridLayout, QLabel
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont
from PyQt5.QtCore import Qt
import random_func as ran


class CircleLabel(QLabel):
    def __init__(self, text):
        super().__init__()

        self.text = text
        self.setStyleSheet('font-weight: bold;')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        circle_rect = self.rect().translated(0, 0)

        if 1 <= int(self.text) < 10:
            brush = QBrush(QColor('#F2B720'))
        elif 11 <= int(self.text) < 20:
            brush = QBrush(QColor('#4072AC'))
        elif 21 <= int(self.text) < 30:
            brush = QBrush(QColor('#DE4C0E'))
        elif 31 <= int(self.text) < 40:
            brush = QBrush(QColor('#9195A4'))
        else:
            brush = QBrush(QColor('#13BE4B'))
        painter.setBrush(brush)
        painter.drawEllipse(circle_rect)

        # 텍스트 그리기
        font = QFont("Arial", 15)
        painter.setFont(font)
        painter.setPen(Qt.white)  # 텍스트 색상
        painter.drawText(self.rect(), Qt.AlignCenter, self.text)


class lotto_Result(QDialog):
    def __init__(self, main_window, times):
        super().__init__()
        self.setWindowTitle('로또 번호 추첨')
        self.layout = QVBoxLayout()
        self.close_button = QPushButton('종료')
        self.layout.addWidget(self.close_button)
        self.setLayout(self.layout)

        # 시그널 추가
        self.close_button.clicked.connect(self.close_dialog)
        self.show_result(times)

    def show_result(self, times):
        result_layout = QGridLayout()
        self.layout.addLayout(result_layout)
        for i in range(times):
            result = ran.draw_lotto()
            result_layout.addWidget(QLabel(f'<b>{i+1}회 추첨 결과 : </b>'), i, 0)
            for j in range(6):
                label = CircleLabel(f'{result[j]}')
                label.setAlignment(Qt.AlignCenter)
                label.setFixedSize(50, 50)
                result_layout.addWidget(label, i, j+1)

    def close_dialog(self):
        self.close()

