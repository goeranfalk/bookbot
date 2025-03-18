def get_num_words(content):
    word = content.split()
    return len(word)


def letter_count(st):
    letter = {}
    for x in st:
        lowered = x.lower()
        if lowered in letter:
            letter[lowered] += 1
        else:
            letter[lowered] = 1
    return letter


def sort_on(input_dict):
    result_list = []
    for key, value in input_dict.items():
        result_list.append({"name": key, "num": value})
    result_list.sort(key=lambda x: x["num"], reverse=True)
    return result_list
