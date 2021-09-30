import json


def get_time_by_lesson(lesson):
    lesson = str(lesson).replace(' ', '')
    with open("time_transaltion.json", "r") as file:
        data = json.load(file)
    return data[lesson]
