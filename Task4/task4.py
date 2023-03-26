print("Шоколадка NxM. Введите N: ")
n = int(input())
print("Введите M:")
m = int(input())
print("Введите кол-во долек: ")
k = int(input())

if (k % n == 0) or (k % m == 0):
    print(f"Можно отломить")
else:
    print(f"Нельзя отломить.")