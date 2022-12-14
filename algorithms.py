
#  Бинарный поиск

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#     while low <= high:
#         mid = int((low + high) / 2)  # int?
#         guess = list[mid]
#         if guess == item:
#             return mid
#         elif guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None


# print(binary_search(my_list, 3))
# print(binary_search(my_list, -1))

# Сортировка выбором

a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47,
     57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41,
     -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56,
     71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20,
     -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93,
     -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

n = len(a)
for i in range(n - 1):
    for k in range(i + 1, n):
        if a[k] < a[i]:
            a[k], a[i] = a[i], a[k]
print(a)
