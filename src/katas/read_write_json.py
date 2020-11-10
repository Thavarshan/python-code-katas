import json


def write_to_json_file(data: dict, file_name: str):
    with open(file_name, 'w+') as write_file:
        json.dump(data, write_file, indent=4)


def read_from_json_file(file_name: str):
    with open(file_name, 'r+') as read_file:
        return json.load(read_file)
