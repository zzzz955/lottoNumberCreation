from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, \
    QHBoxLayout, QPushButton, QLineEdit, QGridLayout
from PyQt5.Qt import QIntValidator
from qt_material import apply_stylesheet
import webbrowser
from dialog import *
import crawling
import to_json
import to_excel_csv


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
        self.draw_one_time_btn = QPushButton('1회 뽑기')
        self.draw_five_time_btn = QPushButton('5회 뽑기')
        self.label1 = QLabel('<b>횟수 입력 : </b>')
        self.lineedit1 = QLineEdit()
        self.draw_as_want_btn = QPushButton('원하는 만큼 뽑기')
        self.label2 = QLabel('<b>회차 입력 : </b>')
        self.lineedit2 = QLineEdit()
        self.is_prize_btn = QPushButton('당첨 정보 확인')
        self.before_prize_btn = QPushButton('지난 회차 당첨 데이터')
        self.close_button = QPushButton('종료')

        # 레이아웃 지정
        layout.addLayout(layout2)
        layout2.addWidget(self.draw_one_time_btn, 0, 0)
        layout2.addWidget(self.draw_five_time_btn, 0, 1)
        layout2.addWidget(self.label1, 1, 0)
        layout2.addWidget(self.lineedit1, 1, 1)
        layout2.addWidget(self.draw_as_want_btn, 1, 2)
        layout2.addWidget(self.label2, 2, 0)
        layout2.addWidget(self.lineedit2, 2, 1)
        layout2.addWidget(self.is_prize_btn, 2, 2)
        layout2.addWidget(self.before_prize_btn, 2, 3)
        layout.addWidget(self.close_button)

        # 시그널 추가
        self.draw_one_time_btn.clicked.connect(lambda: self.draw_lotto(1))
        self.draw_five_time_btn.clicked.connect(lambda: self.draw_lotto(5))
        self.draw_as_want_btn.clicked.connect(lambda: self.draw_lotto((self.lineedit1.text())))
        self.is_prize_btn.clicked.connect(lambda: self.con_prize_page((self.lineedit2.text())))
        self.before_prize_btn.clicked.connect(self.show_dialog)
        self.close_button.clicked.connect(self.close_app)

        self.lineedit1.setValidator(QIntValidator())
        self.lineedit2.setValidator(QIntValidator())

    def draw_lotto(self, num):
        if num:
            result_dialog = lotto_Result(self, int(num))
            result_dialog.exec()

    def con_prize_page(self, index):
        try:
            if index:
                url = ('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query='
                       + index +
                       '%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8')
                webbrowser.open(url)
        except Exception as e:
            print(e)

    def show_dialog(self):
        dialog = download_Lotto_Prize_Value(self)
        dialog.show()


    def get_crawling_data(self, first_num, last_num):
        data = crawling.find_prize_number(first_num, last_num)
        return data

    def fending_json(self, file_path, first_num, last_num):
        data = self.get_crawling_data(first_num, last_num)
        to_json.download_json(file_path, data)

    def fending_excel(self, file_path, first_num, last_num):
        data = self.get_crawling_data(first_num, last_num)
        to_excel_csv.download_excel(file_path, data)

    def fending_csv(self, file_path, first_num, last_num):
        data = self.get_crawling_data(first_num, last_num)
        to_excel_csv.download_csv(file_path, data)

    def close_app(self):
        # 앱 종료
        self.close()

if __name__ == '__main__':
    app = QApplication([])
    apply_stylesheet(app, theme='custom.xml')
    window = MainWindow()
    window.show()
    app.exec()
