from PyQt5.QtWidgets import QMessageBox
import os
import crawling
import to_json_text
import to_excel_csv
import webbrowser
import lotto_prize_solution


def web_view(index):
    # 회차 정보 웹 페이지 이동
    if index:
        url = ('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query='
               + index +
               '%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8')
        webbrowser.open(url)


def fending_json(file_path, first_num, last_num, cool_time):
    # json 파일 정보 전달
    data = crawling.find_prize_number(first_num, last_num, cool_time)
    to_json_text.download_json(file_path, data)
    open_file(file_path)


def fending_excel(file_path, first_num, last_num, cool_time):
    # excel 파일 정보 전달
    data = crawling.find_prize_number(first_num, last_num, cool_time)
    to_excel_csv.download_excel(file_path, data)
    open_file(file_path)


def fending_csv(file_path, first_num, last_num, cool_time):
    # csv 파일 정보 전달
    data = crawling.find_prize_number(first_num, last_num, cool_time)
    to_excel_csv.download_csv(file_path, data)
    open_file(file_path)


def open_file(file_path):
    # 파일 저장 후 파일 오픈 여부
    result = QMessageBox.information(None, '파일 저장 완료', '성공 적으로 파일을 저장 하였습니다. 저장된 파일을 확인해 보시겠습니까?',
                                     QMessageBox.Ok | QMessageBox.No, QMessageBox.Ok)
    if result == QMessageBox.Ok:
        os.startfile(file_path)


def get_prize_solution(file_path, nums, order, is_bonus):
    # 데이터 분석 및 추첨 정보 전달
    num_list = lotto_prize_solution.prize_solution(file_path, nums, order, is_bonus)
    return num_list


def result_download(file_path, data, form):
    # 추첨 결과 다운로드 정보 전달
    if form == 'excel':
        to_excel_csv.download_result(file_path, data)
        open_file(file_path)
    elif form == 'text':
        to_json_text.download_text(file_path, data)
        open_file(file_path)
    else:
        return

