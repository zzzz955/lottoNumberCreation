from PyQt5.QtWidgets import QMessageBox
import os
import crawling
import to_json
import to_excel_csv
import webbrowser


def web_view(index):
    if index:
        url = ('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query='
               + index +
               '%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8')
        webbrowser.open(url)


def fending_json(file_path, first_num, last_num, cool_time):
    data = crawling.find_prize_number(first_num, last_num, cool_time)
    to_json.download_json(file_path, data)
    open_file(file_path)


def fending_excel(file_path, first_num, last_num, cool_time):
    try:
        data = crawling.find_prize_number(first_num, last_num, cool_time)
        to_excel_csv.download_excel(file_path, data)
        open_file(file_path)
    except Exception as e:
        print(e)


def fending_csv(file_path, first_num, last_num, cool_time):
    data = crawling.find_prize_number(first_num, last_num, cool_time)
    to_excel_csv.download_csv(file_path, data)
    open_file(file_path)


def open_file(file_path):
    result = QMessageBox.information(None, '파일 저장 완료', '성공 적으로 파일을 저장 하였습니다. 저장된 파일을 확인해 보시겠습니까?',
                                     QMessageBox.Ok | QMessageBox.No, QMessageBox.Ok)
    if result == QMessageBox.Ok:
        os.startfile(file_path)

