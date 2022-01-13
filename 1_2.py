numbers = []
for el in range(1000):
    if el % 2 != 0:
        numb = el ** 3
        numbers.append(numb)
print(numbers)
summ1 = 0
for el in range(len(numbers)):
    summ = 0
    num = numbers[el]
    while num != 0:
        summ = summ + (num % 10)
        num = num // 10
    if summ % 7 == 0:
        print(numbers[el], summ)
        summ1 += numbers[el]
print(summ1)
summ2 = 0
for el in range(len(numbers)):
    summ = 0
    num = numbers[el] + 17
    while num != 0:
        summ = summ + (num % 10)
        num = num // 10
    if summ % 7 == 0:
        print(numbers[el] + 17, summ)
        summ2 += numbers[el] + 17
print(summ2)
