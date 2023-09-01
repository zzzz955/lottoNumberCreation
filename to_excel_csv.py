import pandas as pd


def download_excel(file_path, data):
    result = []
    result.append(data)
    df = pd.DataFrame(result, index=None)
    df.to_excel(file_path, sheet_name='result')


def download_csv(file_path, data):
    result = []
    result.append(data)
    df = pd.DataFrame(result, index=None)
    df.to_csv(file_path)