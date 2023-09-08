import pandas as pd
import openpyxl


def download_excel(file_path, data):
    # 데이터 프레임 생성 및 엑셀 파일 변환 및 생성
    df = pd.DataFrame(data, index=None)
    df.to_excel(file_path, sheet_name='result', index=False, engine='openpyxl')


def download_csv(file_path, data):
    # 데이터 프레임 생성 및 csv 파일 변환 및 생성
    df = pd.DataFrame(data, index=None)
    df.to_csv(file_path, encoding='euc-kr', index=False)


def download_result(file_path, data):
    # 추첨 결과 엑셀 파일 변환 및 생성
    data_lists = []
    col = []
    for i in range(6):
        col.append(f'추첨 번호{i+1}')
    for i in range(0, len(data), 6):
        data_lists.append(data[i:i + 6])
    df = pd.DataFrame(data_lists, columns=col)
    df.to_excel(file_path, sheet_name='result', index=False, engine='openpyxl')

