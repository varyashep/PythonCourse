def getSquare(num1: int, num2: int) -> int:
    if num2 > 1:
        num2 -= 1
        return num1 * getSquare(num1, num2)
    else:
        return num1

print("Введите число A: ")
A = int(input())
print("Введите число B: ")
B = int(input())
print(getSquare(A,B))