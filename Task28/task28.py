def sum(a,b):
    if (a == 0):
        return b
    else:
        a -= 1
        b += 1
        return sum(a,b)
    
print("Введите число А: ")
num1 = int(input())
print("Введите число B: ")
num2 = int(input())


print(sum(num1,num2))