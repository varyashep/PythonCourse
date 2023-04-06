from random import randint

print("Введите длину массива: ")
length = int(input())
randomList = []
for i in range(length):
    randomList.append(randint(1, length))
randomList.sort()
print(randomList)
print("Введите число: ")
getNumber = int(input())
diffs = []
getDif = 0
for i in range(length):
    getDif = abs(randomList[i] - getNumber)
    diffs.append(getDif)
finalOut = []
for i in range(length):
    if diffs[i] == min(diffs):
        finalOut.append(randomList[i])
print(set(finalOut))