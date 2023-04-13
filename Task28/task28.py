def sum(a,b,summa):
    if (summa < a + b):
        return sum(a, b, summa + 1)
    else:
        return summa 

print("Введите число А: ")
num1 = int(input())
print("Введите число B: ")
num2 = int(input())
cur_sum = 0

print(sum(num1,num2, cur_sum))