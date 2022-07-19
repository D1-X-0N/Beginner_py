my_list = [10, 7, 7, 5, 4, 2, 2]
result_list = []

n = int(input("Введите новое число: "))
if n in my_list:
    ind = my_list[::-1].index(n)
    print(ind)
    if my_list[-1] == n:
        my_list.append(n)
        result_list = my_list
    else:
        result_list = my_list[:-ind] + [n] + my_list[-ind:]
else:
    for i, v in enumerate(my_list):
        if n > v:
            result_list = my_list[:i] + [n] + my_list[i:]
            break
        if n < my_list[-1]:
            my_list.append(n)
            result_list = my_list
            break
print(result_list)
