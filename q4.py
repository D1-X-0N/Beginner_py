user_str = input("Введите строку: ")

user_list = user_str.split()

for i, v in enumerate(user_list, 1):
    if len(v) > 20:
        print(f"{i}) {v[:10]}...")
    else:
        print(f"{i}) {v}")
