print("Введите строку (слоги разделяются дефисами):")

words = input()
count = 0
words_parted = words.split("-")
print(words_parted)
count_letters = []
for word in words_parted:
    for letter in word:
        if letter in "уеыаоэяию":
            count += 1
    count_letters.append(count)
    count = 0
print(count_letters)
all_good = True
for i in range(len(count_letters)-1):
    all_good = (lambda x: x[i] == x[i+1])(count_letters)
if all_good == True:
    print("Парам пам-пам")
else:
    print("Пам парам")