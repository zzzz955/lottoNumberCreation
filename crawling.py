from PyQt5.QtWidgets import QMessageBox
import requests
from bs4 import BeautifulSoup
import time


def find_prize_number(first_num, last_num, cool_time):
    # 리스트 초기화
    index = []
    winning_number1 = []
    winning_number2 = []
    winning_number3 = []
    winning_number4 = []
    winning_number5 = []
    winning_number6 = []
    bonus_number = []
    try:
        # 웹사이트 크롤링 및 데이터 리스트 전달
        for i in range(first_num, last_num + 1):
            url = ('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query='
                   + str(i) +
                   '%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8')
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            target_class = ['winning_number', 'bonus_number']
            elements_with_class = soup.find_all(class_=target_class)
            winning_numbers = elements_with_class[0].text.strip().split(' ')

            index.append(i)
            winning_number1.append(int(winning_numbers[0]))
            winning_number2.append(int(winning_numbers[1]))
            winning_number3.append(int(winning_numbers[2]))
            winning_number4.append(int(winning_numbers[3]))
            winning_number5.append(int(winning_numbers[4]))
            winning_number6.append(int(winning_numbers[5]))
            bonus_number.append(int(elements_with_class[1].text.strip()))
            time.sleep(cool_time)

        # 데이터 딕셔너리 생성 및 반환
        data = {
            '회차 정보': index,
            '당첨 번호1': winning_number1,
            '당첨 번호2': winning_number2,
            '당첨 번호3': winning_number3,
            '당첨 번호4': winning_number4,
            '당첨 번호5': winning_number5,
            '당첨 번호6': winning_number6,
            '보너스 번호': bonus_number
        }
        return data
    except Exception as e:
        QMessageBox.critical(None, '데이터 추출 중단', f'데이터 추출 중 예외가 발생하여 데이터 추출이 중단되었습니다. 네트워크 환경을 확인해 주세요.'
                                                f'\n - 에러 코드 : {e}'
                                                f'\n - 추출 데이터 : {len(index)}회차 까지 데이터 추출 완료')
        data = {
            '회차 정보': index,
            '당첨 번호1': winning_number1,
            '당첨 번호2': winning_number2,
            '당첨 번호3': winning_number3,
            '당첨 번호4': winning_number4,
            '당첨 번호5': winning_number5,
            '당첨 번호6': winning_number6,
            '보너스 번호': bonus_number
        }
        return data

