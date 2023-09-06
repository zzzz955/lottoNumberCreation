import json


def download_json(filepath, data):
    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    with open(filepath, 'w', encoding='euc-kr') as json_file:
        json_file.write(json_data)


def download_text(filepath, data):
    data_lists = []
    string = ''
    for index, i in enumerate(range(0, len(data), 7)):
        data.insert(i, f'추첨 번호 리스트{index+1}')
        data_lists.append(data[i:i+7])
    for i in range(len(data_lists)):
        string += str(data_lists[i]) + '\n'
    with open(filepath, 'w', encoding='euc-kr') as text_file:
        text_file.write(string)

