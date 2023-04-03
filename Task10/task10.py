from random import randint

print("Введите количество монет: ")
num_coins = int(input())
count_o = 0
count_r = 0
for i in range(num_coins):
    coin = randint(0,1)
    if coin == 0:
        count_o += 1
    else:
        count_r += 1

print(f"Орлы: {count_o}")
print(f"Решки: {count_r}")
if (count_o < count_r):
    print(f"Минимальное число монет, которые нужно перевернуть: {count_o}")
else:
    print(f"Минимальное число монет, которые нужно перевернуть: {count_r}")