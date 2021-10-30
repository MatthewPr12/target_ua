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
    dic_of_words = {}
    parts_of_speech = ["/n", "noun", "adj", "/v", "verb", "adv", ]
    with open(file_name, "r", encoding='utf-8') as file_ukr:
        for line in file_ukr:
            line = line.split()
            if len(line[0]) <= 5 and line[0][0] in letters:
                for i in parts_of_speech:
                    if i in line[1]:
                        if i in ('/n', 'noun'):
                            dic_of_words[line[0]] = "noun"
                        elif i in ('/v', 'verb'):
                            dic_of_words[line[0]] = "verb"
                        elif i == "adj":
                            dic_of_words[line[0]] = "adjective"
                        elif i == "adv":
                            dic_of_words[line[0]] = "adverb"
    return dic_of_words


def check_user_words(user_words, language_part, letters, dict_of_words):
    """checks the users words"""
    right_words = []
    lst_of_words = list(dict_of_words.keys())
    for i in user_words:
        if i[0].lower() in letters:
            if i in lst_of_words:
                if dict_of_words[i] == language_part:
                    right_words.append(i)
                lst_of_words.remove(i)
    return right_words, lst_of_words


# if __name__ == "__main__":
#     letters = generate_grid()
#     dict_of_words = get_words("base.lst", letters)
#     print(letters)
#     print(dict_of_words)
