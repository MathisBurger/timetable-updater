import json


def translate_name(name):
    with open("name_translator.json", "r") as file:
        data = json.load(file)
    return data[name]
