print("Введите трехзначное число:")
s = int(input())

dig1 = s // 100
dig2 = (s // 10) % 10
dig3 = s % 10

sum = dig1 + dig2 + dig3

print(f"Сумма цифр числа: {sum}")