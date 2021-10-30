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
    dic_of_words = []
    parts_of_speech = ["/n", "noun", "adj", "/v", "verb", "adv", ]
    with open(file_name, "r", encoding='utf-8') as file_ukr:
        for line in file_ukr:
            line = line.split()
            if len(line[0]) <= 5 and line[0][0] in letters:
                for i in parts_of_speech:
                    if i in line[1][:5]:
                        if i in ('/n', 'noun'):
                            dic_of_words.append((line[0], "noun"))
                        elif i in ('/v', 'verb'):
                            dic_of_words.append((line[0], "verb"))
                        elif i == "adj":
                            dic_of_words.append((line[0], "adjective"))
                        elif i == "adv":
                            dic_of_words.append((line[0], "adverb"))
    return dic_of_words


def check_user_words(user_words, language_part, letters, dict_of_words):
    """checks the users words"""
    right_words = []
    missed_words = []
    lst_of_words = []
    lst_of_parts = []
    for i in dict_of_words:
        lst_of_words.append(i[0])
        lst_of_parts.append(i[1])
    for i in user_words:
        two_parts = []
        if i[0].lower() in letters:
            if i in lst_of_words:
                if lst_of_parts[lst_of_words.index(i)] == language_part:
                    right_words.append(i)
                elif lst_of_words[lst_of_words.index(i)] == lst_of_words[lst_of_words.index(i) + 1]:
                    two_parts.append(lst_of_parts[lst_of_words.index(i)])
                    two_parts.append(lst_of_parts[lst_of_words.index(i) + 1])
                    if language_part in two_parts:
                        right_words.append(i)

    for i in range(len(lst_of_words)):
        if lst_of_parts[i] == language_part and lst_of_words[i] not in right_words:
            missed_words.append(lst_of_words[i])
    return right_words, missed_words


if __name__ == "__main__":
    # print(sorted(set(get_words("base.lst", ['щ']))))
    # print(sorted(set(get_words("base.lst", ['й', 'є', 'ю']))))
    # print(check_user_words([], "verb", ['щ', 'ш', 'ь', 'у', 'ц'], get_words("base.lst", ['щ', 'ш', 'ь', 'у', 'ц'])))
    # print(get_words("base.lst", ['ф', 'у', 'щ', 'б', 'л']))
    print(check_user_words(['гаяти', 'гнати', 'ініціалізація', 'узяти', 'щавель'], "verb", ['ю', 'щ', 'я', 'ц', 'г'], get_words("base.lst", ['ю', 'щ', 'я', 'ц', 'г'])))
    print(check_user_words(
        ['бабин', 'битий', 'бичий', 'білий', 'бісів', 'богів', 'божий', 'босий', 'булий', 'булів', 'бурий', 'ласий',
         'лисий', 'литий', 'лихий', 'лівий', 'любий', 'лютий', 'усний', 'утлий', 'щирий', 'щучий', 'щучин'],
        "adjective", ['ф', 'у', 'щ', 'б', 'л'], get_words("base.lst", ['ф', 'у', 'щ', 'б', 'л'])))
    print(check_user_words([], "adverb", ['ш', 'ь', 'т', 'і', 'х'], get_words("base.lst", ['ш', 'ь', 'т', 'і', 'х'])))
