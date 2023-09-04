import requests
from bs4 import BeautifulSoup


def find_prize_number(first_num, last_num):
    index = []
    winning_number1 = []
    winning_number2 = []
    winning_number3 = []
    winning_number4 = []
    winning_number5 = []
    winning_number6 = []
    bonus_number = []
    for i in range(first_num, last_num+1):
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

    data = {
            '회차 정보': index,
            '당첨 번호1': winning_number1,
            '당첨 번호2': winning_number2,
            '당첨 번호3': winning_number3,
            '당첨 번호4': winning_number4,
            '당첨 번호5': winning_number5,
            '당첨 번호6': winning_number6,
            'bonus_number': bonus_number
        }
    return data

