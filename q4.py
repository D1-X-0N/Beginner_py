num = int(input("Введите число: "))

result = 0

while num:
    if num % 10 > result:
        result = num % 10
    num //= 10

print(result)
