import json


def download_json(filepath, data):
    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    with open(filepath, 'w', encoding='euc-kr') as json_file:
        json_file.write(json_data)

