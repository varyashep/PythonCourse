print("Введите число: ")
num = int(input())

k = 0
while (2**k <= num):
    print(f"Степень {k} : {2**k}")
    k += 1
