my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for el in my_list:
    if el.isdigit():
        numb = int(el)
        new_list.extend(['""', f'{numb:02d}', '""'])
    elif (el.startswith('+') or el.startswith('-')) and el[1:].isdigit():
        numb = int(el[1:])
        new_list.extend(['""', f'{el[0]}{numb:02d}', '""'])
    else:
        new_list.append(el)
    new_list.extend(' ')
txt = "".join(new_list)
print(txt)
