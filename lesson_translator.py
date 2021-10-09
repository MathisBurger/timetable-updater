import json


def get_time_by_lesson(lesson):
    lesson = str(lesson).replace(' ', '')
    with open("time_transaltion.json", "r") as file:
        data = json.load(file)
    start = str(data[lesson][0]).split(":")
    end = str(data[lesson][1]).split(":")
    return [start, end]
