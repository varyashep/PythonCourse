print("Введите номер билета: ")
number = str(input())
half1 = int(number[0]) + int(number[1]) + int(number[2])
half2 = int(number[-3]) + int(number[-2]) + int(number[-1])

if (half1 == half2):
    print("Билет счастливый")
else:
    print("Обычный билет")