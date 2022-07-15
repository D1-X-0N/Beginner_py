revenue = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))

if revenue > costs:
    print(f"прибыль сосотавляет: {revenue - costs}")
    print(f"рентабильность выручки составляет: {(revenue - costs) / revenue}")
    users = int(input("Введите число сотрудников: "))
    print(f"Прибыль одного сотрудника составляет: {(revenue - costs) / users}")
elif revenue < costs:
    print(f"убыток составляет: {costs - revenue}")
else:
    print("Ушли в ноль")
