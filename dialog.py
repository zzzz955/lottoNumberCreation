from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, \
    QGridLayout, QLabel
from PyQt5.QtCore import Qt
import random_func as ran
from label_ui import CircleLabel


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

