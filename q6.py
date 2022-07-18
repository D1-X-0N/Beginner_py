cart = []
result_stat = {"название": [],
               "цена": [],
               "количество": [],
               "ед": ["шт."]
               }

count = int(input("Введите количество товаров: "))
temp = 0

while temp != count:
    item = (temp + 1, {'eд': 'шт.'})
    name = input("Введите название товара: ")
    item[1]["название"] = name
    price = int(input("Введите цену товара: "))
    item[1]["цена"] = price
    quantity = int(input("Введите количество товара: "))
    item[1]["количество"] = quantity
    temp += 1
    cart.append(item)

for i in range(count):
    result_stat["название"].append(cart[i][1]["название"])
    result_stat["цена"].append(cart[i][1]["цена"])
    result_stat["количество"].append(cart[i][1]["количество"])

print(result_stat)
