import requests
from bs4 import BeautifulSoup


def find_prize_number(first_num, last_num):
    for index in range(first_num+1, last_num+1):
        url = ('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query='
               + str(index) +
               '%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        target_class = ['winning_number', 'bonus_number']
        elements_with_class = soup.find_all(class_=target_class)
        for element in elements_with_class:
            print(element.text)


find_prize_number(1, 100)