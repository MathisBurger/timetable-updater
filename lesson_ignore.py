def check_is_ignored(lesson):
    with open("ignore_lessons.txt", "r") as file:
        data = file.readlines()
    for line in data:
        if line.strip() == str(lesson).replace(' ', ''):
            return True
    return False
