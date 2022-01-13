numbers = []
bad = [11, 12, 13, 14, 15, 16, 17, 18, 19]
for i in range(100):
    numbers.append(i+1)
print(numbers)
for i in range(len(numbers)):
    if numbers[i] in bad:
        print(numbers[i], "процентов")
    elif numbers[i] % 10 == 1:
        print(numbers[i], "процент")
    elif numbers[i] % 10 == 2 or numbers[i] % 10 == 3 or numbers[i] % 10 == 4:
        print(numbers[i], "процента")
    elif numbers[i] % 10 == 5 or 6 or 7 or 8 or 9:
        print(numbers[i], "процентов")
