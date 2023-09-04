from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, \
    QGridLayout, QLabel, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.Qt import QIntValidator
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


class download_Lotto_Prize_Value(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle('회차별 당첨 번호 정보')
        self.main_window = main_window

        self.layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        label1 = QLabel('<b>회차 정보 : </b>')
        self.lineedit1 = QLineEdit()
        label2 = QLabel('<b>~</b>')
        self.lineedit2 = QLineEdit()
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
        layout2.addWidget(self.download_json_btn)
        layout2.addWidget(self.download_excel_btn)
        layout2.addWidget(self.download_csv_btn)

        self.layout.addWidget(self.close_button)
        self.setLayout(self.layout)

        # 시그널 추가
        self.download_json_btn.clicked.connect(lambda: self.con_download_files('json'))
        self.download_excel_btn.clicked.connect(lambda: self.con_download_files('excel'))
        self.download_csv_btn.clicked.connect(lambda: self.con_download_files('csv'))
        self.close_button.clicked.connect(self.close_dialog)

        self.lineedit1.setValidator(QIntValidator())
        self.lineedit2.setValidator(QIntValidator())

    def con_download_files(self, form):
        first_num = self.lineedit1.text()
        last_num = self.lineedit2.text()
        if first_num and last_num:
            if first_num <= last_num:
                first_num = int(first_num)
                last_num = int(last_num)
            else:
                QMessageBox.warning(self, '경고', '회차 정보 입력 값을 다시 확인해 주세요. 앞의 값이 더 작아야 합니다.')
                return
        else:
            QMessageBox.warning(self, '경고', '회차 정보 값을 입력해 주세요.')
            return

        if form == 'json':
            file_path, _ = QFileDialog.getSaveFileName(self, '저장 경로 지정', '', '*.json')
            if file_path:
                self.main_window.fending_json(file_path, first_num, last_num)
        elif form == 'excel':
            file_path, _ = QFileDialog.getSaveFileName(self, '저장 경로 지정', '', '*.xlsx')
            if file_path:
                self.main_window.fending_excel(file_path, first_num, last_num)
        elif form == 'csv':
            file_path, _ = QFileDialog.getSaveFileName(self, '저장 경로 지정', '', '*.csv')
            if file_path:
                self.main_window.fending_csv(file_path, first_num, last_num)
        else:
            return

    def close_dialog(self):
        self.close()