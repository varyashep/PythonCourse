def getSquare(num1: int, num2: int) -> int:
    k = 1
    finalNum = 1
    while k <= num2:
        finalNum *= num1
        k += 1
    return finalNum

print("Введите число A: ")
A = int(input())
print("Введите число B: ")
B = int(input())
print(getSquare(A,B))