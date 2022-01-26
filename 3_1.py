def translate(numb):
    """Перевод чисел от 1 до 10 с английского на русский"""
    numbs = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
             'seven': 'семь', 'eight': 'восем', 'nine': 'девять', 'ten': 'десять'}
    return numbs.get(numb)


number = input('Введи число от 1 до 10 на английском ')
if number[0].isupper():
    print(f' {(translate(number.lower())).title()}')
else:
    print(translate(number))
