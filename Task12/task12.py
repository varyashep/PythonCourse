import math

print("Введите сумму чисел: ")
sum = int(input())
print("Введите произведение чисел: ")
multi = int(input())

y1 = (sum + math.sqrt(sum**2 - 4*multi))/2
y2 = (sum - math.sqrt(sum**2 - 4*multi))/2

if (y1 > sum):
    x = sum - y2
    print(f"Число 1: {y2}")
else:
    x = sum - y1
    print(f"Число 1: {y1}")


print(f"Число 2: {x}")