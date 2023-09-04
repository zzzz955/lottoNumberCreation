import pandas as pd
import openpyxl


def download_excel(file_path, data):
    df = pd.DataFrame(data, index=None)
    df.to_excel(file_path, sheet_name='result', index=False, engine='openpyxl')


def download_csv(file_path, data):
    df = pd.DataFrame(data, index=None)
    df.to_csv(file_path, encoding='euc-kr', index=False)

