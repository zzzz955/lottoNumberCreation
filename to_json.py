import json


def download_json(filepath, data):
    json_data = json.dumps(data)
    with open(filepath, 'w') as json_file:
        json.dump(json_data, json_file)

