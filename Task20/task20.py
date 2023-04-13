print("Введите слово: ")
word = input()

getLetters = {}
for item in word:
    getLetters[item] = getLetters.get(item, 0) + 1
#print(getLetters['П'])
count = 0
for i in word:
    if i in "AEIOULNSTRАВЕИНОРСТ":
        count += getLetters.get(i)
    elif i in "DGДКЛМПУ":
        count += 2 * getLetters.get(i)
    elif i in "BCMPБГЁЬЯ":
        count += 3 * getLetters[i]
    elif i in "FHVWYЙЫ":
        count += 4 * getLetters[i]
    elif i == "KЖЗХЦЧ":
        count += 5 * getLetters[i]
    elif i in "JXШЭЮ":
        count += 8 * getLetters[i]
    else:
        count += 10 * getLetters[i]
print(count)