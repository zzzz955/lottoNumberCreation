import json


def download_json(filepath, data):
    json_data = json.dumps(data)
    json.dump(json_data, filepath)

