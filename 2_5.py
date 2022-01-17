values = [57.8, 46.51, 97, 121.7, 63.22, 93.1, 69]
sort_values = []
for el in values:
    rub = int(el)
    kop = int((el * 100) % 100)
    sort_values.extend([f'{rub} руб {kop:02} коп'])
txt = ', '.join(sort_values)
print(txt)
print(id(values))
values.sort()
print(values)
print(id(values))
srt_values = sorted(values, reverse=True)
print(srt_values)
print(sorted(srt_values[:5]))
