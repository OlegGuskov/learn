"""Квадратичные функции сортировки"""


def choise_sort(lst: list) -> list:
    """Сортировка списка А выбором"""
    n = len(lst)
    for pos in range(n - 1):
        for k in range(pos + 1, n):
            if lst[k] < lst[pos]:
                lst[pos], lst[k] = lst[k], lst[pos]


def bubble_sort(lst: list) -> list:
    """Cортировка списка А пузырьками"""
    n = len(lst)

# Variant 1 "Backward"

    for pos in range(n - 1):
        for k in range(n - 1, pos, -1):
            if lst[k] < lst[k - 1]:
                lst[k - 1], lst[k] = lst[k], lst[k - 1]

# Variant 2 "Forward"

    for pos in range(1, n):
        for k in range(0, n - pos):
            if lst[k] > lst[k + 1]:
                lst[k], lst[k + 1] = lst[k + 1], lst[k]


def insert_sort(lst: list) -> list:
    """Сортировка списка А вставками"""
    n = len(lst)

# Variant 1

    for pos in range(1, n):
        for k in range(pos):
            if lst[pos] < lst[k]:
                lst.insert(k, lst.pop(pos))

# Variant 2

    for pos in range(1, n):
        i = pos
        while i > 0 and lst[i] < lst[i - 1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1


# Тесты функций сортировки


def test_sort(algorithm_sort):

    print()
    print(f'testing:  {algorithm_sort.__doc__}', end='\n\n')

    print('testcase 1', end=' ')
    lst = [5, 9, -3, 4, 12, 2, 8]
    lst_sorted = [-3, 2, 4, 5, 8, 9, 12]
    algorithm_sort(lst)
    print('  OK!' if lst == lst_sorted else f'Fail!  {lst}')

    print('testcase 2', end=' ')
    lst = ['f', 'r', 'a', 't', 'c', 'q', 'b', 'g']
    lst_sorted = ['a', 'b', 'c', 'f', 'g', 'q', 'r', 't']
    algorithm_sort(lst)
    print('  OK!' if lst == lst_sorted else f'Fail!  {lst}')

    print('testcase 3', end=' ')
    lst = [0, 3, -5, 10, 8, 0, -5, 8]
    lst_sorted = [-5, -5, 0, 0, 3, 8, 8, 10]
    algorithm_sort(lst)
    print('  OK!' if lst == lst_sorted else f'Fail!  {lst}')

    print()


test_sort(choise_sort)
test_sort(bubble_sort)
test_sort(insert_sort)
