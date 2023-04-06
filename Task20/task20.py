print("Введите слово: ")
word = input()

count = 0
for i in word.upper():
    if i in "AEIOULNSTRАВЕИНОРСТ":
        count += 1
    elif i in "DGДКЛМПУ":
        count += 2
    elif i in "BCMPБГЁЬЯ":
        count += 3
    elif i in "FHVWYЙЫ":
        count += 4
    elif i == "KЖЗХЦЧ":
        count += 5
    elif i in "JXШЭЮ":
        count += 8
    else:
        count += 10
print(count)