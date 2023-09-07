from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, \
    QGridLayout, QLabel, QMessageBox, QFileDialog, QCheckBox
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
        hbox = QHBoxLayout()
        self.layout.addLayout(hbox)
        self.result_download_text_file_btn = QPushButton('텍스트 파일 다운로드')
        self.result_download_excel_file_btn = QPushButton('엑셀 파일 다운로드')
        self.close_button = QPushButton('종료')

        self.layout.addLayout(hbox)
        hbox.addWidget(self.result_download_excel_file_btn)
        hbox.addWidget(self.result_download_text_file_btn)
        self.layout.addWidget(self.close_button)
        self.setLayout(self.layout)

        self.result_download_text_file_btn.clicked.connect(self.result_download_text_file)
        self.result_download_excel_file_btn.clicked.connect(self.result_download_excel_file)
        self.close_button.clicked.connect(self.close)
        self.result_nums = []
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
                label.setFixedSize(30, 30)
                result_layout.addWidget(label, i, j+1)
                self.result_nums.append(result[j])

    def result_download_text_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, '저장 경로 지정', '', '*.txt')
        if file_path and self.result_nums:
            mainfunc.result_download(file_path, self.result_nums, 'text')

    def result_download_excel_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, '저장 경로 지정', '', '*.xlsx')
        if file_path and self.result_nums:
            mainfunc.result_download(file_path, self.result_nums, 'excel')


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


class pick_Num_Solution(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle('데이터 분석 및 뽑기')
        self.layout = QVBoxLayout()

        self.help_btn = QPushButton('도움말')
        self.checkbox1 = QCheckBox(': 출현 빈도 낮은 순서로 추출 여부')
        self.checkbox2 = QCheckBox(': 보너스 번호 출현 횟수 포함 여부')
        label1 = QLabel('<b>번호 개수 : </b>')
        self.lineedit1 = QLineEdit()
        label2 = QLabel('<b>뽑기 횟수 : </b>')
        self.lineedit2 = QLineEdit()
        self.data_upload_btn = QPushButton('데이터 업로드')
        self.accept_button = QPushButton('뽑기')
        self.reject_button = QPushButton('종료')
        self.main_window = main_window
        grid = QGridLayout()
        hbox = QHBoxLayout()

        self.layout.addLayout(grid)
        grid.addWidget(self.help_btn, 0, 0)
        grid.addWidget(self.checkbox1, 1, 0)
        grid.addWidget(self.checkbox2, 1, 1)
        grid.addWidget(label1, 2, 0)
        grid.addWidget(self.lineedit1, 2, 1)
        grid.addWidget(label2, 3, 0)
        grid.addWidget(self.lineedit2, 3, 1)
        self.layout.addWidget(self.data_upload_btn)
        self.layout.addLayout(hbox)
        hbox.addWidget(self.accept_button)
        hbox.addWidget(self.reject_button)
        self.setLayout(self.layout)

        # 시그널 추가
        self.help_btn.clicked.connect(self.help_info_show)
        self.data_upload_btn.clicked.connect(self.data_file_upload)
        self.accept_button.clicked.connect(self.fending_data)
        self.reject_button.clicked.connect(self.reject)

        self.lineedit1.setValidator(QIntValidator())
        self.lineedit2.setValidator(QIntValidator())

        self.file_path = None

    def data_file_upload(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '데이터 파일 업로드', '', '*.xlsx')
        if file_path:
            self.file_path = file_path

    def fending_data(self):
        if self.lineedit1.text() and self.lineedit2.text():
            nums = int(self.lineedit1.text())
            times = int(self.lineedit1.text())-1
            if not self.file_path:
                QMessageBox.warning(self, '경고', '데이터를 업로드 해 주세요.')
            elif nums < 6:
                QMessageBox.warning(self, '경고', '뽑을 번호 갯수는 최소 6개 이상 입니다.')
            elif times <= 0:
                QMessageBox.warning(self, '경고', '뽑기 횟수는 최소 1번 이상 입니다.')
            else:
                order = self.checkbox1.isChecked()
                is_bonus = self.checkbox2.isChecked()
                num_list = mainfunc.get_prize_solution(self.file_path, nums, order, is_bonus)
                show_dialog = lotto_Result(times, num_list)
                show_dialog.exec()


    def help_info_show(self):
        QMessageBox.information(self, '도움말', "1. 메인 화면의 지난 회차 당첨 데이터를 추출합니다."
                                             "\n\n2. 추출한 데이터 파일을 '데이터 업로드' 버튼을 클릭하여 업로드 합니다."
                                             "\n\n3. 체크 박스를 설정 합니다."
                                             "\n - 출현 빈도 낮은 순서로 추출 여부 : "
                                             "데이터 내 출현 빈도가 가장 낮은 순서 부터 시작,"
                                             " 번호 개수 값 만큼의 번호를 추출하여 무작위로 번호를 뽑습니다."
                                             "\n - 보너스 번호 출현 횟수 포함 여부 : "
                                             "보너스 번호로 출현했던 케이스도 포함하여 데이터를 분석합니다."
                                             "\n\n4. 번호 개수 및 뽑기 횟수를 지정해 줍니다.(필수)"
                                             "\n - 번호 개수 : 추출할 번호 개수를 입력 합니다. "
                                             "예)체크 박스를 모두 체크하지 않는 상태로 번호 개수 10개 입력 후 뽑을 시"
                                             "가장 많이 출현했던 10개의 숫자 중 무작위로 6개를 뽑음"
                                             "\n - 뽑기 횟수 : 뽑을 횟수를 지정 합니다."
                                             "\n\n5. 뽑기 버튼 클릭")

