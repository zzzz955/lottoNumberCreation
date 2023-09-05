from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, \
    QGridLayout, QLabel, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.Qt import QIntValidator, QDoubleValidator
import random_func as ran
import mainfunc
from label_ui import CircleLabel


class lotto_Result(QDialog):
    def __init__(self, times, appearance_nums):
        super().__init__()
        self.setWindowTitle('로또 번호 추첨')
        self.layout = QVBoxLayout()
        self.close_button = QPushButton('종료')
        self.layout.addWidget(self.close_button)
        self.setLayout(self.layout)

        # 시그널 추가
        self.close_button.clicked.connect(self.close)
        self.show_result(times, appearance_nums)

    def show_result(self, times, appearance_nums):
        result_layout = QGridLayout()
        self.layout.addLayout(result_layout)

        for i in range(times):
            if appearance_nums:
                result = ran.draw_lotto_fixed_range(appearance_nums)
            else:
                result = ran.draw_lotto()
            result_layout.addWidget(QLabel(f'<b>{i+1}회 추첨 결과 : </b>'), i, 0)
            for j in range(6):
                label = CircleLabel(f'{result[j]}')
                label.setAlignment(Qt.AlignCenter)
                label.setFixedSize(50, 50)
                result_layout.addWidget(label, i, j+1)



class download_Lotto_Prize_Value(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('회차별 당첨 번호 정보')

        self.layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        label1 = QLabel('<b>회차 정보 : </b>')
        self.lineedit1 = QLineEdit()
        label2 = QLabel('<b>~</b>')
        self.lineedit2 = QLineEdit()
        label3 = QLabel('<b>회차간 추출 간격 : </b>')
        self.lineedit3 = QLineEdit()
        label4 = QLabel('<b> * 회차간 추출 간격 × 추출 횟수 만큼의 시간이 소요됩니다. </b>')
        self.download_json_btn = QPushButton('json 파일 다운로드')
        self.download_excel_btn = QPushButton('excel 파일 다운로드')
        self.download_csv_btn = QPushButton('csv 파일 다운로드')
        self.close_button = QPushButton('종료')

        self.layout.addLayout(layout1)
        layout1.addWidget(label1)
        layout1.addWidget(self.lineedit1)
        layout1.addWidget(label2)
        layout1.addWidget(self.lineedit2)

        self.layout.addLayout(layout2)
        layout2.addWidget(label3)
        layout2.addWidget(self.lineedit3)
        layout2.addWidget(label4)

        self.layout.addLayout(layout3)
        layout3.addWidget(self.download_json_btn)
        layout3.addWidget(self.download_excel_btn)
        layout3.addWidget(self.download_csv_btn)

        self.layout.addWidget(self.close_button)
        self.setLayout(self.layout)

        # 시그널 추가
        self.download_json_btn.clicked.connect(lambda: self.con_download_files('json'))
        self.download_excel_btn.clicked.connect(lambda: self.con_download_files('excel'))
        self.download_csv_btn.clicked.connect(lambda: self.con_download_files('csv'))
        self.close_button.clicked.connect(self.close_dialog)

        self.lineedit1.setValidator(QIntValidator())
        self.lineedit2.setValidator(QIntValidator())
        double_validator = QDoubleValidator()
        double_validator.setNotation(QDoubleValidator.StandardNotation)  # 표준 표기법 사용
        double_validator.setDecimals(1)
        self.lineedit3.setValidator(double_validator)

    def con_download_files(self, form):
        try:
            first_num = self.lineedit1.text()
            last_num = self.lineedit2.text()
            cool_time = self.lineedit3.text()
            if first_num and last_num and cool_time:
                if int(first_num) <= int(last_num) and int(float(cool_time) * 10) > 0:
                    first_num = int(first_num)
                    last_num = int(last_num)
                    cool_time = float(cool_time)
                else:
                    QMessageBox.warning(self, '경고', '입력 값을 다시 확인해 주세요.')
                    return
            else:
                QMessageBox.warning(self, '경고', '회차 정보 값을 입력해 주세요.')
                return

            if form == 'json':
                file_path, _ = QFileDialog.getSaveFileName(self, '저장 경로 지정', '', '*.json')
                if file_path:
                    mainfunc.fending_json(file_path, first_num, last_num, cool_time)
            elif form == 'excel':
                file_path, _ = QFileDialog.getSaveFileName(self, '저장 경로 지정', '', '*.xlsx')
                if file_path:
                    mainfunc.fending_excel(file_path, first_num, last_num, cool_time)
            elif form == 'csv':
                file_path, _ = QFileDialog.getSaveFileName(self, '저장 경로 지정', '', '*.csv')
                if file_path:
                    mainfunc.fending_csv(file_path, first_num, last_num, cool_time)
            else:
                return
        except Exception as e:
            print(e)

    def close_dialog(self):
        self.close()


class only_Want_Draw(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle('추첨 번호 선택')
        self.layout = QVBoxLayout()
        self.accept_button = QPushButton('적용')
        self.reject_button = QPushButton('종료')
        self.main_window = main_window
        grid = QGridLayout()

        self.layout.addLayout(grid)
        self.layout.addWidget(self.accept_button)
        self.layout.addWidget(self.reject_button)
        self.setLayout(self.layout)

        # 시그널 추가
        self.accept_button.clicked.connect(self.fending_value)
        self.reject_button.clicked.connect(self.reject)
        self.buttons = []

        for i in range(9):
            for j in range(5):
                self.button = QPushButton(str(i*5+j+1))
                grid.addWidget(self.button, i, j)
                self.button.setCheckable(True)
                self.buttons.append(self.button)

    def fending_value(self):
        button_index = []
        for button in self.buttons:
            if button.isChecked():
                button_index.append(button.text())
        if len(button_index) < 6:
            QMessageBox.critical(self, '경고', '6개 이상의 숫자를 선택해 주세요')
            return
        self.accept()
        self.main_window.appearance_nums = button_index


