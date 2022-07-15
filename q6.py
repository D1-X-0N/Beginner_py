a = float(input("Введите дистанцию, которую вы сегодня пробежали: "))
b = float(input("Введите дистанцию, которую вы хотите пробежать: "))

days = 1

while a < b:
    a *= 1.1
    print(a)
    days += 1
print(days)
