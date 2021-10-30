"""learn ukrainian with this target game!!!"""
import random


def generate_grid():
    """generates random list of 5 ukrainian letters"""
    alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    grid_lst = []
    while len(grid_lst) < 5:
        letter = random.choice(alphabet)
        if letter not in grid_lst:
            grid_lst.append(letter)
    return grid_lst


def get_words(file_name, letters):
    """gets words from the file and puts it in the dic"""
    dict_of_words = {}
    parts_of_speech = ["/n", "noun", "adj", "/v", "verb", "adv", ]
    with open(file_name, "r") as file_ukr:
        for line in file_ukr:
            line = line.split()
            if len(line[0]) <= 5 and line[0][0] in letters:
                for i in parts_of_speech:
                    if i in line[1]:
                        dict_of_words[line[0]] = i
    return dict_of_words


def check_user_words(user_words, language_part, letters, dict_of_words):
    pass

print(generate_grid())
print(get_words("base.lst", ["а", "м", "п", "с", "у"]))
