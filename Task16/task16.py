from random import randint

print("Введите длину массива: ")
length = int(input())

randomList = []
for i in range(length):
    randomList.append(randint(1,length))
print(randomList)
print("Введите число, чтобы узнать сколько раз оно встречается: ")
getNumber = int(input())
print(randomList.count(getNumber))