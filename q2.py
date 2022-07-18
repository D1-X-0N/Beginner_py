test_list = [2, 'text', 456, 45.3, True, [1, 2], ("pop, sort"), {"a", "b"}, {
    "a": 1, "b": 2}, None]

for i in range(1, len(test_list), 2):
    print(i)
    test_list[i], test_list[i - 1] = test_list[i - 1], test_list[i]

print(test_list)
