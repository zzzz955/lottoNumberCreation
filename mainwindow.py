from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, \
    QHBoxLayout, QPushButton, QLineEdit, QGridLayout, QMessageBox
from PyQt5.Qt import QIntValidator
from qt_material import apply_stylesheet
from dialogs import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('로또 번호 추첨')
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 위젯 추가
        layout2 = QGridLayout()
        self.draw_one_time_btn = QPushButton('1회 랜덤 뽑기')
        self.draw_five_time_btn = QPushButton('5회 랜덤 뽑기')
        self.want_num = QPushButton('원하는 숫자만 선택')
        self.label1 = QLabel('<b>횟수 입력 : </b>')
        self.lineedit1 = QLineEdit()
        self.draw_as_want_btn = QPushButton('회 랜덤 뽑기')
        self.label2 = QLabel('<b>회차 입력 : </b>')
        self.lineedit2 = QLineEdit()
        self.pick_num_solution_btn = QPushButton('데이터 기반 뽑기')
        self.is_prize_btn = QPushButton('당첨 정보 확인')
        self.before_prize_btn = QPushButton('지난 회차 당첨 데이터 추출')
        self.close_button = QPushButton('종료')

        # 레이아웃 지정
        layout.addLayout(layout2)
        layout2.addWidget(self.draw_one_time_btn, 0, 0)
        layout2.addWidget(self.draw_five_time_btn, 0, 1)
        layout2.addWidget(self.want_num, 0, 2)
        layout2.addWidget(self.label1, 1, 0)
        layout2.addWidget(self.lineedit1, 1, 1)
        layout2.addWidget(self.draw_as_want_btn, 1, 2)
        layout2.addWidget(self.label2, 2, 0)
        layout2.addWidget(self.lineedit2, 2, 1)
        layout2.addWidget(self.is_prize_btn, 2, 2)
        layout.addWidget(self.pick_num_solution_btn)
        layout.addWidget(self.before_prize_btn)
        layout.addWidget(self.close_button)

        # 시그널 추가
        self.draw_one_time_btn.clicked.connect(lambda: self.draw_lotto(1))
        self.draw_five_time_btn.clicked.connect(lambda: self.draw_lotto(5))
        self.want_num.clicked.connect(self.con_only_want_draw)
        self.draw_as_want_btn.clicked.connect(lambda: self.draw_lotto((self.lineedit1.text())))
        self.is_prize_btn.clicked.connect(lambda: self.con_prize_page((self.lineedit2.text())))
        self.pick_num_solution_btn.clicked.connect(self.con_pick_num_solution)
        self.before_prize_btn.clicked.connect(self.con_download_lotto_prize_value)
        self.close_button.clicked.connect(self.close)

        # lineedit 입력 값 제한
        self.label1.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)
        self.lineedit1.setValidator(QIntValidator())
        self.lineedit2.setValidator(QIntValidator())

        # 인스턴스 변수 초기화
        self.appearance_nums = []

    def draw_lotto(self, num):
        # 랜덤 뽑기 다이얼로그 호출
        if num:
            result_dialog = lotto_Result(int(num), self.appearance_nums)
            result_dialog.exec()

    def con_pick_num_solution(self):
        # 데이터 기반 뽑기 다이얼로그 호출
        solution_dialog = pick_Num_Solution(self)
        solution_dialog.exec()

    def con_prize_page(self, index):
        # 당첨 정보 확인 기능 호출
        mainfunc.web_view(index)

    def con_only_want_draw(self):
        # 원하는 숫자만 선택 다이얼로그 호출
        dialog = only_Want_Draw(self)
        dialog.exec()

    def con_download_lotto_prize_value(self):
        # 지난 회차 당첨 데이터 추출 다이얼로그 호출
        dialog = download_Lotto_Prize_Value()
        dialog.show()


if __name__ == '__main__':
    app = QApplication([])
    apply_stylesheet(app, theme='custom.xml')
    window = MainWindow()
    window.show()
    app.exec()
