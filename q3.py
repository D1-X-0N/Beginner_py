n = int(input("введите номер месяца: "))

seasons = {
    "spring": [3, 4, 5],
    "summer": [6, 7, 8],
    "autumn": [9, 10, 11],
    "winter": [1, 2, 12]
}

for el in seasons:
    if n in seasons[el]:
        print(el)
        break
else:
    print("такого месяца не существует")
