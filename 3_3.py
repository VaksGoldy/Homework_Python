from random import choice
from random import shuffle


def get_jokes(numb):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adv = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adj = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(numb):
        print(choice(nouns), choice(adv), choice(adj))


n = int(input(' Введи количество шуток '))
get_jokes(n)
