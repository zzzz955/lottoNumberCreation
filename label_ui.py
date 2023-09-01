from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont
from PyQt5.QtCore import Qt


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

