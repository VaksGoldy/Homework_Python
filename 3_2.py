def thesaurus(*args):
    my_dict = {}
    for el in args:
        my_dict.setdefault(el.split()[1][0], {}).setdefault(el.split()[0][0], []).append(el)
    return my_dict


print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
